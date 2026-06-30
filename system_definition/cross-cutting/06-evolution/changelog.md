# Changelog

## 2026-06-30 — IMD-005: Rename product-breakdown/ to system_definition/

- Renamed `product-breakdown/` → `system_definition/` (canonical source tree)
- Renamed `.opencode/dev_harness/product-breakdown/` → `.opencode/dev_harness/systems_engineering/` (runtime agent context)
- Renamed `docs/product-breakdown.md` → `docs/system-definition.md`
- Updated all internal cross-references across ~73 files
- Preserved `product-breakdown-work.md` filename and `touches_product_breakdown` control flag
- Created IMD-005 decision record and IMP-033 SE traceability evaluation

## 2026-06-05

- Added UC-014 to cover repository-state review as a first-class workflow task that can route into delivery or candidate capture.
- Consolidated candidate capture into the guarded planner -> builder -> reviewer -> reflection -> reporter chain using `workflow_mode: candidate_capture`.
- Removed standalone improvement/evaluator agent ownership from the guarded workflow; builder now owns candidate persistence in candidate-capture mode.
- Moved detailed candidate-capture rules into `.opencode/dev_harness/workflow/candidate-capture.md` so agents can load the policy only when relevant.
- Split helper-trigger, parallel-helper, and workflow-memory rules out of `control-policy.md` into focused load-on-demand workflow policy files.
- Extracted common stage output schema, agent read/write boundaries, and system-definition work rules into focused workflow policy files.

## 2026-06-29

- Added explicit workflow tailoring profiles (`lightweight`, `standard`, `high_assurance`) and a required `tailoring_record` so planner work orders record how the process was adapted for task risk and context.
- Updated the planner and reporter prompts so tailoring choices are captured in the work order and summarized in the final control report.
- Added product-layer and implementation-layer verification criteria for tailoring-record preservation.

## 2026-06-29 — IMP-032: Product-Breakdown Alignment Review

- Implemented 7 task seeds from IMP-032:
  - Seed 1: Created `pbs/02-architecture/interface-contracts.md` — IBD-adapted handoff tables for all agent-to-agent interfaces
  - Seed 2: Created `pbs/02-architecture/agent-state-machines.md` — State/transition tables for 4 top-level agents
  - Seed 3: Added validation criteria (VAL-001 through VAL-005) to `cross-cutting/04-verification/acceptance-criteria.md`
  - Seed 4: Created 9 decision records: PD-001/002/003, VD-001/002/003, OD-001/002/003; updated decision-log.md
  - Seed 5: Copyright remediation — replaced direct ISO/IEC 15288 quotes in IMP-026/027/028/030 with paraphrased descriptions; added attribution boilerplate to system_definition/README.md
  - Seed 6: Structural cleanup — moved IMP-031 from done/ to selected/, added IMP prefix to naming.md, moved IMD files to decisions/, created evaluations/, documented missing files in 06-evolution/README.md, updated stale references
  - Seed 7: Created `pbs/02-architecture/sequence-parametric.md` — sequence tables and parametric constraints
- Expanded scope: Agent prompt updates (planner, reviewer, systems-engineering); directory restructuring (decisions/ dirs, evaluations/)
- Updated index, traceability, and cross-references (product-tree.md, traceability-map.md, decision-log.md, 02-architecture/README.md, 04-verification/README.md, changelog.md)
- Candidate IMP-032 status updated from Proposed to In Progress

## 2026-06-02

- Added disk-backed focused improvement dispositions: accepted findings remain candidates, while rejected or needs-more-evidence suggestions are recorded under `system_definition/cross-cutting/06-evolution/evaluations/`.
- Added planner and reviewer parallel helper packet guidance so independent planning and review helpers can run concurrently when their dependencies allow it.

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

- Refreshed the source system-definition docs to match the current agent set and the backlog-oriented evolution layer.
- Added UC-013 for direct operator-chosen build work and ED-001 for the canonical evolution candidate location.
- Replaced the verification traceability stub with a concrete matrix tied to the current smoke and review coverage.
- Updated the source traceability map and operator-facing evolution docs to include the evolution/candidates path.

## 2026-05-20

- Implemented IMP-001 through IMP-009 improvements:
  - Renamed docs directories to match system-definition template numbering
  - Distributed ADR files into per-layer `decisions/` directories with prefixed IDs
  - Created verification layer (`04-verification/`) and operation layer (`05-operation/`)
  - Added root `decision-log.md` and `traceability-map.md`
  - Added revision loop to guarded workflow (blocked gate → planner re-scoping)
  - Added improvement candidate persistence under `system_definition/cross-cutting/06-evolution/candidates/`
  - Established backlog infrastructure under `06-evolution/`
