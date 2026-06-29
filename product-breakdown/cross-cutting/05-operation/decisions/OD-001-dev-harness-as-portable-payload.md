# OD-001: Dev Harness As Portable Payload

## Status

Accepted

## Layer

Operation

## Context

The system_dev_harness package provides agent prompts, workflow policies, and product-breakdown context that must be usable across multiple target development repositories. Each target repository should receive a self-contained copy of the runtime context without depending on a shared installation location, network service, or external database. The deployment model needs to be simple, reliable, and inspectable.

## Decision

Package the dev harness as a **copyable portable payload**:

- The runtime context (agent prompts, workflow policies, product-breakdown guidance, templates) lives under `.opencode/dev_harness/` in this package repository.
- A Python sync CLI (`system-dev-harness-sync`) copies the relevant runtime files into a target repository's `.opencode/dev_harness/` directory.
- The sync is one-directional: package → target. No runtime synchronization or background services.
- The sync manifest (`.opencode/dev_harness/.sync-manifest.json`) tracks which files were copied and when, providing a lightweight audit trail.
- The product-breakdown source documentation (`product-breakdown/`) stays in this package repository. Target repositories receive only the copied guidance under `.opencode/dev_harness/product-breakdown/`.
- The package README documents the copy procedure.

## Alternatives Considered

- **Git submodule**: Target repositories reference the package via git submodule — adds git complexity, version pinning overhead, and merge conflicts.
- **Package manager install**: Install via pip/npm — adds external dependency and build step; version resolution may conflict with target environment.
- **Network service**: Serve the harness from a central service — adds infrastructure dependency and availability risk.
- **Manual copy**: Users manually copy files — error-prone, no audit trail, inconsistent across targets.

## Consequences

**Positive:**
- Simple deployment: copy files into target repository.
- No external runtime dependencies.
- Fully inspectable: all runtime context is on disk in the target repository.
- Sync manifest provides audit trail.

**Negative:**
- Target repositories can modify or diverge from the copied context — no automatic update mechanism.
- Sync is one-directional, requiring re-copy for updates.
- The Python CLI must be installed or run from this repository.

## Affected Artifacts

- `pyproject.toml` — Package definition and CLI entry point
- `src/system_dev_harness_sync/` — Python sync CLI implementation
- `product-breakdown/pbs/03-implementation/implementation.md` — Mechanism storage rules
- `product-breakdown/cross-cutting/05-operation/deployment-process.md` — Deployment requirements
- `README.md` — Copy procedure documentation

## Verification

Running `system-dev-harness-sync` against a test target directory produces a `.opencode/dev_harness/` subtree with all required runtime files and a `.sync-manifest.json`. The target repository is independently usable without referencing this package.

## Review Trigger

When the runtime payload grows beyond a manageable size (suggested threshold: >50 MB), or when the copy procedure becomes error-prone for users, revisit the deployment mechanism.