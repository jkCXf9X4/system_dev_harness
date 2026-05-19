from __future__ import annotations

import argparse
import shutil
from pathlib import Path
from uuid import uuid4

from devfix.harness.lessons import parse_lessons
from devfix.output import export_run_failure, export_run_output
from devfix.runner import build_context, default_mcp_policy, read_optional, read_waivers, run_with_executor

DEFAULT_PROMPT = Path(".agents/devfix/PROMPT.md")
DEFAULT_STORAGE = Path(".agents/devfix")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run devfix from the active .agents/devfix prompt.")
    parser.add_argument(
        "--prompt",
        type=Path,
        default=DEFAULT_PROMPT,
        help="Prompt file to execute. Defaults to .agents/devfix/PROMPT.md.",
    )
    parser.add_argument("--context", default="", help="Optional stakeholder, product, or technical context.")
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
        help="Disable automatic grounding from docs/03-system-architecture and docs/04-technical-decisions.",
    )
    parser.add_argument(
        "--lessons",
        type=Path,
        default=Path("docs/07-lessons/known-mistakes.md"),
        help="Path to persistent known mistakes and lessons.",
    )
    parser.add_argument("--thread-id", default=None, help="Stable LangGraph thread id for checkpointed runs.")
    parser.add_argument("--changed-file", action="append", default=[], help="Changed file evidence.")
    parser.add_argument("--diff", type=Path, default=None, help="Diff or diff summary evidence file.")
    parser.add_argument("--test-output", type=Path, default=None, help="Test/check output evidence file.")
    parser.add_argument("--agent-output", type=Path, default=None, help="External coding-agent response evidence file.")
    parser.add_argument("--waivers", type=Path, default=None, help="JSON waiver request file.")
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=None,
        help="Optional directory to export run artifacts, final report, and metadata.",
    )
    parser.add_argument(
        "--executor",
        choices=["none", "mcp", "manual", "opencode"],
        default="mcp",
        help="Execution backend. 'mcp' performs governed in-graph repo access, edits, and verification.",
    )
    parser.add_argument(
        "--execution-mode",
        choices=["headless", "interactive"],
        default="headless",
        help="Execution mode for adapters that support it.",
    )
    parser.add_argument("--opencode-attach", default="", help="Optional opencode server URL.")
    parser.add_argument("--opencode-model", default="", help="Optional opencode model in provider/model format.")
    parser.add_argument("--opencode-agent", default="", help="Optional opencode agent name.")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    _ensure_local_storage()
    env_message = _ensure_env()

    if not args.prompt.exists():
        raise SystemExit(f"Prompt file not found: {args.prompt}")
    prompt = args.prompt.read_text(encoding="utf-8").strip()
    if not prompt:
        raise SystemExit(f"{args.prompt} is empty.")

    lessons_warning = ""
    if args.lessons.exists():
        lessons = [lesson.model_dump() for lesson in parse_lessons(args.lessons.read_text(encoding="utf-8"))]
    else:
        lessons = []
        lessons_warning = f"\n\n> Warning: lessons file not found: `{args.lessons}`. Continuing with empty mistake memory.\n"

    thread_id = args.thread_id or f"devfix-{uuid4()}"
    config = {"configurable": {"thread_id": thread_id}}
    context = build_context(args.context, args.context_file, include_defaults=not args.no_default_context)
    initial_state = {
        "backlog_item": prompt,
        "execution_backend": args.executor,
        "mcp_policy": default_mcp_policy(),
        "stakeholder_context": context,
        "lessons": lessons,
        "changed_files": args.changed_file,
        "diff_summary": read_optional(args.diff),
        "test_output": read_optional(args.test_output),
        "agent_output": read_optional(args.agent_output),
        "waiver_requests": read_waivers(args.waivers),
        "artifacts": [],
        "tool_trace": [],
    }

    try:
        result = run_with_executor(args, initial_state, config)
    except Exception as exc:
        if args.output_dir is not None:
            export_run_failure(
                args.output_dir,
                thread_id=thread_id,
                prompt_path=args.prompt,
                executor=args.executor,
                prompt_text=prompt,
                error=exc,
            )
        raise SystemExit(f"devfix run failed: {exc}") from exc

    print(f"# Devfix Harness Result\n\nThread: `{thread_id}`{env_message}{lessons_warning}\n")
    print(result["final_control_report"])

    if args.output_dir is not None:
        export_run_output(
            args.output_dir,
            thread_id=thread_id,
            prompt_path=args.prompt,
            executor=args.executor,
            result=result,
        )


def _ensure_local_storage() -> None:
    DEFAULT_STORAGE.mkdir(parents=True, exist_ok=True)


def _ensure_env() -> str:
    env_path = Path(".env")
    example_path = Path(".env.example")
    if env_path.exists():
        return ""
    if not example_path.exists():
        return "\n\n> Warning: `.env` is missing and `.env.example` was not found.\n"
    shutil.copyfile(example_path, env_path)
    return "\n\n> Created `.env` from `.env.example`; set `OPENROUTER_API_KEY` before model execution.\n"


if __name__ == "__main__":
    main()
