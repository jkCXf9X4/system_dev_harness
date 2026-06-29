# IMP-030: Process Configuration Management And Root Cause Analysis

Use this template for one backlog-ready improvement candidate.

An improvement candidate is not implementation approval. It needs a scoped task contract before code or documentation changes begin.

## Lifecycle Stage

Candidate

## Status

Proposed

## Layer

Evolution

## Theme

Establish process configuration management (version-controlled process baselines) and a root cause analysis mechanism for systematic workflow failure investigation.

## Evidence

- `.opencode/dev_harness/workflow/control-policy.md` (lines 151-159: Revision Loop Policy has iteration cap and no-improvement detection — but no root cause analysis when the cap is exceeded; escalation goes to human without structured investigation)
- `.opencode/dev_harness/workflow/control-policy.md` (entire file: no reference to process baselines, process versioning, or configuration management of the workflow itself)
- `.opencode/dev_harness/workflow/adaptive-risk-triggers.md` (entire file: triggers are fixed rules — no process configuration management, no baseline comparison)
- ISO/IEC 15288 §6.3.6 — Configuration Management Process: "The configuration management process shall establish and maintain the integrity of all identified outputs and enable their identification, control, status accounting, and verification"
- ISO/IEC 15288 §6.3.8 — Root Cause Analysis (implied by corrective action process): "The corrective action process shall analyze the causes of problems and select corrective actions"
- CMMI — Causal Analysis and Resolution (CAR): "Identify causes of defects and other problems and take action to prevent them from occurring in the future"
- CMMI — Configuration Management: requires establishing baselines, tracking changes, and maintaining integrity of work products

## Current Pain Or Risk

**Process Configuration Management Gap:**
The workflow process itself (stage definitions, policies, agent prompts, risk triggers, gate rules) is version-controlled as part of the repository, but there is no:
- Explicit process baseline identification (which version of the workflow was used for which task)
- Versioned process changelog or rollout tracking
- Mechanism to compare process versions for effectiveness
- Configuration status accounting for the workflow as a managed process asset

**Root Cause Analysis Gap:**
When a workflow fails (blocked_max_reached, repeated blocking gaps, no-improvement escalation), there is no structured root cause analysis:
- No causal analysis of why the revision loop failed
- No systematic differentiation between process failure, implementation failure, and requirement failure
- No corrective action record with follow-up tracking
- No learning feedback loop from failures back into process improvement candidates

The workflow assumes that escalation to a human operator is sufficient, but without structured root cause data, the operator lacks the evidence needed for systematic improvement.

## Proposed Improvement

Two-part improvement:

### Part A: Process Configuration Baseline

1. **Process version identifier**: Add a `process_version` field to `plan-summary-schema.md` that records the workflow version in use (e.g., "dev-harness-v1.0" or a git hash of the `.opencode/dev_harness/` directory)

2. **Process changelog**: Create `.opencode/dev_harness/CHANGELOG.md` that records substantive changes to workflow structure, policies, risk triggers, and stage definitions — each entry references the relevant IMP candidate or task that drove the change

3. **Baseline reference in plan summaries**: Every plan summary records which workflow version was in effect at planning time, enabling post-hoc comparison of process effectiveness across versions

### Part B: Root Cause Analysis Mechanism

1. **Failure investigation trigger**: When the revision loop hits the iteration cap or triggers no-improvement detection, the blocked workflow creates an RCA record before escalating

2. **RCA Record Schema** (optional, can be lightweight):
   - `task_id`: the task that failed
   - `failure_mode`: `revision_cap_exceeded` | `no_improvement_detected` | `blocking_gap_escalation` | `waiver_rejected`
   - `symptoms`: what blocking gaps were observed
   - `causal_factors`: hypothesize root cause (process, requirement, implementation, tooling, or external)
   - `contributing_triggers`: which adaptive-risk triggers were (or should have been) active
   - `corrective_action`: suggested process or tooling change
   - `corrective_action_owner`: link to an IMP candidate or follow-up task

3. **Feedback into improvement backlog**: Each RCA record creates or updates an IMP candidate in the evolution backlog

## Expected Benefit

- Every workflow run is traceable to a specific process version
- Process changes are historically documented with rationale
- Workflow failures drive systematic improvement, not just ad-hoc escalation
- Provides CMMI Configuration Management and Causal Analysis & Resolution evidence
- Creates a closed feedback loop from process execution to process improvement

## Risk And Blast Radius

- Part A (process baselines) is low risk: adds one field to plan summary and one CHANGELOG file
- Part B (RCA) is medium risk: adds a new mechanism that could be over-invoked if the trigger is too sensitive
- Mitigation for Part B: only triggered on iteration cap exceeded or explicit no-improvement detection — not on every blocked gate
- Changes primarily affect control-policy.md, plan-summary-schema.md, and possibly the completion gate escalation logic

## Suggested Priority

Low (foundational improvement that enables systematic process evolution but requires multiple follow-up tasks)

## Selected Date

<!-- Date when this candidate was selected for implementation, or N/A -->

## Completed Date

<!-- Date when implementation was verified complete, or N/A -->

## Implementation Reference

<!-- Link to task contract, PR, or changelog entry when moved to done -->

## Task Contract Seed

The smallest scoped task for Part A only:
1. Add `process_version` field to `plan-summary-schema.md`
2. Create `.opencode/dev_harness/CHANGELOG.md` with initial entry describing the current workflow state
3. Update planner agent to resolve and record the process version in plan summaries

The smallest scoped task for Part B only:
1. Add `rca_triggered` field to control-policy.md revision loop section
2. Define RCA record format in the control-policy.md or a new `rca-schema.md`
3. Update the completion gate escalation path to create an RCA record when `blocked_max_reached`
4. Update reporter to include RCA references when applicable

## Out Of Scope

- Automated causal analysis (causal factors are heuristic/hypothesis-based)
- RCA database or dashboard
- Cross-task RCA pattern analysis
- Process version comparison analytics
- Automated rollback to previous process version

## Traceability

- Intent: ISO/IEC 15288 §6.3.6 Configuration Management, §6.3.8 Corrective Action; CMMI CAR and CM
- Product: Evolution layer — workflow process maturity
- Architecture: Additive to existing schemas; no structural changes
- Implementation: Updated plan-summary-schema, new CHANGELOG, updated control-policy escalation logic
- Verification: Plan summaries contain process_version; CHANGELOG exists and is non-empty; RCA records created when escalation triggers

## Notes

This gap is confirmed in the work-systems engineering evaluation (2026-06-29) as Discovery Gap #5: No process configuration management / root cause analysis. The workflow IS version-controlled (as all files in the repo), but there is no explicit process baseline management or RCA mechanism. This is the most complex of the five gaps and is scoped as the lowest initial priority, with Part A (process baselines) being the simpler and more implementable first step.