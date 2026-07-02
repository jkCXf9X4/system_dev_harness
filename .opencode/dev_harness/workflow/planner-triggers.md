# Planner Triggers

Purpose: Defines tailoring profiles and planner-stage helper triggers for adaptive risk-based helper selection.

## Tailoring Profiles

The planner should select a baseline workflow profile before helper selection. Profiles set the default process depth; risk triggers then add or waive specific helpers on top of that baseline.

- `standard`: use for routine delivery work that needs the guarded chain but no exceptional escalation.
- `high_assurance`: use for behavior changes, cross-module work, architecture or boundary changes, external uncertainty, revision-heavy work, or high-blast-radius tasks.

The selected profile must be recorded in the planner work order's `tailoring_record`. Profile selection does not override mandatory helper triggers.

## Planner Triggers

- Repo-state review requests require `orchestrator-discovery`; add `orchestrator-contract` when the review criteria, scope, or success definition are not already checklistable.
- Code changes require `orchestrator-discovery` and `orchestrator-contract`.
- Behavior changes require planner-owned test obligations in the work order.
- System-definition or durable product behavior changes require planner-owned product placement, traceability, and decision-record obligations in the work order.
- Architecture, module-boundary, dependency-shape, or responsibility changes require `orchestrator-architecture`.
- Known repeated mistake risk or revision input requires `orchestrator-lessons`.
- Durable lesson, pattern, or decision uncertainty requires `orchestrator-memory`.
- External dependency, API, framework, standard, version, or documentation uncertainty requires `orchestrator-researcher` and `requires_external_research: true`.
- External/manual implementation requests are represented as a `handoff_required` section in the planner work order.
- Cross-system, multi-module, interface, workflow-stage, or systems-architecture-level analysis requires `orchestrator-systems-engineering`.

