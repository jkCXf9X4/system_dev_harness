from __future__ import annotations

import argparse
from pathlib import Path
from uuid import uuid4

from harness.graph import build_graph


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
        lessons = args.lessons.read_text(encoding="utf-8").strip()
    else:
        lessons = ""
        lessons_warning = f"\n\n> Warning: lessons file not found: `{args.lessons}`. Continuing with empty mistake memory.\n"

    graph = build_graph()
    thread_id = args.thread_id or f"run-{uuid4()}"
    config = {"configurable": {"thread_id": thread_id}}

    try:
        result = graph.invoke(
            {
                "backlog_item": backlog_item,
                "stakeholder_context": args.context,
                "lessons": lessons,
                "artifacts": [],
            },
            config=config,
        )
    except RuntimeError as exc:
        raise SystemExit(str(exc)) from exc

    print(f"# Guarded Agentic Development Harness Result\n\nThread: `{thread_id}`{lessons_warning}\n")
    print(result["final_control_report"])


if __name__ == "__main__":
    main()
