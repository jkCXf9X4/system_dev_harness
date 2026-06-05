# Workflow Memory

Use this policy when a stage needs task-relevant workflow memory or final memory-incorporation triage.

## Retrieval

Any owning stage may request task-relevant workflow memory from `orchestrator-memory` when lessons, reusable patterns, or decision pointers could reduce repeated work or review misses.

The reviewer may identify memory candidates and stale or conflicting memory evidence, but does not own final memory incorporation. The reflection stage owns final memory-incorporation triage for completed workflows and may invoke `orchestrator-memory-curator` when evidenced findings reveal a durable lesson, reusable pattern, or decision pointer worth evaluating for memory.

Curation is workflow memory capture only; it does not authorize scope expansion, current-task implementation, direct approval, or improvement backlog persistence.

Workflow memory lives under `.opencode/dev_harness_memories/`. Current task state, temporary investigation notes, implementation evidence, backlog candidates, and broad run history do not belong in memory.

Use this destination matrix when deciding what memory should contain:

- stable fact or decision pointer -> memory entry
- repeated failure or prevention rule -> lesson
- reusable operating procedure -> pattern
- broad future work -> improvement candidate
- one-off task evidence -> report or task history, not memory

## Curation Decisions

Memory curation returns one of the following decision taxonomies and should preserve trust metadata when it writes or updates an entry:

- `accepted: durable lesson`
- `accepted: reusable pattern`
- `accepted: decision pointer`
- `rejected: duplicate`
- `rejected: one-off or task-local`
- `rejected: vague or not actionable`
- `rejected: rediscoverable`
- `rejected: unsafe or untrusted content`
- `rejected: belongs in improvement backlog`
- `needs_more_evidence`

## Final Reflection

Every completed guarded workflow, including candidate capture, must run `orchestrator-reflection` before `orchestrator-reporter`.

Reflection owns final memory-incorporation triage. It reviews the completed run and returns one of:

```text
memory_written
memory_rejected
needs_more_evidence
no_memory_action
```

Reflection may invoke `orchestrator-memory-curator` only for evidenced repeatable findings that are task-independent and useful for future planning or review. When reflection exposes a separate backlog-worthy workflow problem, return it as `improvement_candidates`; do not persist it during reflection.

When memory is relevant, reflection owns the memory hygiene summary: retrieved entries, trust metadata, revalidation status, stale or conflicting memory, memory decisions made, and whether memory influenced approval, blocking, or waiver outcomes.

Reflection must not:

- override the reviewer gate
- treat backlog candidates as durable memory
- store current task state, implementation evidence, temporary investigation notes, or full transcripts as memory
- expand the current task scope

The reporter relays the reflection-owned memory hygiene summary and any memory IDs written, rejected candidates, missing-evidence rationale, or no-memory-action rationale. The reporter must not synthesize new memory decisions or invoke memory curation.
