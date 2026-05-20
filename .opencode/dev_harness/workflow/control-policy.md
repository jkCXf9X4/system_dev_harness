# Workflow Control Policy

Use this policy for guarded workflow control, stage applicability, control flags, and waivers.

## Required Stages

Every listed guarded workflow stage must run.

If a stage is not applicable, it must return:

```text
not_applicable
reason: <brief rationale>
evidence_inputs_inspected: <inputs reviewed before declaring not applicable>
```

Missing stage output or unjustified `not_applicable` blocks completion.

## Control Flags

Planner, contract, and packet stages must carry these flags forward:

```text
touches_information_artifacts: true|false
touches_product_breakdown: true|false
requires_decision_record: true|false
requires_external_research: true|false
```

The contract may correct planner flags when discovery proves the planner wrong. The packet must preserve the contract flags. Verifier and gate stages use packet and contract flags as the source of truth for required evidence.

## Handoff Boundary

External or manual handoff is non-executing guidance unless the orchestrator explicitly uses it as builder-stage input.

Any external or manual implementation must produce builder-equivalent evidence and still pass verifier, independent reviews, completion gate, and final reporting.

A handoff cannot authorize scope expansion, skipped checks, direct approval, or waived failures.

## Waivers

Waivers are not approvals.

A waiver requires explicit user approval plus:

- named risk
- waiver scope
- follow-up or expiry condition

Without those fields, `needs_waiver` findings result in `waiver_required`, not `approved`.

## Revision Loop Policy

When the completion gate returns `blocked`, the guarded workflow enters a revision loop:

1. **Iteration cap.** Default maximum of 3 revision attempts. The contract or packet may override this cap per-task by setting `max_revision_attempts` in the control flags.
2. **No-improvement detection.** If the same blocking gap IDs appear in consecutive iterations, escalate to the human operator immediately instead of looping again.
3. **Revision control flag.** When a revision is active, the `revision` control flag is set to `true` with the current iteration count (e.g., `revision: true, revision_count: 2`). This flag is carried from the gate through the planner to downstream stages so that contract, architecture, lessons, and packet know the revision context.
4. **Evidence preservation.** All review findings from every iteration must be preserved and attached to the final report, regardless of whether the workflow completes, loops, or escalates.
5. **Escalation.** When the iteration cap is exceeded or no-improvement detection triggers, the workflow produces a `blocked_max_reached` status with full iteration history. A human operator decides the next action.
