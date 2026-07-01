# Plan Summary Schema

Use this schema for planner work-order summary headers and `.opencode/dev_harness_plans/` archive files.

`schema_version: v2` enables version-aware field validation by downstream agents (see reviewer pfv-002 check).

## Emit-By-Exception Rule

Conditionally-required fields follow the emit-by-exception rule from `.opencode/dev_harness/workflow/stage-output-schema.md`: they are silent (omitted) when their trigger condition is not met. Only emit a conditionally-required field when it carries substantive content triggered by the condition.

## Required Fields (always present)

| Field | Description |
|---|---|
| `schema_version` | Schema version string (`v2` or later) — first field, establishes versioning convention for pfv-002 checking |
| `task_id` | Unique task identifier from the planner or derived from the improvement candidate ID |
| `timestamp` | ISO-8601 timestamp of plan creation |
| `scope` | One-paragraph scope statement |
| `files_touched` | List of file paths with reasons for each change |
| `risk_assessment` | Blast-radius category (`local`, `cross-module`, or `destructive`) plus file count and estimated impact |
| `candidate_linkages` | Improvement candidate IDs linked to this task, or `none` |
| `large_job_triggered` | `true` when the planner classifies the task as a larger job, otherwise `false` |
| `plan_approval_status` | `not_required` or `pending` |
| `plan_approval_reason` | `large_job`, `destructive`, `operator_requested`, or `not_applicable` |
| `tailoring_record` | Selected workflow profile plus applied triggers, helper/stage deviations, and rationale for task-specific tailoring |
| `success_criteria` | Verification obligations consumed by builder, reflection, and reporter — measurable conditions that determine task completion |
| `workflow_mode` | `delivery` or `candidate_capture` — controls whether the builder implements changes or persists improvement backlog artifacts |
| `issue_kind` | `bug`, `fix`, `regression`, `feature`, `docs`, `cleanup`, `refactor`, `tuning`, `architecture`, `workflow`, `review`, or `other` — categorizes the work for downstream routing decisions |
| `control_flags` | Block containing `touches_information_artifacts`, `touches_product_breakdown`, `requires_decision_record`, `requires_external_research`, `touches_shared_interface` — always set by planner |

## Conditionally Required Fields

Conditionally-required fields are emitted only when their trigger condition is met. See "Emit-By-Exception Rule" above.

| Field | Condition | Reason |
|---|---|---|
| `helper_outputs_summary` | When any planner helper was invoked | Consumed by builder to understand helper decisions, constraints, and action items without loading raw helper output |
| `staged_plan` | When `large_job_triggered` is `true` or `files_touched` > 1 | Consumed by builder, reviewer, and reporter — minimum staged implementation plan ensures traceable step-by-step execution |
| `interface_impact_statement` | When `touches_shared_interface` is `true` | Per `.opencode/dev_harness/workflow/interface-consistency.md` — lists touched surfaces and known consumer files |
| `primary_layer` / `downstream_layers` | When `touches_product_breakdown` is `true` | System-definition layer placement consumed by builder and reviewer for product-breakdown work |
| `revision` / `revision_count` | When operating in revision mode | Iteration context consumed by planner (revision input) and builder (scope refinement) |
| `risk_triggers_detected` | When any risk trigger fired | Documents triggers that informed helper selection — consumed by reviewer for gate assessment |
| `major_risks_and_open_questions` | When `risk_assessment` is `cross-module` or `destructive` | Risks affecting downstream decisions — consumed by builder, reviewer, and reporter |
| `assumptions_and_interpretation_choices` | When planner proceeded with assumptions under clarification gate | Consumed by validation VAL-003 and reflection for intent-to-outcome traceability |
| `clarification_status` | When `blocking_uncertainty` was present | Records whether user intent was clarified or assumed — consumed by reviewer and reflection |
| `workflow_memory_entries_applied` | When workflow memory entries were retrieved and applied during planning | Lists memory entry IDs and their influence — consumed by reflection for memory-incorporation decisions |