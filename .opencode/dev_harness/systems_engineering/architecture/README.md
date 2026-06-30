# Architecture Artifacts — Relocated

The runtime reference copies formerly in this directory were pruned to reduce
agent context-window consumption. All four files were traceability/documentation
artifacts whose content is already encoded in agent prompts and workflow policies.

## Canonical Sources

| Artifact | Canonical Location |
|---|---|
| Interface contracts (handoff payloads) | `system_definition/pbs/02-architecture/interface-contracts.md` |
| Agent state machines | `system_definition/pbs/02-architecture/agent-state-machines.md` |
| Sequence diagrams & parametric constraints | `system_definition/pbs/02-architecture/sequence-parametric.md` |
| Component hierarchy (PBS/FBS/WBS) | `system_definition/breakdown-structures.md` |

For context-window budgeting guidance, see `.opencode/dev_harness/workflow/agent-boundaries.md`.

> **Note for target repos:** These canonical files are available only in the source repository.
> Target repos receive `.opencode/` only and do not include `system_definition/`.
> Orchestration agents derive equivalent structural data from `.opencode/agents/` prompts
> and `.opencode/dev_harness/workflow/` policies at runtime.