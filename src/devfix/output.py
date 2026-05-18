from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any


def export_run_output(
    output_dir: Path,
    *,
    thread_id: str,
    prompt_path: Path,
    executor: str,
    result: dict[str, Any],
) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    artifacts_dir = output_dir / "artifacts"
    artifacts_dir.mkdir(parents=True, exist_ok=True)

    execution_session = result.get("execution_session")
    decision = result.get("completion_decision") or {}
    run_manifest = {
        "thread_id": thread_id,
        "prompt_path": str(prompt_path),
        "executor": executor,
        "status": decision.get("status", "unknown"),
        "final_control_report_path": "final-control-report.md" if result.get("final_control_report") else "",
        "artifacts_dir": "artifacts",
        "artifact_count": len(result.get("artifacts", [])),
        "has_execution_session": bool(execution_session),
    }
    _write_json(output_dir / "run.json", run_manifest)

    final_report = result.get("final_control_report")
    if isinstance(final_report, str) and final_report.strip():
        _write_text(output_dir / "final-control-report.md", final_report)

    if execution_session:
        _write_json(output_dir / "execution-session.json", execution_session)

    for index, artifact in enumerate(result.get("artifacts", []), start=1):
        title = _artifact_title(artifact) or f"artifact-{index:02d}"
        filename = f"{index:02d}-{_slugify(title)}.md"
        _write_text(artifacts_dir / filename, artifact)


def export_run_failure(
    output_dir: Path,
    *,
    thread_id: str,
    prompt_path: Path,
    executor: str,
    prompt_text: str,
    error: Exception,
) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    failure_manifest = {
        "thread_id": thread_id,
        "prompt_path": str(prompt_path),
        "executor": executor,
        "status": "failed",
        "error": str(error),
    }
    _write_json(output_dir / "run.json", failure_manifest)
    _write_text(
        output_dir / "run-failure.md",
        "\n".join(
            [
                "# Run Failure",
                "",
                f"- Thread: `{thread_id}`",
                f"- Prompt: `{prompt_path}`",
                f"- Executor: `{executor}`",
                "",
                "## Error",
                "",
                f"```text\n{error}\n```",
                "",
                "## Prompt",
                "",
                "```text",
                prompt_text,
                "```",
            ]
        ),
    )


def _write_json(path: Path, data: Any) -> None:
    path.write_text(json.dumps(data, indent=2, sort_keys=True), encoding="utf-8")


def _write_text(path: Path, content: str) -> None:
    path.write_text(content.rstrip() + "\n", encoding="utf-8")


def _artifact_title(artifact: str) -> str:
    match = re.search(r"^##\s+(.+)$", artifact, re.MULTILINE)
    return match.group(1).strip() if match else ""


def _slugify(value: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")
    return slug or "artifact"
