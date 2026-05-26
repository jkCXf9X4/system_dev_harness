# IMD-003: Use Repo-Local Workflow Memory For Durable Lessons

## Status

Accepted

## Context

The workflow needs durable lessons, reusable patterns, and decision pointers to survive dev-harness refreshes without being overwritten by copied payload updates. If the memory lives only inside the copied `.opencode/dev_harness/` tree, a later sync can replace it or reintroduce stale references.

## Decision

Keep durable workflow memory in `.opencode/dev_harness_memories/` rather than in the copied dev-harness tree. Use separate files for lessons, reusable patterns, and decision pointers so the repo-local memory can evolve independently of copied runtime policy.

The copied `workflow/` tree remains the policy source for guarded workflow control, information hygiene, and review output. Repo-local memory is intentionally not copied from the dev harness package.

## Consequences

Benefits:

- repo-local memory is insulated from dev-harness refreshes
- copied runtime policy stays small and stable
- lessons, patterns, and decision pointers can be curated independently
- update diffs remain easier to inspect because policy and memory are separated

Tradeoffs:

- the repository now has two related runtime document roots to keep aligned
- agents must know which artifacts are copied policy and which are local memory

## Traceability

- Product commitments: PC-003, PC-006, PC-007
- Use cases: UC-004, UC-009
