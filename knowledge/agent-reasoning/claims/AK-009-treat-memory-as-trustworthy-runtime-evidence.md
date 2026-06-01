# AK-009: Treat Memory As Runtime-Verified Evidence

## Claim

Agent memory should not be trusted merely because it is persistent or retrieved as relevant. Memory should be treated as a hypothesis whose trust is re-established at use time through scope, freshness, provenance, and verification against the current environment.

## Practical Interpretation

Persistent memory entries should be compact, scoped, and reviewable. When a memory affects planning, implementation, verification, or user-facing behavior, the owning stage should check whether the entry is still valid before acting on it. Memory retrieval should prefer entries with clear source context, recent validation, precise scope, and explicit applicability.

## Applies To

- Memory helper
- Memory curator
- Lessons stage
- Lessons review
- Planner work order
- Reviewer gate
- Improvement workflow

## Evidence

- SRC-013 frames trustworthy memory as a harness-level bottleneck and distinguishes precision, durability, retrievability, and verifiability as memory quality axes.
- SRC-013 identifies "stale-but-confident" memory as a failure mode where relevant retrieved memory can be wrong after the environment changes.
- SRC-013 argues that trust should be re-established at retrieval time and paired with periodic verification against the live environment.
- SRC-005, SRC-009, and SRC-010 support separating prompt, planning, memory, and reusable procedures rather than treating all persistence as one prompt concern.

## Trace Targets

- `.opencode/dev_harness_memories/`
- `orchestrator-memory`
- `orchestrator-memory-curator`
- `orchestrator-lessons`
- `orchestrator-review-lessons`
- planner work-order memory fields
- reviewer evidence checks for memory-derived assumptions

## Limits

Runtime verification has a cost. Not every memory entry needs full revalidation on every task. The stricter check should apply when memory affects a durable decision, file path, tool choice, user preference, security-sensitive behavior, or task-critical assumption.
