# Adaptive Risk Triggers

Use helper agents based on task risk instead of forcing the full helper set for every task. A top-level stage may handle a task itself only when no trigger below applies, or when it returns an explicit `helper_not_used` rationale for each applicable-but-waived helper. Use `.opencode/dev_harness/workflow/workflow-memory.md` for workflow memory boundaries after this policy selects `orchestrator-memory`.

## Planner Triggers

- Code changes require `orchestrator-discovery` and `orchestrator-contract`.
- Behavior changes require planner-owned test obligations in the work order.
- Product-breakdown or durable product behavior changes require planner-owned product placement, traceability, and decision-record obligations in the work order.
- Architecture, module-boundary, dependency-shape, or responsibility changes require `orchestrator-architecture`.
- Known repeated mistake risk or revision input requires `orchestrator-lessons`.
- Durable lesson, pattern, or decision uncertainty requires `orchestrator-memory`.
- External dependency, API, framework, standard, version, or documentation uncertainty requires `orchestrator-researcher` and `requires_external_research: true`.
- External/manual implementation requests are represented as a `handoff_required` section in the planner work order.

## Builder Triggers

- Build, test, type-check, or dependency failures that need isolated diagnosis may use `orchestrator-build-error-resolver`.
- Created, moved, renamed, rewritten, replaced, deleted, or superseded artifacts that require reference patching, tracker/index updates, duplicate reconciliation, orphan cleanup, link checks, or traceability cleanup may use `orchestrator-cleanup`.
- External dependency, API, framework, standard, version, or documentation uncertainty during implementation may use `orchestrator-researcher`.
- Noteworthy cleanup or information-hygiene findings outside the approved scope may be returned as `improvement_candidates` instead of expanding the current task.

## Reviewer Triggers

- Code changes require `orchestrator-verifier` plus `orchestrator-review-completeness`; architecture review is added when architecture triggers apply.
- Behavior changes require `orchestrator-review-completeness` to check acceptance criteria, edge cases, and test adequacy.
- Product-breakdown or information-artifact changes require `orchestrator-review-completeness`; durable decision changes also require `orchestrator-review-architecture`.
- Architecture, module-boundary, dependency-shape, or responsibility changes require `orchestrator-review-architecture`.
- Known repeated mistake risk or revision input requires `orchestrator-review-lessons`.
- Durable lesson, pattern, or decision uncertainty requires `orchestrator-memory`; evidenced repeatable memory candidates are reported to `orchestrator-reflection` for final memory triage.
- External dependency, API, framework, standard, version, or documentation uncertainty requires `orchestrator-researcher`; reviewer may not approve external claims without cited researcher evidence or a waiver.

Low-risk documentation, formatting, wording, or metadata-only tasks may be planned or reviewed directly when the stage records why no risk trigger applies.
