# Interface Contracts

IBD-adapted interface specification tables for all agent-to-agent handoffs in the guarded orchestration workflow.

SysML is a trademark of the Object Management Group (OMG).

Current as of IMP-032 (2026-06-29).

## Notation

Each handoff is documented with:
- **Source port**: the stage/agent that produces the output
- **Target port**: the stage/agent that consumes the input
- **Payload schema**: the structured fields carried across the handoff
- **Preconditions**: conditions that must hold before the handoff
- **Postconditions**: conditions that must hold after the handoff
- **Error handling**: how failures and edge cases are managed

---

## Top-Level Agent Handoffs

### H01: planner → builder

| Field | Value |
|---|---|
| Source port | planner work order output |
| Target port | builder work order input |
| Purpose | Hand off the approved implementation plan |
| Payload schema | Task normalization, summary header (per plan-summary-schema.md), minimum staged plan, control flags (workflow_mode, plan_approval_status, touches_information_artifacts, touches_product_breakdown, requires_decision_record, requires_external_research), tailoring_record, success criteria, helper dispositions, parallel_helper_plan, risk triggers, revision input (when applicable) |
| Preconditions | Planner has normalized the request, selected workflow mode, resolved uncertainty (or set clarification_status=required), selected helpers and grouped them into parallel-safe packets, produced the work order, and for delivery mode: persisted the plan summary |
| Postconditions | Builder receives a self-contained work order with no unresolved ambiguity. Builder may start implementation or candidate-capture persistence. |
| Error handling | If work order is incomplete or contradictory, builder returns blocking gap to reviewer. If clarification_status=required, builder does not execute until clarified. |

### H02: builder → reviewer

| Field | Value |
|---|---|
| Source port | builder evidence output |
| Target port | reviewer evidence input |
| Purpose | Submit implementation evidence for independent review and gating |
| Payload schema | Files changed (list), summary of implementation, cleanup evidence (stale references patched, trackers/indexes updated, duplicates reconciled, orphaned artifacts removed, links fixed, traceability updated), helper agents used and why (or none), helper lifecycle decisions, builder-owned review pass results (or none), information hygiene evidence, work order compliance assertion |
| Preconditions | Builder has completed all assigned changes within the approved scope. Cleanup has been performed. Information hygiene evidence has been collected. |
| Postconditions | Reviewer receives full evidence to verify contract satisfaction. Gate can compute approved, blocked, or waiver_required. |
| Error handling | If evidence is missing required sections (e.g., no cleanup evidence when information artifacts were touched), reviewers may block. Incomplete work is returned as blocked with specific finding IDs. |

### H03: reviewer → reflection

| Field | Value |
|---|---|
| Source port | reviewer gate output |
| Target port | reflection input |
| Purpose | Pass gate result and memory candidates to reflection stage |
| Payload schema | Gate status (approved | blocked | waiver_required), blocking gaps (list with finding IDs, descriptions, next actions), waivers granted (list with IDs, reasons, follow-ups), memory candidates identified for reflection (list), memory hygiene input (retrieved entries, revalidation status, stale/conflicting memory, whether memory influenced gate), helper dispositions, plan file verification result |
| Preconditions | Reviewer has completed all review helper calls, aggregated findings, and computed the gate decision |
| Postconditions | Reflection receives gate result and memory candidates for final memory triage |
| Error handling | If gate=blocked, the workflow loops back to planner for revision. Reflection only executes when gate=approved. |

### H04: reflection → reporter

| Field | Value |
|---|---|
| Source port | reflection memory triage output |
| Target port | reporter input |
| Purpose | Pass final memory triage results and completed run evidence to reporter |
| Payload schema | Memory candidates accepted/rejected/deferred (list with rationale), memory curator invocation evidence (when applicable), gate result, implementation summary, any remaining improvement candidates, tailoring_record |
| Preconditions | Reflection has reviewed the completed run for durable memory candidates. Memory curator has been invoked if needed. |
| Postconditions | Reporter produces the final control report summarizing the entire workflow run. |
| Error handling | Reflection must not override or block the gate result. Missing reflection output defaults to no memory candidates. |

### H05: builder → candidate-capture

| Field | Value |
|---|---|
| Source port | builder candidate-capture output |
| Target port | reviewer input (candidate-capture path) |
| Purpose | Persist improvement backlog candidates as information artifacts |
| Payload schema | Candidate files written (paths and IDs), candidate evidence, parent context traces, lifecycle stage (Candidate), duplicate check result |
| Preconditions | workflow_mode=candidate_capture. Planner work order specifies candidate persistence scope. Builder has inspected the target area and determined candidates are warranted or not. |
| Postconditions | Candidate files exist in candidates/ directory. Reviewer validates the persisted artifacts. |
| Error handling | If no candidate is warranted, builder returns no_candidate disposition with rationale. Reviewer validates no_candidate is justified. |

---

## Planner-Owned Directed Helper Handoffs

### H10: planner → discovery

| Field | Value |
|---|---|
| Source port | planner helper invocation |
| Target port | discovery helper input |
| Purpose | Repository inspection and smallest useful file set identification |
| Payload schema | Request scope, target paths (when specified), discovery questions |
| Preconditions | Adaptive risk triggers require or justify discovery. Planner has determined that repository inspection is needed. |
| Postconditions | Returns identified files, directory structure overview, relevant context for planning. |
| Error handling | Discovery may return no relevant files found with rationale. |

### H11: planner → contract

| Field | Value |
|---|---|
| Source port | planner helper invocation |
| Target port | contract helper input |
| Purpose | Produce checklistable requirements for the task |
| Payload schema | Task scope, user intent, product commitments, acceptance criteria references |
| Preconditions | Adaptive risk triggers require contract (code changes, behavior changes, or repo-state review with non-checklistable criteria) |
| Postconditions | Returns structured requirements list with IDs, descriptions, priorities, sources, and verification methods. |
| Error handling | If scope is too broad, contract returns scoping recommendations. |

### H12: planner → architecture

| Field | Value |
|---|---|
| Source port | planner helper invocation |
| Target port | architecture helper input |
| Purpose | Software architecture guardrails, module boundaries, durable design choices |
| Payload schema | Task scope, affected modules, architecture.md references |
| Preconditions | Adaptive risk triggers require architecture review (architecture, module-boundary, dependency-shape, or responsibility changes) |
| Postconditions | Returns architecture constraints, boundary analysis, design quality risks, and recommendations. |
| Error handling | If no architecture impact, returns not_applicable with rationale. |

### H13: planner → memory

| Field | Value |
|---|---|
| Source port | planner helper invocation |
| Target port | memory helper input |
| Purpose | Retrieve task-relevant workflow memory without editing |
| Payload schema | Task type, relevant domain keywords, known mistake patterns |
| Preconditions | Durable lesson, pattern, or decision uncertainty exists |
| Postconditions | Returns task-relevant lessons, reusable patterns, decision pointers, and trust metadata. |
| Error handling | Returns relevant entries or none found if no matching memory. |

### H14: planner → lessons

| Field | Value |
|---|---|
| Source port | planner helper invocation |
| Target port | lessons helper input |
| Purpose | Persistent mistake memory retrieval for known repeated mistake risk |
| Payload schema | Task context, known failure modes, revision input (when available) |
| Preconditions | Known repeated mistake risk or revision input is present |
| Postconditions | Returns relevant mistake memory entries with trust metadata and revalidation cues. |
| Error handling | Returns no relevant lesson entries if none match. |

---

## Trace Links

- Cross-references state machines in `agent-state-machines.md`
- Input for sequence diagrams and parametric constraints in `sequence-parametric.md`
- References architecture Stable Concepts from `architecture.md` (agent roles, handoff boundaries, completion model)
- Satisfies SysML IBD adaptation requirement (IMP-032 Seed 1)