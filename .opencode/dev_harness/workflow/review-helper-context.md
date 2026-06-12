# Review Helper Caller Context

Use this protocol when a builder or reviewer invokes a read-only review helper.

Apply `.opencode/dev_harness/workflow/subagent-lifecycle.md` before sending follow-up review work to an existing helper. If the review input can be summarized clearly, prefer a fresh helper context with `caller_context` and a compact handoff over accumulated helper history.

The invoking stage must include one caller context:

```text
caller_context: builder_preflight|reviewer_gate
```

## Contexts

`builder_preflight` means the helper is being invoked by `orchestrator-builder` before final builder handoff.

- Return findings as implementation evidence and local fix guidance only.
- Do not return or imply `approved`, `blocked`, or `waiver_required`.
- A helper `pass`, `fail`, or `needs_waiver` result is scoped to this helper check only. It is not a completion-gate decision.

`reviewer_gate` means the helper is being invoked by `orchestrator-reviewer` as part of the formal completion gate.

- Return findings as reviewer-gate input.
- Findings may inform the reviewer decision: `approved`, `blocked`, or `waiver_required`.

## Required Output Fields

Every read-only review helper that receives a caller context must include:

```text
caller_context: builder_preflight|reviewer_gate|not_provided
decision_scope: helper_findings_only|reviewer_gate_input
```

Use `decision_scope: helper_findings_only` for `builder_preflight`.
Use `decision_scope: reviewer_gate_input` for `reviewer_gate`.
Use `caller_context: not_provided` only when the invoking stage omitted the context; report that omission as a finding when the task depends on distinguishing builder preflight from reviewer gate.
