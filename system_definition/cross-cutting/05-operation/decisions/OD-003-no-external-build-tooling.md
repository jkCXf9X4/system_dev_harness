# OD-003: No External Build Tooling

## Status

Accepted

## Layer

Operation

## Context

The system_dev_harness package depends on OpenCode as its execution platform and on a local Python CLI for syncing the runtime payload to target repositories. Beyond these, the workflow itself (agent prompts, stage definitions, gate logic) is entirely text-based — defined in markdown files and configured through opencode.json. Adding external build or CI/CD tooling (e.g., GitHub Actions, Jenkins, Makefile-based build pipelines) would introduce additional dependencies, complicate the deployment model, and create maintenance burden for target repositories.

## Decision

Do not depend on external build, CI/CD, or continuous integration tooling for the workflow package:

- The package is self-contained text configuration and agent prompts.
- The Python sync CLI is a lightweight development tool, not a build dependency for target repositories.
- No CI/CD configuration files (`.github/workflows/`, `Jenkinsfile`, `.gitlab-ci.yml`) are included in the package.
- No Makefile or equivalent build automation is required for package use.
- Testing and verification are performed through the OpenCode workflow itself (verifier stage, review helpers), not through external CI pipelines.

Target repositories may add their own CI/CD around the workflow, but that is an operator responsibility, not a package requirement.

## Alternatives Considered

- **GitHub Actions CI**: Add workflow validation and test automation — couples the package to a specific CI provider; adds configuration burden for target repos.
- **Makefile build**: Add Make targets for common operations — useful for maintainers but not required for consumers of the package.
- **Including CI config as optional**: Provide sample configurations — risks becoming de facto requirements and adds maintenance overhead.

## Consequences

**Positive:**
- Zero external build dependencies for consumers.
- Simpler deployment: copy files into a target repository.
- The package is runtime-platform-agnostic (no CI provider lock-in).
- All workflow behavior is documented in inspectable markdown, not hidden in CI scripts.

**Negative:**
- No automated CI checks for the package itself — testing relies on manual or workflow-internal verification.
- Maintainers must manually validate changes to agent prompts and workflow policies.
- The Python sync CLI has its own unit tests, but no CI runs them automatically.

## Affected Artifacts

- `pyproject.toml` — Package definition (Python dependencies only)
- `system_definition/pbs/02-architecture/architecture.md` — Boundaries section
- `system_definition/pbs/03-implementation/implementation.md` — Mechanism storage rules
- `system_definition/cross-cutting/05-operation/deployment-process.md` — Deployment requirements (no CI dependency)

## Verification

No CI/CD configuration files exist in the package repository. The package README does not reference external build tooling setup steps. The package can be inspected and used with only `opencode.json` and `.opencode/` in a target repository.

## Review Trigger

When the Python sync CLI or agent prompt testing becomes complex enough to warrant automated CI, revisit this decision and evaluate lightweight CI options that are optional for target repositories.