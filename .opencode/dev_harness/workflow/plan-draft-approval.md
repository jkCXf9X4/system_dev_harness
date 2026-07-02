# Plan Draft Approval

Purpose: Defines when a plan draft needs operator approval before builder execution.

For `workflow_mode: delivery`, the planner emits a draft work order before builder execution.

Planner output uses:

```text
plan_approval_status: not_required|pending
plan_approval_reason: large_job|destructive|operator_requested|not_applicable
```

Use `plan_approval_status: pending` when builder execution must wait for operator approval. Required approval triggers include:

- `large_job_triggered: true`
- destructive or high-blast-radius changes
- explicit user requests to review or approve the plan before implementation

Use `plan_approval_status: not_required` for routine low-risk delivery work. Candidate-capture work does not require plan draft approval unless the workflow is explicitly extended.

Operator decisions route as follows:

- `approve`: orchestrator-router forwards the approved planner work order to builder.
- `revise`: orchestrator-router calls planner again with the user's requested revision and prior planner output.
- `reject`: orchestrator-router stops before builder execution and reports the rejection rationale.

Operator decisions are routing inputs, not `plan_approval_status` values.

Large-job approval is one trigger for this draft approval cycle; do not route large jobs through a separate approval path.

