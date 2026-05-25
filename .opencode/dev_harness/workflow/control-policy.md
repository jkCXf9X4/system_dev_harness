# Workflow Control Policy

Use this policy for guarded workflow control, stage applicability, control flags, and waivers.

## Required Stages

Every listed top-level guarded workflow stage must run:

```text
orchestrator-planner
orchestrator-builder
orchestrator-reviewer
orchestrator-reporter
```

Directed helper stages run when their owning top-level stage determines they are needed from task risk. Missing required top-level output blocks completion. Missing helper output blocks completion only when the owning stage declared that helper required or when the helper is mandatory under the adaptive risk triggers below.

If a stage is not applicable, it must return:

```text
not_applicable
reason: <brief rationale>
evidence_inputs_inspected: <inputs reviewed before declaring not applicable>
```

Missing stage output or unjustified `not_applicable` blocks completion.

## Structured Stage Feedback

Every top-level stage and directed helper returns these fields:

```text
user_feedback_required: true|false
user_feedback_request: <specific question, waiver request, or not_applicable>
improvement_candidates: <out-of-scope candidates or none>
research_requests: <research already performed or needed, or none>
```

When `user_feedback_required` is true, the orchestrator pauses and requests the user decision before continuing. Improvement candidates are backlog candidates only; they do not authorize scope expansion in the current task. Research requests are handled by `orchestrator-researcher` when source material is needed for the current stage.

## Adaptive Risk Triggers

Use helper agents based on task risk instead of forcing the full helper set for every task. A top-level stage may handle a task itself only when no trigger below applies, or when it returns an explicit `helper_not_used` rationale for each applicable-but-waived helper.

Planner triggers:

- Code changes require `orchestrator-discovery` and `orchestrator-contract`.
- Behavior changes require planner-owned test obligations in the work order.
- Product-breakdown or durable product behavior changes require planner-owned product placement, traceability, and decision-record obligations in the work order.
- Architecture, module-boundary, dependency-shape, or responsibility changes require `orchestrator-architecture`.
- Known repeated mistake risk or revision input requires `orchestrator-lessons`.
- External dependency, API, framework, standard, version, or documentation uncertainty requires `orchestrator-researcher` and `requires_external_research: true`.
- External/manual implementation requests are represented as a `handoff_required` section in the planner work order.

Reviewer triggers:

- Code changes require `orchestrator-verifier` plus `orchestrator-review-completeness`; architecture review is added when architecture triggers apply.
- Behavior changes require `orchestrator-review-completeness` to check acceptance criteria, edge cases, and test adequacy.
- Product-breakdown or information-artifact changes require `orchestrator-review-completeness`; durable decision changes also require `orchestrator-review-architecture`.
- Architecture, module-boundary, dependency-shape, or responsibility changes require `orchestrator-review-architecture`.
- Known repeated mistake risk or revision input requires `orchestrator-review-lessons`.
- External dependency, API, framework, standard, version, or documentation uncertainty requires `orchestrator-researcher`; reviewer may not approve external claims without cited researcher evidence or a waiver.

Low-risk documentation, formatting, wording, or metadata-only tasks may be planned or reviewed directly when the stage records why no risk trigger applies.

## Control Flags

Planner-owned planning output must carry these flags forward into builder and reviewer evidence:

```text
touches_information_artifacts: true|false
touches_product_breakdown: true|false
requires_decision_record: true|false
requires_external_research: true|false
```

Planner-directed helpers may correct initial flags when discovery or specialist planning proves them wrong. Reviewer and gate checks use the final planner work order as the source of truth for required evidence.

## Handoff Boundary

External or manual handoff is non-executing guidance unless the orchestrator explicitly uses it as builder-stage input.

Any external or manual implementation must produce builder-equivalent evidence and still pass reviewer-coordinated verification, independent reviews, completion gate, and final reporting.

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

1. **Iteration cap.** Default maximum of 3 revision attempts. The planner work order may override this cap per-task by setting `max_revision_attempts` in the control flags.
2. **No-improvement detection.** If the same blocking gap IDs appear in consecutive iterations, escalate to the human operator immediately instead of looping again.
3. **Revision control flag.** When a revision is active, the `revision` control flag is set to `true` with the current iteration count (e.g., `revision: true, revision_count: 2`). This flag is carried from the gate through the planner to downstream stages so that selected helpers know the revision context.
4. **Evidence preservation.** All review findings from every iteration must be preserved and attached to the final report, regardless of whether the workflow completes, loops, or escalates.
5. **Escalation.** When the iteration cap is exceeded or no-improvement detection triggers, the workflow produces a `blocked_max_reached` status with full iteration history. A human operator decides the next action.
