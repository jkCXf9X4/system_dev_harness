# Plans Archive

This directory stores standardized plan summaries for every implementation task processed by the guarded orchestrator workflow.

## Purpose

- Creates a local, searchable task-history trail for pattern discovery, regression analysis, and cross-task traceability.
- Provides a queryable record of scope, risk, large-job status, and candidate linkages across all implemented tasks.
- Supports lightweight archive-integrity checks for the current run without turning the plan archive into an implementation artifact.

## Ownership

- The **planner** writes the complete plan summary file during the planning stage.
- The **planner** owns the `large_job_triggered` decision and writes it into the plan file.
- The **builder** does not write or modify plan files.

## Naming Convention

Each plan summary file follows this naming convention:

```
YYYY-MM-DD_HHMMSS-<task-id>.md
```

- `YYYY-MM-DD` — the date the plan was written (ISO-8601 date)
- `HHMMSS` — the time the plan was written (24-hour local time)
- `<task-id>` — the task identifier assigned by the planner (e.g., `IMP-008`, `IMP-009-impl`)

Example: `2026-06-10_143022-IMP-008-009.md`

## Retention

This directory is **volatile** content. Plan files are:

- **NOT tracked in git** (see `.opencode/.gitignore`).
- Subject to ad-hoc cleanup to prevent unbounded growth.
- Useful as a local historical reference but not a durable record outside the working copy.

The tracked bootstrap files in this directory are `.gitkeep` and `README.md`; they ensure the directory exists on fresh clones and document the archive contract.

## Standardized Summary Fields

Every plan summary file contains the following fields:

| Field | Description |
|---|---|
| `task_id` | Unique task identifier from the planner or derived |
| `timestamp` | ISO-8601 timestamp of plan creation |
| `scope` | One-paragraph scope statement |
| `files_touched` | List of file paths with reasons for each |
| `risk_assessment` | Blast-radius category (local, cross-module, destructive) + file count + estimated impact |
| `candidate_linkages` | Improvement candidate IDs linked to this task, or `none` |
| `large_job_triggered` | Planner decision: `true` or `false` |

## Source Of Truth

The planner work order is the authoritative source. Plan summary files are a structured extraction for archival purposes. If a discrepancy exists between the planner work order and the plan summary, the planner work order takes precedence.
