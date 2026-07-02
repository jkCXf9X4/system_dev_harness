# Task Tracking Archive

This directory stores standardized task tracking files for every task processed by the guarded orchestrator workflow.

## Purpose

- Creates a continuous, stage-by-stage traceability record for every task from inception through completion.
- Enables any agent or operator to inspect the full lifecycle of a task — routing decisions, planning scope, implementation evidence, review findings, reflection outcomes, and final report — from a single file.
- Provides a queryable task-history trail for pattern discovery, regression analysis, and cross-task traceability.
- Extends beyond plan-only tracking to cover all workflow stages and all agents.

## Ownership

- The **router** creates the task tracking file when it first routes a task to the planner.
- Every stage updates the task tracking file after completing its work, appending its stage record.
- The **reporter** finalizes the task tracking file with the final outcome and closes the record.
- The **task-tracker helper** (`orchestrator-task-tracker`) handles all file writes for task tracking updates.

## Naming Convention

Each task tracking file follows this naming convention:

```
YYYY-MM-DD_HHMMSS-<task-id>.md
```

- `YYYY-MM-DD` — the date the task was created (ISO-8601 date)
- `HHMMSS` — the time the task was created (24-hour local time)
- `<task-id>` — the task identifier assigned by the planner (e.g., `IMP-008`, `IMP-009-impl`)

Example: `2026-07-02_120000-IMP-061.md`

## Retention

This directory is **volatile** content. Task tracking files are:

- **NOT tracked in git** (see `.opencode/.gitignore`).
- Subject to ad-hoc cleanup to prevent unbounded growth.
- Useful as a local historical reference but not a durable record outside the working copy.

The tracked bootstrap files in this directory are `.gitkeep` and `README.md`; they ensure the directory exists on fresh clones and document the archive contract.

## Standardized Schema

Every task tracking file follows the schema defined in `.opencode/dev_harness/workflow/task-summary-schema.md`.

## Source Of Truth

The stage handoff files under `.opencode/dev_harness_handoffs/` are the authoritative source for each stage's detailed output. Task tracking files are a structured extraction and lifecycle summary for cross-stage traceability. If a discrepancy exists between a handoff file and the task tracking file, the handoff file takes precedence.
