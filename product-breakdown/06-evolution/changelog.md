# Changelog

## 2026-06-01

- Implemented IMP-001 through IMP-005 by adding workflow-memory trust metadata, curation taxonomy, durable-memory boundaries, memory hygiene reporting, and procedural-pattern guidance.
- Implemented IMP-007 by adding a final reflection stage that owns memory-incorporation triage before final reporting.
- Implemented IMP-006 by adding an initial clarification gate to planner and workflow policy, plus orchestrator routing behavior for planner-requested clarification.

## 2026-05-26 — Consolidation: removed self-duplicate imp.md, added @see references to centralize governance rules (control-policy.md) and lifecycle docs (06-evolution/README.md)

## 2026-05-26

- Migrated improvement lifecycle from `backlog/` to three-stage folder structure: `candidates/`, `selected/`, `done/`
- Added `06-evolution/README.md` documenting the lifecycle model
- Updated all agent and template references to use new paths
## 2026-05-30

- Refreshed the source product-breakdown docs to match the current agent set and the backlog-oriented evolution layer.
- Added UC-013 for direct operator-chosen build work and ED-001 for the canonical evolution candidate location.
- Replaced the verification traceability stub with a concrete matrix tied to the current smoke and review coverage.
- Updated the source traceability map and operator-facing evolution docs to include the evolution/candidates path.

## 2026-05-20

- Implemented IMP-001 through IMP-009 improvements:
  - Renamed docs directories to match product-breakdown template numbering
  - Distributed ADR files into per-layer `decisions/` directories with prefixed IDs
  - Created verification layer (`04-verification/`) and operation layer (`05-operation/`)
  - Added root `decision-log.md` and `traceability-map.md`
  - Added revision loop to guarded workflow (blocked gate → planner re-scoping)
  - Added improvement candidate persistence under `product-breakdown/06-evolution/candidates/`
  - Established backlog infrastructure under `06-evolution/`
