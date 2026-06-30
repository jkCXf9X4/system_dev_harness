# Intent Verification

> **Note:** Per IMP-021, verification uses a dual pattern: the centralized Verification Strategy at `cross-cutting/04-verification/acceptance-criteria.md` is the authoritative index; per-layer artifacts are authoritative for their element. This artifact covers the Intent layer (`fbs/00-intent/`).

This document extracts and scopes the acceptance criteria from `system_definition/cross-cutting/04-verification/acceptance-criteria.md` that are relevant to the Intent layer. It co-locates intent verification with the intent artifacts it verifies (vision, use cases), following the INCOSE §1.3.5 horizontal-view model.

## Intent-Scoped Acceptance Criteria

The following criteria are extracted from the centralized acceptance criteria and scoped to the Intent layer. Each entry cross-references the original criterion.

### Criterion AC-INTENT-01: Every run produces planner-owned work order with verifiable checks

| Property | Value |
|---|---|
| **Original Reference** | `system_definition/cross-cutting/04-verification/acceptance-criteria.md` — criterion 1 |
| **Scope** | `fbs/00-intent/vision.md`, `.opencode/dev_harness/workflow/agent-boundaries.md` |
| **Description** | Every guarded workflow run must produce a planner-owned work order that contains verifiable checks. The work order defines what must be verified before the run is complete. |
| **Verification** | Confirm each completed run references a planner-owned work order with explicit verification criteria. |

### Criterion AC-INTENT-02: Every change independently reviewed before completion

| Property | Value |
|---|---|
| **Original Reference** | `system_definition/cross-cutting/04-verification/acceptance-criteria.md` — criterion 3 |
| **Scope** | `fbs/00-intent/vision.md`, `fbs/00-intent/use-cases.md` |
| **Description** | Every change must be independently reviewed before it is treated as complete. This applies to changes at all layers, including intent-layer artifacts. |
| **Verification** | Verify that the workflow includes an independent review stage between implementation and completion for all artifact changes. |

### Criterion AC-INTENT-03: Every run performs final reflection

| Property | Value |
|---|---|
| **Original Reference** | `system_definition/cross-cutting/04-verification/acceptance-criteria.md` — criterion 4 |
| **Scope** | `fbs/00-intent/vision.md` |
| **Description** | Every completed guarded workflow run must perform final reflection before reporting, so durable memory incorporation is explicitly accepted, rejected, deferred, or marked not applicable. |
| **Verification** | Confirm final reflection is a mandatory stage in the guarded workflow sequence. |

### Criterion AC-INTENT-04: Product source info stays in system_definition/

| Property | Value |
|---|---|
| **Original Reference** | `system_definition/cross-cutting/04-verification/acceptance-criteria.md` — criterion 15 |
| **Scope** | `fbs/00-intent/vision.md`, `fbs/00-intent/use-cases.md` |
| **Description** | Product source information, scope, stable decisions, and traceability must remain in `system_definition/`. Intent artifacts (vision, use cases) are product source and belong in this directory. |
| **Verification** | Confirm all intent-layer source documents reside under `system_definition/fbs/00-intent/`. No intent source information should be duplicated outside `system_definition/`. |

### Criterion AC-INTENT-05: Runnable guidance stays in docs/ without duplicating product text

| Property | Value |
|---|---|
| **Original Reference** | `system_definition/cross-cutting/04-verification/acceptance-criteria.md` — criterion 16 |
| **Scope** | `fbs/00-intent/vision.md`, `fbs/00-intent/use-cases.md` |
| **Description** | Runnable guidance, examples, install/deploy instructions, verification commands, and contributor workflow must remain in `docs/` without duplicating product text from the intent layer. |
| **Verification** | Confirm `docs/` does not duplicate content from `fbs/00-intent/` (it may reference it). Intent artifacts describe what and why; `docs/` describes how to use and run. |

## Cross-Reference to Centralized Criteria

| Intent Criterion | Centralized Criterion (cross-cutting/04-verification/acceptance-criteria.md) |
|---|---|
| AC-INTENT-01 | Criterion 1 |
| AC-INTENT-02 | Criterion 3 |
| AC-INTENT-03 | Criterion 4 |
| AC-INTENT-04 | Criterion 15 |
| AC-INTENT-05 | Criterion 16 |

## Relationship to FBS

Per IMP-021, each FBS layer should have its own local verification artifact. This file (`fbs/00-intent/verification.md`) is the verification artifact for the Intent layer. It covers verification of vision.md and use-cases.md, ensuring that intent-level artifacts satisfy the centralized acceptance criteria scoped to this layer.

## Trace Links

- Feeds from: `system_definition/cross-cutting/04-verification/acceptance-criteria.md` (centralized criteria)
- Informs: `system_definition/traceability-map.md`
- Satisfies: PC-006 (traceability and artifact lineage)
- Implements: IMP-021 (per-layer verification evolution)