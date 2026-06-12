# Stage Output Schema

Use this schema for every top-level stage and directed helper. Role prompts may add role-specific fields, but they should not redefine these common fields.

## Common Fields

```text
user_feedback_required: true|false
user_feedback_request: <specific question, waiver request, or not_applicable>
improvement_candidates: <out-of-scope candidates or none>
research_requests: <research already performed or needed, or none>
helper_lifecycle: <reuse/start-fresh decision for helper follow-up, or not_applicable>
```

Any stage may set `user_feedback_required: true` when it needs user input, approval, or a waiver.

When `user_feedback_required` is true, the orchestrator pauses and requests the user decision before continuing. The unresolved `user_feedback_request` must be relayed unchanged to downstream stages after the user responds so every agent sees the same active feedback context.

Improvement candidates are backlog candidates only. They do not authorize scope expansion in the current task. Incidental candidate handling and persistence ownership live in `.opencode/dev_harness/workflow/candidate-capture.md`.

Research requests are handled by `orchestrator-researcher` when source material is needed for the current stage.

Helper lifecycle decisions use `.opencode/dev_harness/workflow/subagent-lifecycle.md`. They make helper reuse explicit because the workflow cannot force compaction, clearing, pruning, or reset of another agent's context.

When a stage invokes helpers after previous helper work, include:

```text
helper_lifecycle:
  reuse_decision: reuse_existing|start_fresh|not_applicable
  reason: <why reuse or a fresh helper is appropriate>
  prior_context_dependency: none|low|medium|high
  context_rot_risk: low|medium|high
  handoff_summary: <compact handoff summary when start_fresh, or not_applicable>
```

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
