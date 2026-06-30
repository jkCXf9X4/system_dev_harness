# Deployment Product Requirements

This artifact captures the product-level deployment model. Runnable copy and refresh steps live in [docs/install-and-deploy.md](../../docs/install-and-deploy.md).

## Requirements

- The package must remain deployable by copying only `opencode.json` and `.opencode/` into a target development repository.
- The package `system_definition/` tree must remain source documentation for this repository and must not be required at runtime in target repositories.
- The copied payload must include the agent prompts, workflow policy, reusable prompt templates, system-definition guidance for agents, and package-local runtime dependency metadata needed by OpenCode.
- Target repositories must be able to refresh the workflow payload from a newer package commit without overwriting repo-local workflow memory under `.opencode/dev_harness_memories/`.
- Deployment updates should be reviewable as ordinary repository diffs in the target repository.

## Product Boundaries

- The package does not provide a registry, installer, or release server.
- The package does not manage target-repository source control operations.
- The package does not copy this repository's `system_definition/` tree into target repositories.

## Trace Links

- Operator-facing deployment steps: [docs/install-and-deploy.md](../../docs/install-and-deploy.md)
- Runtime artifact map: [system_definition/pbs/03-implementation/implementation.md](../../pbs/03-implementation/implementation.md)
- Repo-local memory decision: [IMD-003](../03-implementation/decisions/IMD-003-use-repo-local-workflow-memory.md)
