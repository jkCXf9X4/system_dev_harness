# Workflow Control Policy

Use this policy for guarded workflow control, stage applicability, control flags, and waivers.

## Required Stages

Every listed top-level guarded workflow stage must run:

```text
orchestrator-planner
orchestrator-builder
orchestrator-reviewer
orchestrator-reflection
orchestrator-reporter
```

Directed helper stages run when their owning top-level stage determines they are needed from task risk. Missing required top-level output blocks completion. Missing helper output blocks completion only when the owning stage declared that helper required or when the helper is mandatory under `.opencode/dev_harness/workflow/adaptive-risk-triggers.md`.

If a stage is not applicable, it must use the `not_applicable` fields from `.opencode/dev_harness/workflow/stage-output-schema.md`. Missing stage output or unjustified `not_applicable` blocks completion.

## Route Selection

Planner output separates the subject from the requested outcome:

```text
issue_kind: bug|fix|regression|feature|docs|cleanup|refactor|tuning|architecture|workflow|review|other
requested_outcome: implement_now|capture_candidate
workflow_mode: delivery|candidate_capture
route: guarded_chain
```

Use `workflow_mode: delivery` when the user asks for actual changes now. Use `workflow_mode: candidate_capture` when the user asks for a proposal, recommendation, evaluation, discovery, review-only assessment, documented candidate, future task seed, or backlog item.

Bug, fix, regression, feature, documentation, cleanup, and refactoring subjects can all use `workflow_mode: candidate_capture` when the requested outcome is candidate capture. Do not use the subject alone to block candidate capture.

Repo-state review requests use the same split: review-and-change requests are delivery, while review-only assessment requests are candidate capture with either persisted candidates or a reviewed `no_candidate` result.

Both workflow modes use the same guarded chain: planner, builder, reviewer, reflection, and reporter. In `candidate_capture` mode, load `.opencode/dev_harness/workflow/candidate-capture.md` for detailed ownership, write-boundary, disposition, and review rules.

## Tailoring

The workflow must be tailored to the task and project context instead of applying the same process depth to every request. The planner must choose the lightest workflow profile that still covers the task's risk, uncertainty, and traceability needs, then record that choice in `tailoring_record`.

Use these baseline profiles:

- `lightweight` for low-risk documentation, metadata-only, or narrow no-code tasks with no architecture, external dependency, or major verification risk. When all concrete thresholds from `.opencode/dev_harness/workflow/adaptive-risk-triggers.md` are met, stages may be skipped per the Lightweight Skip Rules defined there.
- `standard` for routine contained delivery tasks that need the full guarded chain but no exceptional escalation.
- `high_assurance` for behavior changes, cross-module changes, architecture or boundary changes, external uncertainty, revision-heavy work, large jobs, or other high-blast-radius tasks.

Tailoring may change helper depth, review emphasis, or whether optional helpers are invoked. Tailoring does not remove required stages, waive evidence requirements, or bypass review and gate rules. When a task uses a narrower or broader process than the default, the planner must explain why in the work order and plan summary. When `lightweight` profile is selected and all concrete thresholds from `.opencode/dev_harness/workflow/adaptive-risk-triggers.md` are met, the planner work order must record which stages are skipped and why in the `tailoring_record`.

## Stage Output Schema

Every top-level stage and directed helper returns the common fields from `.opencode/dev_harness/workflow/stage-output-schema.md`.

## Plan Draft Approval

For `workflow_mode: delivery`, the planner emits a draft work order before builder execution.

Planner output uses:

```text
plan_approval_status: not_required|pending
plan_approval_reason: large_job|destructive|operator_requested|not_applicable
```

Use `plan_approval_status: pending` when builder execution must wait for operator approval. Required approval triggers include:

- `large_job_triggered: true`
- destructive or high-blast-radius changes
- explicit user requests to review or approve the plan before implementation

Use `plan_approval_status: not_required` for routine low-risk delivery work. Candidate-capture work does not require plan draft approval unless the workflow is explicitly extended.

Operator decisions route as follows:

- `approve`: orchestrator forwards the approved planner work order to builder.
- `revise`: orchestrator calls planner again with the user's requested revision and prior planner output.
- `reject`: orchestrator stops before builder execution and reports the rejection rationale.

Operator decisions are routing inputs, not `plan_approval_status` values.

Large-job approval is one trigger for this draft approval cycle; do not route large jobs through a separate approval path.

## Initial Clarification Gate

The planner must distinguish harmless assumptions from blocking uncertainty before routing work to delivery or improvement.

Set `user_feedback_required: true` and ask the user for clarification when uncertainty materially affects any of:

- requested outcome: implement now versus capture candidate
- target artifact, module, feature, or document
- intended behavior, acceptance criteria, or success definition
- scope boundary or out-of-scope work
- destructive, broad, irreversible, or high-blast-radius changes
- user preference that would materially change the solution
- external dependency, API, framework, standard, version, or documentation choice that cannot be resolved safely through researcher evidence

The planner may proceed with stated assumptions when all of these are true:

- the ambiguity is low impact
- the likely interpretation is strongly implied by the user's wording or repository context
- proceeding will not edit unrelated files, commit to durable product behavior, or perform destructive work
- the assumption can be verified or corrected by normal discovery, implementation, or review

Planner output must include the clarification fields from `.opencode/dev_harness/workflow/stage-output-schema.md`.

Open questions alone do not require a pause. Only questions that materially change route, scope, acceptance, safety, or durable behavior should block the workflow.

## Candidate Capture Disposition

Any working stage or directed helper may return incidental `improvement_candidates` under `.opencode/dev_harness/workflow/stage-output-schema.md`. Detailed incidental candidate handling, candidate-capture criteria, and valid dispositions live in `.opencode/dev_harness/workflow/candidate-capture.md`.

## Workflow Memory

Load `.opencode/dev_harness/workflow/workflow-memory.md` when a stage needs task-relevant memory, memory curation, memory hygiene evidence, or final reflection memory-incorporation rules.

## Final Reflection

Every completed guarded workflow, including candidate capture, must run `orchestrator-reflection` before `orchestrator-reporter`. Detailed reflection and memory-incorporation rules live in `.opencode/dev_harness/workflow/workflow-memory.md`.

## Adaptive Risk Triggers

Load `.opencode/dev_harness/workflow/adaptive-risk-triggers.md` when planner, builder, or reviewer decides which helpers are required, optional, or waived.

## Parallel Helper Execution

Load `.opencode/dev_harness/workflow/parallel-helper-execution.md` when planner or reviewer groups independent helpers into parallel-safe packets.

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
