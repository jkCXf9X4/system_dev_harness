# PD-003: Verification Before Completion Gating

## Status

Accepted

## Layer

Product

## Context

The guarded orchestrator workflow delivers changes through a multi-stage pipeline: planner normalizes the request, builder implements the change, and a deterministic gate computes approval. Before IMP-003, there was no explicit independent review stage — the builder's output was implicitly trusted if it passed basic checks. This created risks of incomplete implementation, unverified assumptions, and missed edge cases. The workflow needed a formal independent review gate to ensure every delivery change is verified before completion.

## Decision

Every guarded delivery run MUST pass through an independent reviewer stage before completion:

- The reviewer stage (orchestrator-reviewer) is the only completion gate authority.
- The reviewer coordinates focused verification (orchestrator-verifier) and independent review helpers (orchestrator-review-architecture, orchestrator-review-completeness, orchestrator-review-lessons) based on adaptive risk triggers.
- The gate produces one of three outcomes: `approved`, `blocked`, or `waiver_required`.
- Blocked findings route back to the planner for revision (revision loop, capped at 3 iterations).
- The reviewer is read-only — it never edits implementation files.
- In candidate-capture mode, the same reviewer gate validates backlog artifacts or a reviewed `no_candidate` disposition.

## Alternatives Considered

- **Self-verification by builder**: Builder both implements and verifies — conflicts of interest, misses systematic issues.
- **No completion gate**: Trust builder implicitly — acceptable only for trivial, no-risk changes but not as a general policy.
- **External review stage**: Separate human-in-the-loop — incompatible with autonomous LLM-driven workflow.
- **Soft review (non-blocking)**: Reviewer findings are advisory only — allows incomplete work to proceed.

## Consequences

**Positive:**
- Every delivery change is independently verified before completion.
- Blocking findings are captured with stable IDs, descriptions, and next actions.
- Revision loop provides structured rework without infinite iterations.
- Waiver mechanism handles edge cases where strict blocking would be counterproductive.

**Negative:**
- Adds workflow latency for the review stage.
- Requires clear separation of responsibilities between builder and reviewer.
- Waiver use must be tracked to avoid becoming a loophole.

## Affected Artifacts

- `system_definition/pbs/02-architecture/architecture.md` — Completion model, boundaries
- `system_definition/pbs/03-implementation/implementation.md` — Execution roles (reviewer is read-only)
- `.opencode/agents/orchestrator-reviewer.md` — Reviewer agent prompt
- `.opencode/dev_harness/workflow/control-policy.md` — Required stages, gate routing
- `.opencode/dev_harness/workflow/adaptive-risk-triggers.md` — Review helper selection

## Verification

Every completed guarded delivery run includes at least one reviewer gate decision in its run evidence. The revision loop policy is documented and has a cap of 3 iterations.

## Review Trigger

If the waiver mechanism is used more than once per 10 delivery tasks, or if blocked findings consistently exceed the revision loop cap, revisit the review gate design or the waiver criteria.