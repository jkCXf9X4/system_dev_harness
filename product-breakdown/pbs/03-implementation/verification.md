# Implementation Verification

> **Note:** Per IMP-021, verification uses a dual pattern: the centralized Verification Strategy at `cross-cutting/04-verification/acceptance-criteria.md` is the authoritative index; per-layer artifacts are authoritative for their element. This artifact covers the Implementation layer (`pbs/03-implementation/`).

This document extracts and scopes the acceptance criteria from `product-breakdown/cross-cutting/04-verification/acceptance-criteria.md` that are relevant to the Implementation layer. It co-locates implementation verification with the implementation artifacts it verifies, following the INCOSE §1.3.5 horizontal-view model.

## Implementation-Scoped Acceptance Criteria

The following criteria are extracted from the centralized acceptance criteria and scoped to the Implementation layer. Each entry cross-references the original criterion.

### Criterion AC-IMPL-01: Planner/reviewer identify parallel-safe helper packets

| Property | Value |
|---|---|
| **Original Reference** | `product-breakdown/cross-cutting/04-verification/acceptance-criteria.md` — criterion 2 |
| **Scope** | `pbs/03-implementation/implementation.md` |
| **Description** | Planner and reviewer stages must identify parallel-safe helper packets for independent helper work and preserve dependencies, expected outputs, and file write sets. |
| **Verification** | Confirm planner and reviewer prompts include instructions for identifying parallel-safe work packets. Verify that helper handoffs include dependency metadata, expected outputs, and file write sets. |

### Criterion AC-IMPL-02: Reviewer findings are actionable (blocked → planner)

| Property | Value |
|---|---|
| **Original Reference** | `product-breakdown/cross-cutting/04-verification/acceptance-criteria.md` — criterion 8 |
| **Scope** | `pbs/03-implementation/implementation.md` |
| **Description** | Reviewer findings must be actionable. Blocked findings must route back to planner per the revision loop. |
| **Verification** | Confirm the reviewer prompt produces findings that include specific required actions. Verify blocked findings are routed back to planner through the revision loop. |

### Criterion AC-IMPL-03: Repo-state review tasks produce updates or reviewed no-change result

| Property | Value |
|---|---|
| **Original Reference** | `product-breakdown/cross-cutting/04-verification/acceptance-criteria.md` — criterion 10 |
| **Scope** | `pbs/03-implementation/implementation.md` |
| **Description** | Repo-state review tasks must either produce trace-preserving updates or a reviewed no-change/backlog result that records stale, duplicated, conflicting, or orphaned findings. |
| **Verification** | Confirm repo-state review mode records its findings (either updates applied or no-change result with orphaned/conflicting/duplicate entries documented). |

## Cross-Reference to Centralized Criteria

| Implementation Criterion | Centralized Criterion (cross-cutting/04-verification/acceptance-criteria.md) |
|---|---|
| AC-IMPL-01 | Criterion 2 |
| AC-IMPL-02 | Criterion 8 |
| AC-IMPL-03 | Criterion 10 |

## Relationship to PBS

Per IMP-021, each PBS layer should have its own local verification artifact. This file (`pbs/03-implementation/verification.md`) is the verification artifact for the Implementation layer. It covers verification of implementation.md and the associated implementation artifact set.

## Trace Links

- Feeds from: `product-breakdown/cross-cutting/04-verification/acceptance-criteria.md` (centralized criteria)
- Informs: `product-breakdown/traceability-map.md`
- Satisfies: PC-006 (traceability and artifact lineage)
- Implements: IMP-021 (per-layer verification evolution)