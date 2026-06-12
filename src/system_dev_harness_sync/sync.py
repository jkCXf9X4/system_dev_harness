from __future__ import annotations

import json
import shutil
import subprocess
import tempfile
from dataclasses import dataclass, field
from pathlib import Path, PurePosixPath
from typing import Iterable

DEFAULT_REPOSITORY = "git@github.com:jkCXf9X4/system_dev_harness.git"
PAYLOAD_ROOTS = ("opencode.json", ".opencode")
MANIFEST_PATH = PurePosixPath(".opencode/dev_harness/.sync-manifest.json")
LEGACY_PAYLOAD_PATHS = frozenset({".opencode/instructions.md"})
EXCLUDED_DIRS = frozenset({".git", "__pycache__", "node_modules"})


@dataclass(frozen=True)
class SyncOptions:
    target: Path
    source: str = DEFAULT_REPOSITORY
    ref: str = "main"
    prune: bool = False
    dry_run: bool = False
    keep_temp: bool = False


@dataclass
class SyncResult:
    copied: list[str] = field(default_factory=list)
    removed: list[str] = field(default_factory=list)
    skipped: list[str] = field(default_factory=list)
    manifest_path: str | None = None
    source_commit: str | None = None


@dataclass(frozen=True)
class SourceCheckout:
    path: Path
    temp_dir: Path | None = None


def sync_payload(options: SyncOptions) -> SyncResult:
    target = options.target.resolve()
    result = SyncResult()

    checkout = _prepare_source(options)
    try:
        source = checkout.path
        source_commit = _git_output(source, ["rev-parse", "HEAD"], allow_failure=True)
        result.source_commit = source_commit or None
        payload_paths = _payload_paths(source)
        old_manifest = _read_manifest(target)

        for rel_path in payload_paths:
            _copy_payload_file(source, target, rel_path, options.dry_run)
            result.copied.append(rel_path)

        if options.prune:
            for rel_path in _prune_candidates(old_manifest, payload_paths):
                target_path = target / rel_path
                if target_path.exists() and target_path.is_file():
                    if not options.dry_run:
                        target_path.unlink()
                        _remove_empty_parents(target_path.parent, target)
                    result.removed.append(rel_path)
                else:
                    result.skipped.append(rel_path)

        manifest_path = str(MANIFEST_PATH)
        result.manifest_path = manifest_path
        if not options.dry_run:
            _write_manifest(
                target,
                {
                    "source": options.source,
                    "ref": options.ref,
                    "commit": result.source_commit,
                    "payload_roots": list(PAYLOAD_ROOTS),
                    "files": payload_paths,
                },
            )
    finally:
        if checkout.temp_dir and not options.keep_temp:
            shutil.rmtree(checkout.temp_dir, ignore_errors=True)

    return result


def _prepare_source(options: SyncOptions) -> SourceCheckout:
    local_source = Path(options.source).expanduser()
    if local_source.exists():
        return SourceCheckout(local_source.resolve())

    temp_dir = Path(tempfile.mkdtemp(prefix="system-dev-harness-sync-"))
    checkout = temp_dir / "source"
    cmd = [
        "git",
        "clone",
        "--depth",
        "1",
        "--branch",
        options.ref,
        options.source,
        str(checkout),
    ]
    subprocess.run(cmd, check=True)
    return SourceCheckout(checkout, temp_dir)


def _payload_paths(source: Path) -> list[str]:
    git_paths = _git_output(source, ["ls-files", "--", *PAYLOAD_ROOTS], allow_failure=True)
    if git_paths:
        paths = [line for line in git_paths.splitlines() if _is_payload_path(line)]
    else:
        paths = list(_walk_payload_paths(source))

    return sorted(set(paths))


def _walk_payload_paths(source: Path) -> Iterable[str]:
    for root in PAYLOAD_ROOTS:
        path = source / root
        if path.is_file():
            yield root
            continue
        if not path.is_dir():
            continue
        for child in path.rglob("*"):
            if not child.is_file():
                continue
            rel = child.relative_to(source).as_posix()
            if _is_payload_path(rel):
                yield rel


def _is_payload_path(path: str) -> bool:
    rel = PurePosixPath(path)
    if rel.is_absolute() or ".." in rel.parts:
        return False
    if rel == MANIFEST_PATH:
        return False
    if any(part in EXCLUDED_DIRS for part in rel.parts):
        return False
    if (
        len(rel.parts) == 3
        and rel.parts[0] == ".opencode"
        and rel.parts[1] == "dev_harness_plans"
        and rel.suffix == ".md"
        and rel.name != "README.md"
    ):
        return False
    if rel == PurePosixPath("opencode.json"):
        return True
    return len(rel.parts) > 1 and rel.parts[0] == ".opencode"


def _copy_payload_file(source: Path, target: Path, rel_path: str, dry_run: bool) -> None:
    source_path = source / rel_path
    target_path = target / rel_path
    if not source_path.is_file():
        raise FileNotFoundError(f"payload file missing in source: {rel_path}")
    if dry_run:
        return
    target_path.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source_path, target_path)


def _prune_candidates(old_manifest: dict[str, object], payload_paths: list[str]) -> list[str]:
    current = set(payload_paths)
    previous = set()
    files = old_manifest.get("files")
    if isinstance(files, list):
        previous.update(path for path in files if isinstance(path, str) and _is_payload_path(path))
    previous.update(LEGACY_PAYLOAD_PATHS)
    return sorted(previous - current)


def _read_manifest(target: Path) -> dict[str, object]:
    manifest = target / str(MANIFEST_PATH)
    if not manifest.exists():
        return {}
    try:
        data = json.loads(manifest.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return {}
    return data if isinstance(data, dict) else {}


def _write_manifest(target: Path, data: dict[str, object]) -> None:
    manifest = target / str(MANIFEST_PATH)
    manifest.parent.mkdir(parents=True, exist_ok=True)
    manifest.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def _remove_empty_parents(path: Path, stop_at: Path) -> None:
    stop_at = stop_at.resolve()
    current = path.resolve()
    while current != stop_at and stop_at in current.parents:
        try:
            current.rmdir()
        except OSError:
            break
        current = current.parent


def _git_output(cwd: Path, args: list[str], *, allow_failure: bool = False) -> str:
    completed = subprocess.run(
        ["git", *args],
        cwd=cwd,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    if completed.returncode != 0:
        if allow_failure:
            return ""
        raise RuntimeError(completed.stderr.strip())
    return completed.stdout.strip()
