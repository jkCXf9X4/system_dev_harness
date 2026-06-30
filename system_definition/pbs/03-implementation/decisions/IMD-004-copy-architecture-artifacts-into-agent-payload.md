# IMD-004: Copy Architecture Artifacts Into Agent Payload

## Status

Accepted

## Context

IMP-032 added agent prompt references to architecture artifacts (`interface-contracts.md`, `agent-state-machines.md`, `sequence-parametric.md`) and verification artifacts (`acceptance-criteria.md`) under `system_definition/`. These paths resolve in the source repository but not in target repositories, which receive `.opencode/` but not `system_definition/`.

IMD-002 established `.opencode/dev_harness/systems_engineering/` as the runtime agent context directory. Architecture and verification artifacts that agents load at runtime must follow the same pattern.

## Decision

Copy architecture and verification artifacts that are directly referenced by agent prompt files into `.opencode/dev_harness/systems_engineering/architecture/` and `.opencode/dev_harness/systems_engineering/verification/` as runtime reference copies. Each copy includes a header note identifying its canonical source in `system_definition/`.

Adapt internal cross-references in the runtime copies:
- References to co-located copied files remain relative.
- References to files outside the copy set use workspace-relative paths pointing to the canonical source.

Agent prompt files reference the `.opencode/` runtime copies, not the canonical `system_definition/` sources.

## Consequences

**Benefits:**
- Target-repo agents can resolve architecture and verification artifact references from the shipped `.opencode/` payload.
- Canonical system-definition artifacts remain the design and traceability source of truth.
- The pattern is consistent with IMD-002's runtime-copy approach.

**Tradeoffs:**
- Runtime copies must be kept synchronized with canonical sources when architecture evolves.
- New architecture artifacts referenced by agents require the same copy-and-adapt treatment.
- The `architecture/` and `verification/` subdirectories add a structural mirror of the system-definition layer model.

## Affected Artifacts

- `.opencode/agents/orchestrator-planner.md`
- `.opencode/agents/orchestrator-reviewer.md`
- `.opencode/agents/orchestrator-systems-engineering.md`
- `.opencode/dev_harness/systems_engineering/architecture/`
- `.opencode/dev_harness/systems_engineering/verification/`

## Traceability

- Product commitments: PC-006, PC-007
- Architecture: copied runtime reference in `.opencode/dev_harness/systems_engineering/architecture/`
- Implementation: this decision record
- Predecessor: IMD-002