# Planner Triggers

Purpose: Defines tailoring profiles, lightweight skip rules, and planner-stage helper triggers for adaptive risk-based helper selection.

## Tailoring Profiles

The planner should select a baseline workflow profile before helper selection. Profiles set the default process depth; risk triggers then add or waive specific helpers on top of that baseline.

- `lightweight`: use for low-risk documentation, metadata-only, and narrow no-code work when no higher-risk trigger applies.
- `standard`: use for routine delivery work that needs the guarded chain but no exceptional escalation.
- `high_assurance`: use for behavior changes, cross-module work, architecture or boundary changes, external uncertainty, revision-heavy work, or high-blast-radius tasks.

The selected profile must be recorded in the planner work order's `tailoring_record`. Profile selection does not override mandatory helper triggers.

## Lightweight Skip Rules

When ALL of the following concrete thresholds are met, the lightweight profile enables stage-skipping behavior beyond normal helper selection:

- **Local blast radius**: change affects only the immediate task scope, no cascading effects
- **≤3 files**: change touches at most 3 files
- **No behavior change**: no functional, routing, or permission logic changes
- **No interface touch**: no shared interface surface modification
- **No architecture impact**: no module boundary, dependency shape, or design quality changes

When ALL thresholds are met:

- **Planner**: skip discovery, contract, architecture, lessons, memory, systems-engineering. Produce a direct work order unless a risk trigger explicitly fires.
- **Builder**: skip verifier, review-completeness, review-architecture, review-lessons. Use only build-error-resolver or cleanup if needed.
- **Reviewer**: single-stage review. Skip all review helper sub-agents.
- **Reflection**: skip entirely. Set `not_applicable`.
- **Reporter**: single-pass summary. Skip improvement-candidate processing.

> **Note**: `lightweight` profile selection alone does not trigger these skips — the concrete thresholds above must also be met. The planner must verify each threshold against the task before applying skip rules.

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

Source: extracted from `adaptive-risk-triggers.md` §A Tailoring Profiles, §B Lightweight Skip Rules, §C Planner Triggers.