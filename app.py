from __future__ import annotations

import argparse
import json
from pathlib import Path
from uuid import uuid4

from harness.execution import ManualAdapter, OpenCodeAdapter
from harness.graph import build_graph, build_packet_graph, build_review_graph
from harness.lessons import parse_lessons
from harness.schemas import EvidenceBundle, ExternalAgentHandoff


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run the guarded agentic development harness.")
    parser.add_argument(
        "--backlog",
        type=Path,
        required=True,
        help="Path to a backlog item, stakeholder note, or feature request.",
    )
    parser.add_argument(
        "--context",
        default="",
        help="Optional stakeholder, product, or technical context.",
    )
    parser.add_argument(
        "--context-file",
        action="append",
        type=Path,
        default=[],
        help="Optional project context file. May be provided multiple times.",
    )
    parser.add_argument(
        "--no-default-context",
        action="store_true",
        help="Disable automatic grounding from docs/architecture.md, docs/requirements.md, and ADRs.",
    )
    parser.add_argument(
        "--lessons",
        type=Path,
        default=Path("docs/lessons/known-mistakes.md"),
        help="Path to persistent known mistakes and lessons.",
    )
    parser.add_argument(
        "--thread-id",
        default=None,
        help="Stable LangGraph thread id for checkpointed runs.",
    )
    parser.add_argument(
        "--changed-file",
        action="append",
        default=[],
        help="Changed file from external coding-agent output. May be provided multiple times.",
    )
    parser.add_argument(
        "--diff",
        type=Path,
        default=None,
        help="Optional file containing diff or diff summary from external implementation.",
    )
    parser.add_argument(
        "--test-output",
        type=Path,
        default=None,
        help="Optional file containing test/check output from external implementation.",
    )
    parser.add_argument(
        "--agent-output",
        type=Path,
        default=None,
        help="Optional file containing the external coding agent's final response.",
    )
    parser.add_argument(
        "--waivers",
        type=Path,
        default=None,
        help="Optional JSON file containing waiver requests.",
    )
    parser.add_argument(
        "--executor",
        choices=["none", "manual", "opencode"],
        default="none",
        help="Execution adapter to run after handoff generation.",
    )
    parser.add_argument(
        "--execution-mode",
        choices=["headless", "interactive"],
        default="headless",
        help="Execution mode for adapters that support it.",
    )
    parser.add_argument(
        "--opencode-attach",
        default="",
        help="Optional opencode server URL, for example http://localhost:4096.",
    )
    parser.add_argument(
        "--opencode-model",
        default="",
        help="Optional opencode model in provider/model format.",
    )
    parser.add_argument(
        "--opencode-agent",
        default="",
        help="Optional opencode agent name.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if not args.backlog.exists():
        raise SystemExit(f"Backlog file not found: {args.backlog}")

    backlog_item = args.backlog.read_text(encoding="utf-8").strip()
    if not backlog_item:
        raise SystemExit(f"{args.backlog} is empty.")

    lessons_warning = ""
    if args.lessons.exists():
        lessons = [lesson.model_dump() for lesson in parse_lessons(args.lessons.read_text(encoding="utf-8"))]
    else:
        lessons = []
        lessons_warning = f"\n\n> Warning: lessons file not found: `{args.lessons}`. Continuing with empty mistake memory.\n"

    thread_id = args.thread_id or f"run-{uuid4()}"
    config = {"configurable": {"thread_id": thread_id}}
    stakeholder_context = _build_context(args.context, args.context_file, include_defaults=not args.no_default_context)

    initial_state = {
        "backlog_item": backlog_item,
        "stakeholder_context": stakeholder_context,
        "lessons": lessons,
        "changed_files": args.changed_file,
        "diff_summary": _read_optional(args.diff),
        "test_output": _read_optional(args.test_output),
        "agent_output": _read_optional(args.agent_output),
        "waiver_requests": _read_waivers(args.waivers),
        "artifacts": [],
    }

    try:
        result = _run_with_executor(args, initial_state, config)
    except Exception as exc:
        raise SystemExit(f"Harness run failed: {exc}") from exc

    print(f"# Guarded Agentic Development Harness Result\n\nThread: `{thread_id}`{lessons_warning}\n")
    print(result["final_control_report"])


def _run_with_executor(args: argparse.Namespace, initial_state: dict, config: dict) -> dict:
    if args.executor == "none":
        return build_graph().invoke(initial_state, config=config)

    packet_state = build_packet_graph().invoke(initial_state, config=config)
    handoff = ExternalAgentHandoff.model_validate(packet_state["external_agent_handoff"])
    adapter = _build_adapter(args)
    execution = adapter.execute(handoff, title=_task_title(packet_state), workdir=Path.cwd())
    evidence = execution.evidence

    merged_state = {
        **packet_state,
        "changed_files": evidence.changed_files or initial_state.get("changed_files", []),
        "diff_summary": evidence.diff_summary or initial_state.get("diff_summary", ""),
        "test_output": evidence.test_output or initial_state.get("test_output", ""),
        "agent_output": evidence.agent_output or initial_state.get("agent_output", ""),
        "waiver_requests": [waiver.model_dump() for waiver in evidence.waiver_requests],
        "artifacts": [
            *packet_state.get("artifacts", []),
            f"## Execution Session\n\n```json\n{execution.session.model_dump_json(indent=2)}\n```",
        ],
    }
    return build_review_graph().invoke(merged_state, config=config)


def _build_adapter(args: argparse.Namespace):
    if args.executor == "manual":
        return ManualAdapter()
    if args.executor == "opencode":
        return OpenCodeAdapter(
            mode=args.execution_mode,
            attach_url=args.opencode_attach,
            model=args.opencode_model,
            agent=args.opencode_agent,
        )
    raise ValueError(f"Unknown executor: {args.executor}")


def _task_title(state: dict) -> str:
    contract = state.get("requirement_contract", {})
    title = str(contract.get("task_objective") or "system-dev-harness task")
    return title[:80]


def _read_optional(path: Path | None) -> str:
    if path is None:
        return ""
    if not path.exists():
        raise SystemExit(f"Evidence file not found: {path}")
    return path.read_text(encoding="utf-8").strip()


def _build_context(user_context: str, context_files: list[Path], *, include_defaults: bool) -> str:
    sections: list[str] = []
    if user_context.strip():
        sections.append(f"## User Context\n\n{user_context.strip()}")

    if include_defaults:
        default_paths = [
            Path("docs/architecture.md"),
            Path("docs/requirements.md"),
            *sorted(Path("docs/decisions").glob("*.md")),
        ]
        for path in default_paths:
            if path.exists():
                sections.append(f"## Context File: {path}\n\n{path.read_text(encoding='utf-8').strip()}")

    for path in context_files:
        if not path.exists():
            raise SystemExit(f"Context file not found: {path}")
        sections.append(f"## Context File: {path}\n\n{path.read_text(encoding='utf-8').strip()}")

    return "\n\n".join(sections)


def _read_waivers(path: Path | None) -> list[dict[str, str]]:
    if path is None:
        return []
    if not path.exists():
        raise SystemExit(f"Waiver file not found: {path}")
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise SystemExit(f"Waiver file is not valid JSON: {path}: {exc}") from exc
    if not isinstance(data, list):
        raise SystemExit(f"Waiver file must contain a JSON array: {path}")
    return data


if __name__ == "__main__":
    main()
