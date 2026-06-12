from __future__ import annotations

import json
from pathlib import Path

from system_dev_harness_sync.cli import build_parser
from system_dev_harness_sync import SyncOptions, sync_payload


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def test_sync_payload_copies_current_files_and_writes_manifest(tmp_path: Path) -> None:
    source = tmp_path / "source"
    target = tmp_path / "target"
    write(source / "opencode.json", '{"default_agent": "orchestrator"}\n')
    write(source / ".opencode/dev_harness/instructions.md", "# Instructions\n")
    write(source / ".opencode/dev_harness/.sync-manifest.json", "{}\n")
    write(source / ".opencode/dev_harness_plans/2026-01-01-example.md", "generated\n")
    write(source / ".opencode/node_modules/cache.js", "ignored\n")

    result = sync_payload(SyncOptions(target=target, source=str(source)))

    assert sorted(result.copied) == [
        ".opencode/dev_harness/instructions.md",
        "opencode.json",
    ]
    assert (target / "opencode.json").read_text(encoding="utf-8") == '{"default_agent": "orchestrator"}\n'
    assert (target / ".opencode/dev_harness/instructions.md").exists()
    assert not (target / ".opencode/dev_harness_plans/2026-01-01-example.md").exists()
    assert not (target / ".opencode/node_modules/cache.js").exists()

    manifest = json.loads(
        (target / ".opencode/dev_harness/.sync-manifest.json").read_text(encoding="utf-8")
    )
    assert manifest["files"] == [
        ".opencode/dev_harness/instructions.md",
        "opencode.json",
    ]


def test_sync_payload_prunes_previous_and_legacy_payload_files(tmp_path: Path) -> None:
    source = tmp_path / "source"
    target = tmp_path / "target"
    write(source / "opencode.json", "{}\n")
    write(source / ".opencode/dev_harness/instructions.md", "# New\n")
    write(target / ".opencode/agents/removed.md", "old\n")
    write(target / ".opencode/instructions.md", "# Legacy\n")
    write(
        target / ".opencode/dev_harness/.sync-manifest.json",
        json.dumps(
            {
                "files": [
                    "opencode.json",
                    ".opencode/agents/removed.md",
                    ".opencode/dev_harness/instructions.md",
                ]
            }
        ),
    )

    result = sync_payload(SyncOptions(target=target, source=str(source), prune=True))

    assert ".opencode/agents/removed.md" in result.removed
    assert ".opencode/instructions.md" in result.removed
    assert not (target / ".opencode/agents/removed.md").exists()
    assert not (target / ".opencode/instructions.md").exists()
    assert (target / ".opencode/dev_harness/instructions.md").exists()


def test_dry_run_reports_without_writing(tmp_path: Path) -> None:
    source = tmp_path / "source"
    target = tmp_path / "target"
    write(source / "opencode.json", "{}\n")

    result = sync_payload(SyncOptions(target=target, source=str(source), dry_run=True))

    assert result.copied == ["opencode.json"]
    assert not (target / "opencode.json").exists()
    assert not (target / ".opencode/dev_harness/.sync-manifest.json").exists()


def test_cli_defaults_to_current_directory_default_source_and_prune() -> None:
    args = build_parser().parse_args([])

    assert args.target == Path.cwd()
    assert args.ref == "main"
    assert args.prune is True


def test_cli_no_prune_disables_default_prune() -> None:
    args = build_parser().parse_args(["--no-prune"])

    assert args.prune is False
