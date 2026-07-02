# Handoff Boundary

Purpose: Defines constraints for external or manual implementation handoffs.

External or manual handoff is non-executing guidance unless the orchestrator explicitly uses it as builder-stage input.

Any external or manual implementation must produce builder-equivalent evidence and still pass reviewer-coordinated verification, independent reviews, completion gate, and final reporting.

A handoff cannot authorize scope expansion, skipped checks, direct approval, or waived failures.

## File-Based Handoff Methodology

The file-based handoff methodology is the standard for all agent-to-agent handoffs within the guarded workflow.

### Rules

1. **Minimal inline fields**: Only `task_id`, `task_file_path`, `plan_file_path`, `status`, and `key_evidence` are passed inline between agents.
2. **Full context on disk**: Each stage writes its complete output to a handoff file before returning.
3. **Pre-consumption integrity check**: Every stage must verify file existence and non-emptiness before loading a handoff file.
4. **Schema versioning**: Every handoff file includes `schema_version` for version-aware validation.
5. **Handoff file location**: Files are stored under `.opencode/dev_harness_handoffs/` with the naming convention `<timestamp>-<task_id>-<stage>.md`.

### Exceptions

The initial Router-to-Planner handoff may pass the raw user request inline since there is no prior handoff file to reference. All other handoffs must use the file-based methodology.

## Task Tracking in Handoffs

Every agent-to-agent handoff must include the `task_file_path` field so downstream stages can load the task tracking file for full lifecycle context.

### Handoff Inline Fields (Updated)

Every agent-to-agent handoff passes these fields inline:

```text
task_id: <unique task identifier>
task_file_path: <path to task tracking file, or none for initial router handoff>
plan_file_path: <path to plan file on disk, or none>
status: <current stage status>
key_evidence: <brief summary, ≤200 tokens>
```

### Task Tracking File Lifecycle

1. **Router** creates the task tracking file at `.opencode/dev_harness_tasks/<timestamp>-<task-id>.md` before routing to planner.
2. **Each stage** updates the task tracking file after completing its work, appending its stage record.
3. **Reporter** finalizes the task tracking file with the final outcome.

The task tracking file is the authoritative cross-stage lifecycle record. Every stage should update it before returning control to the router.
