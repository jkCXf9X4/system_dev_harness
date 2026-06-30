# OD-002: Repo-Local Workflow Memory

## Status

Accepted

## Layer

Operation

## Context

The guarded orchestrator workflow produces durable lessons, reusable patterns, and decision pointers from each completed run. These artifacts should survive across runs and across repositories to avoid repeating mistakes and to capture emerging best practices. However, each target repository has its own domain context, tooling choices, and team conventions, so workflow memory must be repo-local rather than shared across the entire package user base.

## Decision

Store workflow memory as **repo-local versioned markdown** under `.opencode/dev_harness_memories/` in each target repository:

- Workflow memory files are plain markdown with YAML frontmatter for trust metadata, version, and revalidation cues.
- The memory helper (`orchestrator-memory`) retrieves task-relevant memory entries from this directory (read-only).
- The memory curator (`orchestrator-memory-curator`) may edit only workflow memory files and only for evidenced durable memory candidates.
- The reflection stage (`orchestrator-reflection`) owns final memory-incorporation triage before reporting.
- Repository-local memory is not synced across repositories; each target builds its own memory base.

The package repository maintains its own `.opencode/dev_harness_memories/` with initial canonical entries that serve as a starting point for new targets.

## Alternatives Considered

- **Global shared memory**: A single memory store across all repositories — loses repo-specific context; risk of conflicting conventions.
- **No persistent memory**: Each run starts fresh — loses accumulated lessons and patterns across runs.
- **Database-backed memory**: External storage — adds infrastructure dependency and sync complexity.
- **In-memory only during run**: Survives only the current conversation — no cross-run learning.

## Consequences

**Positive:**
- Each repository builds its own relevant memory base.
- Plain markdown is inspectable, version-controlled, and portable.
- Trust metadata supports revalidation and aging of memory entries.
- Clear ownership: reflection triages, curator persists.

**Negative:**
- Memory is not shared across repositories — each target must build its own base.
- Revalidation relies on agent discipline rather than automatic triggers.
- Memory files can grow without an automated pruning mechanism.

## Affected Artifacts

- `.opencode/dev_harness_memories/` — Repository-local memory directory
- `.opencode/dev_harness_memories/lessons.md` — Persistent lesson memory
- `.opencode/dev_harness_memories/patterns.md` — Reusable patterns
- `.opencode/dev_harness_memories/README.md` — Memory schema and rules
- `.opencode/agents/orchestrator-memory.md` — Memory helper (read-only)
- `.opencode/agents/orchestrator-memory-curator.md` — Memory curator (limited write)
- `.opencode/agents/orchestrator-reflection.md` — Reflection stage
- `system_definition/pbs/03-implementation/implementation.md` — Mechanism storage rules

## Verification

A new target repository initialized with the sync tool has a `.opencode/dev_harness_memories/` directory with initial entries. The memory helper can retrieve entries by domain keyword. The memory curator can edit only allowed files.

## Review Trigger

When `.opencode/dev_harness_memories/` grows beyond 100 entries, or when memory retrieval becomes noticeably slow on LLM context load, consider adding a pruning or archiving mechanism.