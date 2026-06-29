# VD-003: Independent Review Requirement

## Status

Accepted

## Layer

Verification

## Context

The guarded orchestrator workflow includes a reviewer stage as the completion gate authority (see PD-003). For the review to be meaningful, the reviewer must operate independently from the builder — the same agent that implements a change should not be the sole authority on whether that change is correct. This separation of duty is a key architectural principle for quality assurance.

## Decision

Every change delivered through the guarded workflow MUST be independently reviewed before completion:

- The reviewer stage (`orchestrator-reviewer`) is a separate agent from the builder (`orchestrator-builder`).
- The reviewer is **read-only**: it inspects evidence but never edits implementation files.
- The reviewer coordinates independent subagents (verifier, review-architecture, review-completeness, review-lessons) that are also read-only.
- Review helpers evaluate implementation evidence against contract, architecture, lessons, and information hygiene criteria.
- The completion gate (approved, blocked, waiver_required) is computed by the reviewer based on aggregated findings.
- In `workflow_mode: candidate_capture`, the same independent review gate validates backlog artifacts.

The reviewer's independence is structural — enforced by agent permission configurations (`edit: deny`, `write: deny`) and by the workflow control policy.

## Alternatives Considered

- **Builder self-review**: Builder verifies its own work — efficient but conflicts of interest.
- **External human review**: Operator manually verifies — incompatible with autonomous execution and inconsistent.
- **No review**: Trust all builder output — acceptable only for trivial changes with no risk triggers.
- **Separate review agent with edit permissions**: Reviewer could fix minor issues — blurs separation of duty and risks scope creep.

## Consequences

**Positive:**
- Structural independence ensures impartial verification.
- Read-only enforcement prevents reviewers from making unverified changes.
- Adaptive helper selection (via risk triggers) ensures appropriate review depth per task.
- Consistent gate outcomes per delivery.

**Negative:**
- Review stage adds workflow latency.
- Requires clear evidence handoff from builder to reviewer.
- Review helpers may duplicate effort if not well coordinated.

## Affected Artifacts

- `.opencode/agents/orchestrator-reviewer.md` — Reviewer agent (edit: deny, write: deny)
- `.opencode/dev_harness/workflow/control-policy.md` — Required stages, gate routing
- `.opencode/dev_harness/workflow/agent-boundaries.md` — Read-only agents list
- `product-breakdown/pbs/02-architecture/architecture.md` — Completion model, boundaries
- `.opencode/dev_harness/workflow/adaptive-risk-triggers.md` — Review helper triggers

## Verification

Every completed delivery run's evidence includes a reviewer gate decision. The reviewer agent configuration has `edit: deny` and `write: deny`. No delivery run completes without passing through the reviewer stage.

## Review Trigger

If a delivery run completes without evidence of independent review (e.g., the reviewer agent was not invoked), or if the reviewer configuration is changed to allow editing, this decision must be revisited.