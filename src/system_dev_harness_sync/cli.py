from __future__ import annotations

import argparse
from pathlib import Path

from .sync import DEFAULT_REPOSITORY, SyncOptions, sync_payload


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="system-dev-harness-sync",
        description="Sync the OpenCode dev harness payload into a local repository.",
    )
    parser.add_argument(
        "--target",
        type=Path,
        default=Path.cwd(),
        help="Target repository root to update. Defaults to the current directory.",
    )
    parser.add_argument(
        "--source",
        default=DEFAULT_REPOSITORY,
        help=(
            "Git repository URL or local source checkout. "
            f"Defaults to {DEFAULT_REPOSITORY!r}."
        ),
    )
    parser.add_argument(
        "--ref",
        default="main",
        help="Git ref, branch, or tag to sync when --source is a Git URL. Defaults to main.",
    )
    parser.add_argument(
        "--prune",
        dest="prune",
        action="store_true",
        default=True,
        help="Remove files that belonged to a previous harness sync but are absent upstream. Enabled by default.",
    )
    parser.add_argument(
        "--no-prune",
        dest="prune",
        action="store_false",
        help="Copy current payload files without removing obsolete previously synced files.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print planned changes without writing files.",
    )
    parser.add_argument(
        "--keep-temp",
        action="store_true",
        help="Keep the temporary clone directory for debugging.",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    result = sync_payload(
        SyncOptions(
            target=args.target,
            source=args.source,
            ref=args.ref,
            prune=args.prune,
            dry_run=args.dry_run,
            keep_temp=args.keep_temp,
        )
    )

    for path in result.copied:
        print(f"copy {path}")
    for path in result.removed:
        print(f"remove {path}")
    for path in result.skipped:
        print(f"skip {path}")
    if result.manifest_path:
        action = "would write" if args.dry_run else "wrote"
        print(f"{action} manifest {result.manifest_path}")
    if result.source_commit:
        print(f"source commit {result.source_commit}")

    return 0
