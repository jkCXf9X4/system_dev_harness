from __future__ import annotations

import argparse
import json
from pathlib import Path

from devfix.harness.execution import ManualAdapter, OpenCodeAdapter
from devfix.harness.graph import build_graph, build_packet_graph, build_review_graph
from devfix.harness.schemas import ExternalAgentHandoff


def run_with_executor(args: argparse.Namespace, initial_state: dict, config: dict) -> dict:
    if args.executor == "none":
        return build_graph().invoke(initial_state, config=config)

    packet_state = build_packet_graph().invoke(initial_state, config=config)
    handoff = ExternalAgentHandoff.model_validate(packet_state["external_agent_handoff"])
    adapter = build_adapter(args)
    execution = adapter.execute(handoff, title=task_title(packet_state), workdir=Path.cwd())
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
    result = build_review_graph().invoke(merged_state, config=config)
    result["execution_session"] = execution.session.model_dump()
    return result


def build_adapter(args: argparse.Namespace):
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


def task_title(state: dict) -> str:
    contract = state.get("requirement_contract", {})
    title = str(contract.get("task_objective") or "system-dev-harness task")
    return title[:80]


def read_optional(path: Path | None) -> str:
    if path is None:
        return ""
    if not path.exists():
        raise SystemExit(f"Evidence file not found: {path}")
    return path.read_text(encoding="utf-8").strip()


def build_context(user_context: str, context_files: list[Path], *, include_defaults: bool) -> str:
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


def read_waivers(path: Path | None) -> list[dict[str, str]]:
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
