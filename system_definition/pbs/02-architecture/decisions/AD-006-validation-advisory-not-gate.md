# AD-006: Validation Is Advisory, Not A Completion Gate

## Status

Accepted

## Layer

Architecture

## Context

IMP-026 added a read-only validation stage (`orchestrator-validation`) between builder and reviewer in the guarded workflow chain. The validation stage checks builder evidence against planner intent and acceptance criteria, returning `pass`, `fail`, or `not_applicable`. When validation returns `fail`, the workflow routes back to the planner for revision — the same routing mechanism used by the reviewer stage when it returns `blocked`.

This structural similarity raised a legitimate architectural question: does validation `fail` constitute an independent gate decision, and if so, does it violate PD-003's single-gate-authority model?

PD-003 states: **"The reviewer stage is the only completion gate authority."**

The validation stage was deliberately introduced as an upstream advisory check (see IMP-026 plan summary, Risks section item #5, and the follow-up deferred to BC-004). However, without explicit architectural documentation, future agents or operators could misinterpret validation `fail` as a second gate authority or question whether PD-003 needs revision.

## Decision

Validation is an **upstream advisory check**, NOT an independent completion gate. The single-gate-authority model defined in PD-003 is preserved.

The distinction rests on the difference in trigger, meaning, and consequence:

| Dimension | Validation `fail` | Reviewer `blocked` |
|-----------|-------------------|-------------------|
| **Trigger** | Intent-to-outcome traceability gap — builder evidence does not match planner intent or acceptance criteria | Final gate verification failure — work does not meet completion bar |
| **Meaning** | Upstream finding: "revisit the approach or evidence before formal review" | Gate finding: "this task cannot complete without revision" |
| **Consequence** | Routes back to planner for revision; planner may revise scope, refine intent, or adjust the approach | Routes back to planner for revision; planner must address the blocking finding |
| **Which stage ends the task?** | Neither — both route back to planner. Only the reviewer can permanently block completion via the revision loop cap (3 iterations, then `blocked_max_reached`) | Same — reviewer gates are subject to the same revision loop cap |
| **Gate authority** | None — validation is advisory; it cannot produce `approved` or `blocked` | Sole gate authority per PD-003 — produces `approved`, `blocked`, or `waiver_required` |

The key architectural property is that validation does not have the authority to produce a terminal outcome. It can only signal a need for revision. The reviewer retains exclusive authority to:

- `approve` — complete the task
- `blocked` — halt the task (subject to revision loop cap)
- `waiver_required` — escalate to human operator

Validation and reviewer share a routing mechanism (back to planner) but serve fundamentally different roles: validation is a quality-of-intent check that catches misalignment early; the reviewer is the completion gate that decides whether the task is done.

This is analogous to a code linter versus a code reviewer: both can flag issues and send work back, but only the reviewer can approve or reject a pull request.

## Alternatives Considered

- **Treat validation as a second gate authority**: Explicitly give validation the power to block tasks independently. Rejected — creates dual-gate ambiguity, violates PD-003, and adds unnecessary process overhead without clear benefit since the reviewer already gates completion.

- **Embed validation inside the reviewer stage**: Instead of a separate stage, have the reviewer run validation checks as part of its gate decision. Rejected at this time — a separate stage provides earlier feedback, reduces reviewer context load, and makes validation results inspectable before the reviewer gate. This is tracked as a potential future evolution (see IMP-049).

- **Remove validation entirely**: Rely solely on the reviewer's existing VAL-001 through VAL-005 checks. Rejected — the validation stage catches intent-alignment gaps before the reviewer gate, reducing revision cycles and providing a dedicated check that is not diluted by other review concerns.

- **No documentation change**: Accept the ambiguity and rely on future agents to reason about PD-003 consistency independently. Rejected — the structural similarity between validation `fail` and reviewer `blocked` is a known ambiguity risk (identified in IMP-026, deferred to BC-004 / IMP-048). Explicit documentation eliminates future misinterpretation.

## Consequences

**Positive:**
- Eliminates ambiguity about validation stage authority relative to PD-003.
- Future agents can reference the documented rationale instead of rediscovering it.
- Preserves the architectural clarity of a single gate authority.
- Validation remains an early, lightweight check that can send work back for revision without conflicting with the reviewer's gate role.

**Negative:**
- The shared routing mechanism (both `fail` and `blocked` go back to planner) may still appear redundant to operators unfamiliar with the distinction, requiring this documentation to explain the difference.
- If validation routing is ever changed to bypass the planner (e.g., direct builder revision), this decision record would need to be revisited.

## Affected Artifacts

- `system_definition/fbs/01-product/decisions/PD-003-verification-before-completion-gating.md` — Referenced as the single-gate-authority constraint; no changes to PD-003 itself.
- `system_definition/pbs/02-architecture/decisions/` — This decision record.
- `system_definition/decision-log.md` — Index update to add this record.
- `.opencode/agents/orchestrator-validation.md` — Validation agent definition; no changes, but this record documents its architectural intent.
- `.opencode/dev_harness/workflow/control-policy.md` — Required Stages and routing; no changes, but referenced for routing mechanism.
- `system_definition/cross-cutting/06-evolution/selected/IMP-048.md` — Implementation reference for this decision record.

## Verification

- This decision record exists in the architecture decisions directory with Status: Accepted.
- The record explicitly states that validation is an advisory check, not a completion gate.
- The record cites PD-003's exact text: "The reviewer stage is the only completion gate authority."
- The record references IMP-026, `control-policy.md` (validation routing), and `orchestrator-validation.md`.
- The decision-log index includes an entry for AD-006 with a link to this file.