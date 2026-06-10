# Plan Summary Schema

Use this schema for planner work-order summary headers and `.opencode/dev_harness_plans/` archive files.

## Required Fields

| Field | Description |
|---|---|
| `task_id` | Unique task identifier from the planner or derived from the improvement candidate ID |
| `timestamp` | ISO-8601 timestamp of plan creation |
| `scope` | One-paragraph scope statement |
| `files_touched` | List of file paths with reasons for each change |
| `risk_assessment` | Blast-radius category (`local`, `cross-module`, or `destructive`) plus file count and estimated impact |
| `candidate_linkages` | Improvement candidate IDs linked to this task, or `none` |
| `large_job_triggered` | `true` when the planner classifies the task as a larger job, otherwise `false` |
| `plan_approval_status` | `not_required` or `pending` |
| `plan_approval_reason` | `large_job`, `destructive`, `operator_requested`, or `not_applicable` |
