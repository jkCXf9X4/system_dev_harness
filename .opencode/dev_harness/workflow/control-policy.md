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

Directed helper stages run when their owning top-level stage determines they are needed from task risk. Missing required top-level output blocks completion. Missing helper output blocks completion only when the owning stage declared that helper required or when the helper is mandatory under the adaptive risk triggers below.

If a stage is not applicable, it must return:

```text
not_applicable
reason: <brief rationale>
evidence_inputs_inspected: <inputs reviewed before declaring not applicable>
```

Missing stage output or unjustified `not_applicable` blocks completion.

## Route Selection

Planner output separates the subject from the requested outcome:

```text
issue_kind: bug|fix|regression|feature|docs|cleanup|refactor|tuning|architecture|workflow|other
requested_outcome: implement_now|capture_candidate
route: delivery|improvement
```

Route to `delivery` when the user asks for actual changes now. Route to `improvement` when the user asks for a proposal, recommendation, evaluation, discovery, documented candidate, future task seed, or backlog item.

Bug, fix, regression, feature, documentation, cleanup, and refactoring subjects can all route to `improvement` when the requested outcome is candidate capture. Do not use the subject alone to block improvement routing.

## Structured Stage Feedback

Every top-level stage and directed helper returns these fields:

```text
user_feedback_required: true|false
user_feedback_request: <specific question, waiver request, or not_applicable>
improvement_candidates: <out-of-scope candidates or none>
research_requests: <research already performed or needed, or none>
```

When `user_feedback_required` is true, the orchestrator pauses and requests the user decision before continuing. Improvement candidates are backlog candidates only; they do not authorize scope expansion in the current task. Research requests are handled by `orchestrator-researcher` when source material is needed for the current stage.

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

Planner output must include:

```text
clarification_status: not_needed|required
blocking_uncertainty: <decision that cannot be made safely, or none>
clarification_questions: <one to three specific questions, or none>
assumption_rationale: <why assumptions are safe, or not_applicable>
```

Open questions alone do not require a pause. Only questions that materially change route, scope, acceptance, safety, or durable behavior should block the workflow.

## Focused Improvement Evaluation

Any working stage or directed helper may invoke `orchestrator-improvement-evaluator` when it finds a noteworthy improvement opportunity during its assigned work.

Any non-`none` `improvement_candidates` value in a stage output must receive a disk-backed disposition before final reporting. The owning stage should invoke `orchestrator-improvement-evaluator` before returning the candidate when the finding is concrete enough to evaluate. If a candidate reaches final reporting without a disposition, the reporter must return `user_feedback_required: true` and request evaluator disposition instead of treating the suggestion as complete.

Use the evaluator for focused findings only, not broad improvement discovery. A finding is backlog-worthy only when it has all of:

- concrete evidence from the current work
- meaningful impact, risk, maintenance cost, architecture pressure, or verification gap

The evaluator may persist qualifying candidates directly under `product-breakdown/06-evolution/candidates/`. Evaluator persistence is backlog capture only; it does not authorize scope expansion, current-task implementation, direct approval, or skipped checks.

When evidence is missing or the finding duplicates an existing candidate, the evaluator returns `needs_more_evidence` or `rejected` instead of writing a candidate file, but it must still write an evaluation record under `product-breakdown/06-evolution/evaluations/EVAL-YYYY-MM-DD-NNN.md`. Evaluation records are future-reference artifacts, not candidate backlog approval.

Every evaluator disposition must include one of:

- `persisted` with candidate ID and candidate file path
- `rejected` with evaluation ID, evaluation file path, and rejection reason
- `needs_more_evidence` with evaluation ID, evaluation file path, and missing-evidence rationale

## Workflow Memory

Any owning stage may request task-relevant workflow memory from `orchestrator-memory` when lessons, reusable patterns, or decision pointers could reduce repeated work or review misses.

The reviewer may identify memory candidates and stale or conflicting memory evidence, but does not own final memory incorporation. The reflection stage owns final memory-incorporation triage for completed workflows and may invoke `orchestrator-memory-curator` when evidenced findings reveal a durable lesson, reusable pattern, or decision pointer worth evaluating for memory. The focused improvement evaluator may invoke the curator only when a focused backlog finding also exposes a separate durable memory candidate. Curation is workflow memory capture only; it does not authorize scope expansion, current-task implementation, direct approval, or improvement backlog persistence.

Workflow memory lives under `.opencode/dev_harness_memories/`. Current task state, temporary investigation notes, implementation evidence, backlog candidates, and broad run history do not belong in memory.

Use this destination matrix when deciding what memory should contain:

- stable fact or decision pointer -> memory entry
- repeated failure or prevention rule -> lesson
- reusable operating procedure -> pattern
- broad future work -> improvement candidate
- one-off task evidence -> report or task history, not memory

Memory curation returns one of the following decision taxonomies and should preserve trust metadata when it writes or updates an entry:

- `accepted: durable lesson`
- `accepted: reusable pattern`
- `accepted: decision pointer`
- `rejected: duplicate`
- `rejected: one-off or task-local`
- `rejected: vague or not actionable`
- `rejected: rediscoverable`
- `rejected: unsafe or untrusted content`
- `rejected: belongs in improvement backlog`
- `needs_more_evidence`

## Final Reflection

Every completed guarded delivery or improvement workflow must run `orchestrator-reflection` before `orchestrator-reporter`.

Reflection owns final memory-incorporation triage. It reviews the completed run and returns one of:

```text
memory_written
memory_rejected
needs_more_evidence
no_memory_action
```

Reflection may invoke `orchestrator-memory-curator` only for evidenced repeatable findings that are task-independent and useful for future planning or review. It may invoke `orchestrator-improvement-evaluator` only when reflection exposes a separate backlog-worthy workflow problem.

When memory is relevant, reflection owns the memory hygiene summary: retrieved entries, trust metadata, revalidation status, stale or conflicting memory, memory decisions made, and whether memory influenced approval, blocking, or waiver outcomes.

Reflection must not:

- override the reviewer gate
- treat backlog candidates as durable memory
- store current task state, implementation evidence, temporary investigation notes, or full transcripts as memory
- expand the current task scope

The reporter relays the reflection-owned memory hygiene summary and any memory IDs written, rejected candidates, missing-evidence rationale, or no-memory-action rationale. The reporter must not synthesize new memory decisions or invoke memory curation.

## Adaptive Risk Triggers

Use helper agents based on task risk instead of forcing the full helper set for every task. A top-level stage may handle a task itself only when no trigger below applies, or when it returns an explicit `helper_not_used` rationale for each applicable-but-waived helper.

## Parallel Helper Execution

Planner and reviewer helpers should be grouped into parallel-safe helper packets whenever their inputs are available and their outputs do not depend on each other.

Parallel-safe planner helpers are read-only and can run together when they inspect different concerns from the same user request and repository evidence. Typical parallel planning packets include discovery, contract, architecture, lessons, memory, and researcher, unless one helper explicitly depends on another helper's output.

Parallel-safe reviewer helpers are read-only and can run together after builder evidence is available. Typical parallel review packets include verifier, review-completeness, review-architecture, review-lessons, memory, and researcher, unless a check needs another helper's result first.

Do not parallelize helper work when:

- a helper must consume another helper's output before it can produce useful evidence
- two helpers would write or mutate the same artifact
- the task requires a user clarification or waiver before helper work is meaningful
- external research must decide which files, checks, or standards another helper should inspect

Planner and reviewer outputs should include:

```text
parallel_helper_plan:
- packet_id: <short-id>
  helpers: <helper agents that can run together>
  dependencies: <packet IDs or none>
  reason: <why this packet is parallel-safe>
  expected_outputs: <evidence each helper must return>
```

Each helper disposition should report `parallel_safe: true|false`, `dependencies`, and `file_write_set`. Read-only helpers normally use `file_write_set: none`.

Planner triggers:

- Code changes require `orchestrator-discovery` and `orchestrator-contract`.
- Behavior changes require planner-owned test obligations in the work order.
- Product-breakdown or durable product behavior changes require planner-owned product placement, traceability, and decision-record obligations in the work order.
- Architecture, module-boundary, dependency-shape, or responsibility changes require `orchestrator-architecture`.
- Known repeated mistake risk or revision input requires `orchestrator-lessons`.
- Durable lesson, pattern, or decision uncertainty requires `orchestrator-memory`.
- External dependency, API, framework, standard, version, or documentation uncertainty requires `orchestrator-researcher` and `requires_external_research: true`.
- External/manual implementation requests are represented as a `handoff_required` section in the planner work order.

Builder triggers:

- Build, test, type-check, or dependency failures that need isolated diagnosis may use `orchestrator-build-error-resolver`.
- Created, moved, renamed, rewritten, replaced, deleted, or superseded artifacts that require reference patching, tracker/index updates, duplicate reconciliation, orphan cleanup, link checks, or traceability cleanup may use `orchestrator-cleanup`.
- External dependency, API, framework, standard, version, or documentation uncertainty during implementation may use `orchestrator-researcher`.
- Noteworthy cleanup or information-hygiene findings outside the approved scope may use `orchestrator-improvement-evaluator` for backlog evaluation instead of expanding the current task.

Reviewer triggers:

- Code changes require `orchestrator-verifier` plus `orchestrator-review-completeness`; architecture review is added when architecture triggers apply.
- Behavior changes require `orchestrator-review-completeness` to check acceptance criteria, edge cases, and test adequacy.
- Product-breakdown or information-artifact changes require `orchestrator-review-completeness`; durable decision changes also require `orchestrator-review-architecture`.
- Architecture, module-boundary, dependency-shape, or responsibility changes require `orchestrator-review-architecture`.
- Known repeated mistake risk or revision input requires `orchestrator-review-lessons`.
- Durable lesson, pattern, or decision uncertainty requires `orchestrator-memory`; evidenced repeatable memory candidates are reported to `orchestrator-reflection` for final memory triage.
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
