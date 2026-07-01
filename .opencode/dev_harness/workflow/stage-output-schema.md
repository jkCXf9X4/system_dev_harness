# Stage Output Schema

Use this schema for every top-level stage and directed helper. Role prompts may add role-specific fields, but they should not redefine these common fields.

## Emit-By-Exception Rule

Optional fields are silent when they carry no meaningful value. Replace `none`/`not_applicable` with omission. Only emit a field when it has substantive content.

## Common Fields

```text
user_feedback_required: true|false    # only emit when true
user_feedback_request: <specific question, waiver request>  # omit when none
validation_status: pass|fail|not_applicable  # only emit when set by orchestrator-validation; other stages omit
improvement_candidates: <out-of-scope candidates>  # omit when none
research_requests: <research already performed or needed>  # omit when none
helper_lifecycle: <reuse/start-fresh decision>  # only emit when reusing a helper
```

Any stage may set `user_feedback_required: true` when it needs user input, approval, or a waiver.

When `user_feedback_required` is true, the orchestrator pauses and requests the user decision before continuing. The unresolved `user_feedback_request` must be relayed unchanged to downstream stages after the user responds so every agent sees the same active feedback context.

Improvement candidates are backlog candidates only. They do not authorize scope expansion in the current task. Incidental candidate handling and persistence ownership live in `.opencode/dev_harness/workflow/candidate-capture.md`.

Research requests are handled by `orchestrator-researcher` when source material is needed for the current stage.

Helper lifecycle decisions use `.opencode/dev_harness/workflow/subagent-lifecycle.md`. They make helper reuse explicit because the workflow cannot force compaction, clearing, pruning, or reset of another agent's context.

When a stage reuses a helper after previous helper work, include:

```text
helper_lifecycle:
  reuse_decision: reuse_existing|start_fresh
  reason: <why reuse or a fresh helper is appropriate>
```

Omit the entire `helper_lifecycle` block for first-call helpers or when no reuse decision is needed.

## Compact Output Format Example

For low-risk tasks, stages may use a compact output format:

```
status: <pass|fail|approved|blocked|...>
key_evidence: <brief summary>
findings: <stable item IDs or none>
```

All other fields are emitted only when they carry meaningful content. The compact format does not waive required evidence — it only reduces token overhead for fields that would otherwise be `none` or `not_applicable`.

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