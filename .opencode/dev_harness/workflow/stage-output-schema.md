# Stage Output Schema

Use this schema for every top-level stage and directed helper. Role prompts may add role-specific fields, but they should not redefine these common fields.

## Common Fields

```text
user_feedback_required: true|false
user_feedback_request: <specific question, waiver request, or not_applicable>
improvement_candidates: <out-of-scope candidates or none>
research_requests: <research already performed or needed, or none>
```

When `user_feedback_required` is true, the orchestrator pauses and requests the user decision before continuing.

Improvement candidates are backlog candidates only. They do not authorize scope expansion in the current task. Incidental candidate handling and persistence ownership live in `.opencode/dev_harness/workflow/candidate-capture.md`.

Research requests are handled by `orchestrator-researcher` when source material is needed for the current stage.

## Not Applicable

If a stage is not applicable, it must return:

```text
not_applicable
reason: <brief rationale>
evidence_inputs_inspected: <inputs reviewed before declaring not applicable>
```

Missing stage output or unjustified `not_applicable` blocks completion.

## Clarification Fields

Planner clarification output uses:

```text
clarification_status: not_needed|required
blocking_uncertainty: <decision that cannot be made safely, or none>
clarification_questions: <one to three specific questions, or none>
assumption_rationale: <why assumptions are safe, or not_applicable>
```
