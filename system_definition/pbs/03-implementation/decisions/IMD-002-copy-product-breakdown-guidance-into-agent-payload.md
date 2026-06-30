# IMD-002: Copy System Definition Guidance Into Agent Payload

## Status

Accepted

## Context

Only `opencode.json` and `.opencode/` are copied into target development repositories. Package documentation under `system_definition/` remains in this source repository. Product breakdown guidance therefore cannot live only in `system_definition/` if target-repo agents are expected to use it.

The guidance also needs to stay small enough for agents to load selectively. A single large document would make routine breakdown, decision, and traceability tasks carry unnecessary context.

## Decision

Store reusable product breakdown guidance under `.opencode/dev_harness/systems_engineering/` and split it into load-on-demand files:

- an entry README with the structure overview
- one file per breakdown layer
- separate decision placement, decision log, traceability, naming, and reusable template files
- decision, decision-log-entry, improvement-overview, and improvement-candidate templates under `.opencode/dev_harness/systems_engineering/templates/`

Keep source docs updated to describe this copied agent context, but treat `.opencode/dev_harness/systems_engineering/` as the runtime source available to agents in target repositories.

## Consequences

Benefits:

- target-repo agents receive the product breakdown guidance automatically with the copied payload
- agents can load only the relevant layer or support file
- distributed decisions remain close to affected artifacts while the global decision log stays an index
- improvement backlog templates live in the evolution/system-definition context instead of a separate generic `others` bucket
- source docs stay aligned with the copied runtime payload

Tradeoffs:

- guidance duplicated conceptually between source docs and copied templates must be kept synchronized
- changes to the product breakdown model must update both implementation mapping and package-level traceability

## Traceability

- Product commitments: PC-006, PC-007
- Architecture: copied runtime source of truth in `.opencode/`
- Implementation: `.opencode/dev_harness/systems_engineering/`
