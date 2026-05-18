from __future__ import annotations

import argparse
import json
from pathlib import Path
from uuid import uuid4

from harness.graph import build_graph
from harness.lessons import parse_lessons


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

    graph = build_graph()
    thread_id = args.thread_id or f"run-{uuid4()}"
    config = {"configurable": {"thread_id": thread_id}}
    stakeholder_context = _build_context(args.context, args.context_file, include_defaults=not args.no_default_context)

    try:
        result = graph.invoke(
            {
                "backlog_item": backlog_item,
                "stakeholder_context": stakeholder_context,
                "lessons": lessons,
                "changed_files": args.changed_file,
                "diff_summary": _read_optional(args.diff),
                "test_output": _read_optional(args.test_output),
                "agent_output": _read_optional(args.agent_output),
                "waiver_requests": _read_waivers(args.waivers),
                "artifacts": [],
            },
            config=config,
        )
    except Exception as exc:
        raise SystemExit(f"Harness run failed: {exc}") from exc

    print(f"# Guarded Agentic Development Harness Result\n\nThread: `{thread_id}`{lessons_warning}\n")
    print(result["final_control_report"])


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
