# Task Summary Schema

Use this schema for task tracking files under `.opencode/dev_harness_tasks/`. Every stage updates the task tracking file after completing its work.

`schema_version: v1` establishes the initial version for version-aware downstream validation.

## Emit-By-Exception Rule

Conditionally-required fields follow the emit-by-exception rule from `.opencode/dev_harness/workflow/stage-output-schema.md`: they are silent (omitted) when their trigger condition is not met. Only emit a conditionally-required field when it carries substantive content triggered by the condition.

## Required Fields (always present)

| Field | Description |
|---|---|
| `schema_version` | Schema version string (`v1` or later) — first field |
| `task_id` | Unique task identifier from the planner or derived from the improvement candidate ID |
| `timestamp` | ISO-8601 timestamp of task creation (set by router) |
| `task_status` | Current lifecycle status: `routed` | `planned` | `building` | `reviewing` | `reflecting` | `reporting` | `completed` | `blocked` | `cancelled` |
| `issue_kind` | `bug`, `fix`, `regression`, `feature`, `docs`, `cleanup`, `refactor`, `tuning`, `architecture`, `workflow`, `review`, or `other` |
| `workflow_mode` | `delivery` or `candidate_capture` |
| `route` | Routing path taken: `guarded_chain` |
| `stage_records` | Ordered list of stage records (see below) |

## Stage Record Schema

Each entry in `stage_records` captures one stage's contribution to the task lifecycle:

| Field | Description |
|---|---|
| `stage` | Stage name: `router` | `planner` | `builder` | `reviewer` | `reflection` | `reporter` |
| `status` | Stage-specific status (see per-stage below) |
| `timestamp` | ISO-8601 timestamp when the stage completed |
| `handoff_file` | Path to the handoff file written by this stage, or `none` |
| `key_evidence` | Brief summary of the stage outcome (≤200 tokens) |

### Router Stage Record

| Field | Description |
|---|---|
| `stage` | `router` |
| `status` | `routed_to_planner` | `clarification_needed` | `routed_to_builder` | `blocked` |
| `timestamp` | ISO-8601 timestamp |
| `handoff_file` | `none` (router does not write a handoff file for initial routing) |
| `key_evidence` | Routing decision summary |
| `clarification_status` | `not_needed` | `required` | `resolved` — only emit when clarification was involved |
| `clarification_questions` | Questions asked, or `none` — only emit when `clarification_status` is `required` or `resolved` |

### Planner Stage Record

| Field | Description |
|---|---|
| `stage` | `planner` |
| `status` | `planned` | `revision_planned` | `blocked` |
| `timestamp` | ISO-8601 timestamp |
| `handoff_file` | Path to the planner handoff file |
| `key_evidence` | Planning outcome summary |
| `plan_file_path` | Path to the plan summary file |
| `plan_approval_status` | `not_required` | `pending` | `approved` |
| `revision_count` | Revision iteration number — only emit when `revision` is active |
| `helper_agents_used` | List of helpers invoked, or `none` |
| `helper_agents_waived` | List of helpers waived, or `none` |

### Builder Stage Record

| Field | Description |
|---|---|
| `stage` | `builder` |
| `status` | `implemented` | `persisted` | `no_candidate` | `blocked` |
| `timestamp` | ISO-8601 timestamp |
| `handoff_file` | Path to the builder handoff file |
| `key_evidence` | Implementation outcome summary |
| `files_changed` | List of files modified, created, or deleted — only emit when `workflow_mode` is `delivery` |
| `candidate_disposition` | `persisted` with candidate IDs, or `no_candidate` with rationale — only emit when `workflow_mode` is `candidate_capture` |
| `helper_agents_used` | List of helpers invoked, or `none` |
| `cleanup_performed` | Summary of cleanup actions, or `none` |

### Reviewer Stage Record

| Field | Description |
|---|---|
| `stage` | `reviewer` |
| `status` | `approved` | `blocked` | `waiver_required` | `blocked_max_reached` |
| `timestamp` | ISO-8601 timestamp |
| `handoff_file` | Path to the reviewer handoff file |
| `key_evidence` | Gate decision summary |
| `blocking_gaps` | List of blocking gap IDs and descriptions — only emit when `blocked` or `blocked_max_reached` |
| `waiver_rationale` | Waiver rationale — only emit when `waiver_required` |
| `plan_file_verification` | `pass` | `fail` | `not_applicable` |
| `helper_agents_used` | List of helpers invoked, or `none` |
| `memory_candidates` | Memory candidates identified, or `none` |

### Reflection Stage Record

| Field | Description |
|---|---|
| `stage` | `reflection` |
| `status` | `memory_written` | `memory_rejected` | `needs_more_evidence` | `no_memory_action` |
| `timestamp` | ISO-8601 timestamp |
| `handoff_file` | Path to the reflection handoff file |
| `key_evidence` | Reflection outcome summary |
| `memory_ids_written` | Memory entry IDs written or updated, or `none` |
| `memory_candidates_evaluated` | List of candidates evaluated, or `none` |
| `improvement_candidates` | Improvement candidates raised, or `none` |

### Reporter Stage Record

| Field | Description |
|---|---|
| `stage` | `reporter` |
| `status` | `reported` | `blocked` |
| `timestamp` | ISO-8601 timestamp |
| `handoff_file` | Path to the reporter handoff file |
| `key_evidence` | Final outcome summary |
| `final_status` | `completed` | `completed_with_waivers` | `blocked` | `cancelled` |
| `next_required_action` | What the operator should do next, or `none` |

## Task Tracking File Lifecycle

1. **Router creates** the task tracking file with `task_status: routed` and the router stage record.
2. **Planner updates** the file with `task_status: planned` and the planner stage record.
3. **Builder updates** the file with `task_status: building` (or `reviewing` if builder completes) and the builder stage record.
4. **Reviewer updates** the file with `task_status: reviewing` (or `reflecting` if approved) and the reviewer stage record.
5. **Reflection updates** the file with `task_status: reflecting` (or `reporting` if done) and the reflection stage record.
6. **Reporter finalizes** the file with `task_status: completed` (or `blocked`/`cancelled`) and the reporter stage record.

## Task Tracking File Consumption

Any stage may load the task tracking file to understand the full lifecycle context of the current task:
- **Router**: Creates and initializes the file; reads it on revision loops to preserve iteration history.
- **Planner**: Reads prior stage records for revision context; appends its own record.
- **Builder**: Reads planner and router records for full context; appends its own record.
- **Reviewer**: Reads all prior records for gate assessment; appends its own record.
- **Reflection**: Reads all prior records for memory triage; appends its own record.
- **Reporter**: Reads all prior records for final report synthesis; finalizes the file.
