# Agent State Machines

> **Runtime reference copy for agent context.** Canonical source: `system_definition/pbs/02-architecture/agent-state-machines.md`.

State/transition tables for the four top-level workflow agents: planner, builder, reviewer, and reflection.

Current as of IMP-032 (2026-06-29).

Last reviewed: 2026-06-29.

> **External references:** This file adapts SysML concepts (state machine notation) for analytical use within this workflow. SysML is a trademark of OMG. Descriptions are original summaries; for authoritative definitions, consult the SysML specification directly.

## Notation

Each agent uses these states:
- **Idle**: Not yet invoked or has completed work
- **Active**: Currently executing its stage responsibility
- **Blocked**: Cannot proceed without external input (user clarification, waiver, or revision)
- **Waiting_for_input**: Awaiting helper or upstream stage output
- **Completed**: Finished its stage with a definitive outcome

Transitions specify:
- **Trigger**: Event or condition that causes the transition
- **Guards**: Conditions that must hold for the transition to fire
- **Effects**: Actions or side effects of the transition

---

## Planner State Machine

| Current State | Trigger | Guards | Effect | Next State |
|---|---|---|---|---|
| Idle | Invoked by orchestrator with user request | Workflow mode not yet determined | Load instructions, apply control policy | Active |
| Active | Task normalization complete | Request is ambiguous | Set clarification_status=required, set user_feedback_required=true | Blocked |
| Active | Task normalization complete | Request is clear, workflow mode selected | Select helpers per adaptive risk triggers, plan parallel helper packets | Active (helper planning) |
| Active (helper planning) | Helpers selected and dispatched | Helpers can run in parallel | Invoke parallel-safe helper packets | Waiting_for_input |
| Waiting_for_input | Helper outputs received | All dispatched helpers returned | Synthesize work order from helper outputs | Active (synthesis) |
| Active (synthesis) | Work order complete | workflow_mode=delivery | Write plan summary to .opencode/dev_harness_plans/ | Active (plan persistence) |
| Active (synthesis) | Work order complete | workflow_mode=candidate_capture | Skip plan persistence | Active (output) |
| Active (plan persistence) | Plan summary written | Approval not required | Emit work order to builder | Completed |
| Active (plan persistence) | Plan summary written | Approval required | Set plan_approval_status=pending, request operator approval | Blocked |
| Blocked | User clarification received | All blocked decisions resolved | Update work order with clarification | Active |
| Blocked | Operator approval received | Approval granted | Proceed to builder handoff | Completed |
| Blocked | Operator rejected plan | Rejection with guidance | Revise plan per rejection | Active |
| Blocked | Revision input from blocked gate | Iteration count ≤ max_revision_loops | Revise scope to address blocking findings | Active |
| Blocked | Revision input from blocked gate | Iteration count > max_revision_loops | Escalate to operator, return blocked_max_reached | Completed (blocked escalation) |

---

## Builder State Machine

| Current State | Trigger | Guards | Effect | Next State |
|---|---|---|---|---|
| Idle | Invoked with planner work order | Work order is valid, clarification not required | Load work order, determine assigned files | Active |
| Active | Implementation started | workflow_mode=delivery | Apply changes per work order | Active (implementation) |
| Active | Candidate persistence started | workflow_mode=candidate_capture | Persist backlog artifacts per candidate-capture.md | Active (candidate persistence) |
| Active (implementation) | Build or test failure detected | Build error resolver available | Invoke orchestrator-build-error-resolver | Waiting_for_input |
| Active (implementation) | Cleanup needed after changes | Information artifacts touched | Invoke orchestrator-cleanup | Waiting_for_input |
| Waiting_for_input | Build error resolver returned | Issue resolved or waiver needed | Continue implementation or report blocker | Active |
| Waiting_for_input | Cleanup helper returned | All cleanup tasks complete | Collect cleanup evidence | Active |
| Active (implementation) | All changes applied, cleanup done | All required changes within scope applied | Run builder-owned review pass (optional) | Active (review pass) |
| Active (review pass) | Builder review pass complete | No blocking issues found | Collect implementation evidence | Active (evidence) |
| Active (review pass) | Builder review pass complete | Blocking issues found | Fix issues | Active |
| Active (evidence) | Implementation evidence collected | Evidence includes files changed, summary, cleanup, helper dispositions | Emit evidence to reviewer | Completed |
| Active (candidate persistence) | Candidate files written | Files saved to disk, duplicates checked | Collect persistence evidence | Active (evidence) |
| Active (candidate persistence) | No candidate warranted | inspected scope does not justify backlog artifact | Set disposition=no_candidate with rationale | Completed |

---

## Reviewer State Machine

| Current State | Trigger | Guards | Effect | Next State |
|---|---|---|---|---|
| Idle | Invoked with builder evidence | Evidence bundle is non-empty | Load evidence, apply control policy | Active |
| Active | Verification needed | Code changes present or verifier trigger active | Invoke orchestrator-verifier | Waiting_for_input |
| Active | Review needed | Adaptive risk triggers require review helpers | Invoke independent review helpers (parallel-safe packets) | Waiting_for_input |
| Active | Plan file verification needed | workflow_mode=delivery | Check plan file exists, has required fields | Active |
| Waiting_for_input | Verifier returned | Results collected | Aggregate verification evidence | Active |
| Waiting_for_input | Review helpers returned | All dispatched helpers returned | Aggregate review findings | Active |
| Active (aggregation) | All evidence collected | No blocking gaps found | Set gate=approved | Completed |
| Active (aggregation) | All evidence collected | Blocking gaps found, waiver possible | Evaluate waiver, set gate=waiver_required or blocked | Completed |
| Active | No verification or review needed | Low-risk task, direct review rationale provided | Assess evidence directly | Active (aggregation) |

---

## Reflection State Machine

| Current State | Trigger | Guards | Effect | Next State |
|---|---|---|---|---|
| Idle | Invoked after reviewer gate=approved | Gate result available | Load gate output, implementation summary | Active |
| Active | Memory triage started | Memory candidates identified in reviewer output | Evaluate each candidate for durability | Active (evaluation) |
| Active | Memory triage started | No memory candidates identified | Set result=no candidates | Completed |
| Active (evaluation) | Durable candidate found | Evidence supports repeatable lesson | Accept candidate, invoke memory curator (optional) | Active (curation) |
| Active (evaluation) | Insufficient evidence | Pattern not yet repeatable | Defer candidate with rationale | Active (next) |
| Active (evaluation) | Not applicable | Finding is task-local or not a memory concern | Reject candidate | Active (next) |
| Active (curation) | Memory curator returned | Changes persisted | Record curation result | Active (next) |
| Active (next) | All candidates processed | — | Prepare memory triage summary | Active (summary) |
| Active (summary) | Summary prepared | — | Emit output to reporter | Completed |

---

## Trace Links

- States referenced by sequence diagrams in `sequence-parametric.md`
- Triggers and guards cross-reference handoff payloads in `interface-contracts.md`
- Completeness of state sets satisfies SysML State Machine adaptation requirement (IMP-032 Seed 2)