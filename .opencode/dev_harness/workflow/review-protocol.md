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

# Review Output Protocol

Use this protocol for independent review stages.

Return exactly one status:

```text
pass
fail
needs_waiver
```

Include:

- caller context and decision scope from the Caller Context section above when the helper was invoked with `caller_context`
- findings with stable item ids
- brief evidence for each finding
- waiver request details when status is `needs_waiver`
- when memory is relevant, memory hygiene input evidence covering retrieved entries, revalidation status, stale or conflicting memory, new memory candidates for reflection, and whether memory influenced the review outcome

Use `fail` when evidence is missing, contradictory, or does not prove completion. Use `needs_waiver` only when the implementation is intentionally incomplete or risky and requires explicit user approval under `.opencode/dev_harness/workflow/waivers.md`.