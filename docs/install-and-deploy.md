# Install and Deploy

## Package Deployment

The workflow package is deployed by copying `opencode.json` and `.opencode/` into a target development repository.

## Steps

1. Clone or open the target development repository.
2. Copy `opencode.json` into the repository root.
3. Copy the `.opencode/` directory into the repository root.
4. Leave `system_definition/` in this repository; it is source documentation, not runtime payload.

## Dependency Handling

The `.opencode/package.json` file declares the OpenCode plugin dependency, and `.opencode/.gitignore` excludes `node_modules`, `package.json`, `package-lock.json`, and `bun.lock` from the copied runtime tree. Treat the copied manifest as the source of truth for the runtime dependency set.

## Update Process

1. Pull the latest changes from this repository.
2. Re-copy `opencode.json` and `.opencode/` into the target repository.
3. Review `git diff` in the target repository to confirm only the intended changes were applied.

## Local Sync Helper

Install the package locally from this repository:

```bash
python -m pip install -e .
```

Then sync the latest payload into a target repository:

```bash
cd /path/to/target/repo
system-dev-harness-sync
```

With no arguments, the helper syncs from the default online repository into the current directory and prunes obsolete previously synced payload files. It copies the tracked runtime payload (`opencode.json` and `.opencode/`) and writes `.opencode/dev_harness/.sync-manifest.json` in the target. Pruning removes files from the previous sync manifest that no longer exist upstream, plus known legacy payload paths such as the old `.opencode/instructions.md`.

Use `--no-prune` to copy current files without removing obsolete files:

```bash
system-dev-harness-sync --no-prune
```

Use `--dry-run` to preview changes:

```bash
system-dev-harness-sync --dry-run
```

Use `--source` and `--ref` to override the repository or branch:

```bash
system-dev-harness-sync --source git@github.com:jkCXf9X4/system_dev_harness.git --ref main --target /path/to/target/repo
```
