# Evolution Verification

> **Note:** Per IMP-021, verification uses a dual pattern: the centralized Verification Strategy at `cross-cutting/04-verification/acceptance-criteria.md` is the authoritative index; per-layer artifacts are authoritative for their element. This artifact covers the Evolution layer (`cross-cutting/06-evolution/`).

This document extracts and scopes verification criteria for the Evolution layer. It co-locates evolution verification with the evolution artifacts it verifies (`roadmap.md`, `changelog.md`, `risks.md`, `gap-analysis.md`, `wbs.md`), following the INCOSE §1.3.5 horizontal-view model.

## Evolution-Scoped Acceptance Criteria

The following criteria are extracted from the centralized acceptance criteria and from evolution artifact requirements. Each entry cross-references the original source.

### Criterion AC-EVOL-01: Backlog persistence criteria applied to evolution artifacts

| Property | Value |
|---|---|
| **Original Reference** | `product-breakdown/cross-cutting/04-verification/acceptance-criteria.md` — criterion 11 (evolution-scoped) |
| **Scope** | `cross-cutting/06-evolution/roadmap.md`, `cross-cutting/06-evolution/candidates/` |
| **Description** | Backlog-worthy improvement candidates must be persisted to `product-breakdown/cross-cutting/06-evolution/candidates/` by builder candidate-capture mode. Evolution artifacts (roadmap, changelog, risks, gap analysis, WBS) must reference the candidate lifecycle correctly. |
| **Verification** | Confirm evolution artifacts reference the correct candidate storage path. Confirm the candidate lifecycle (candidates/ → selected/ → done/) is documented in evolution artifacts. |

### Criterion AC-EVOL-02: Candidate disposition criteria applied to candidate lifecycle

| Property | Value |
|---|---|
| **Original Reference** | `product-breakdown/cross-cutting/04-verification/acceptance-criteria.md` — criterion 12 (evolution-scoped) |
| **Scope** | `cross-cutting/06-evolution/roadmap.md`, `cross-cutting/06-evolution/` lifecycle |
| **Description** | Every deliberate candidate-capture run must receive a reviewed disposition (accepted candidate or no candidate) before final reporting. The evolution lifecycle must maintain this disposition review. |
| **Verification** | Confirm the evolution lifecycle documents the disposition review step. Confirm candidate files include disposition metadata. |

### Criterion AC-EVOL-03: Product source and runnable guidance boundaries maintained

| Property | Value |
|---|---|
| **Original Reference** | `cross-cutting/06-evolution/roadmap.md` — Current Focus |
| **Scope** | `cross-cutting/06-evolution/roadmap.md` |
| **Description** | Product source information and traceability must remain in `product-breakdown/` while runnable usage, install, verification, and contributor guidance remain in `docs/`. The evolution roadmap must track alignment between source and runtime payload. |
| **Verification** | Confirm roadmap.md references the product-breakdown/docs boundary. Confirm roadmap reflects ongoing alignment work between source product-breakdown tree, copied runtime payload, and agent prompts. |

### Criterion AC-EVOL-04: Changelog accuracy and traceability

| Property | Value |
|---|---|
| **Original Reference** | `cross-cutting/06-evolution/changelog.md` |
| **Scope** | `cross-cutting/06-evolution/changelog.md` |
| **Description** | Changelog entries must accurately reflect what changed, when, and in which implementation cycle. All changes must be traceable to a changelog entry with a dated, descriptive summary. |
| **Verification** | Confirm changelog.md contains dated entries with descriptive summaries. Verify that implementation changes are reflected in the changelog within a reasonable timeframe. |

### Criterion AC-EVOL-05: Risk register maintained with likelihood, impact, and mitigation

| Property | Value |
|---|---|
| **Original Reference** | `cross-cutting/06-evolution/risks.md` |
| **Scope** | `cross-cutting/06-evolution/risks.md` |
| **Description** | Known risks must be documented with likelihood, impact, and mitigation. The risk register must be reviewed for stale entries during the evolution lifecycle. |
| **Verification** | Confirm risks.md uses a consistent table format with likelihood, impact, and mitigation columns. Verify risks are reviewed periodically for continued relevance. |

### Criterion AC-EVOL-06: FBS-PBS gap analysis maintained and current

| Property | Value |
|---|---|
| **Original Reference** | `cross-cutting/06-evolution/gap-analysis.md` |
| **Scope** | `cross-cutting/06-evolution/gap-analysis.md` |
| **Description** | FBS-PBS gap analysis must be maintained and updated when new artifacts (FBS or PBS) are added, ensuring all functional and physical elements remain mutually traceable. |
| **Verification** | Confirm gap-analysis.md cross-references all current FBS elements (UCs, PCs) against PBS elements (agents, layers). Verify that adding a new FBS or PBS element triggers a gap analysis update. |

## Cross-Reference to Centralized Criteria and Source Artifacts

| Evolution Criterion | Original Source |
|---|---|
| AC-EVOL-01 | Centralized criterion 11 (evolution-scoped) |
| AC-EVOL-02 | Centralized criterion 12 (evolution-scoped) |
| AC-EVOL-03 | roadmap.md — Current Focus |
| AC-EVOL-04 | changelog.md — changelog practice |
| AC-EVOL-05 | risks.md — risk register format |
| AC-EVOL-06 | gap-analysis.md — gap analysis maintenance |

## Relationship to Evolution Layer

Per IMP-021, each PBS layer has its own local verification artifact. This file (`cross-cutting/06-evolution/verification.md`) is the verification artifact for the Evolution layer. It covers verification of roadmap.md, changelog.md, risks.md, gap-analysis.md, and wbs.md, ensuring evolution lifecycle artifacts satisfy the centralized acceptance criteria scoped to this layer.

## Trace Links

- Feeds from: `product-breakdown/cross-cutting/04-verification/acceptance-criteria.md` (centralized criteria), `product-breakdown/cross-cutting/06-evolution/roadmap.md`, `product-breakdown/cross-cutting/06-evolution/changelog.md`, `product-breakdown/cross-cutting/06-evolution/risks.md`, `product-breakdown/cross-cutting/06-evolution/gap-analysis.md`
- Informs: `product-breakdown/traceability-map.md`
- Satisfies: PC-006 (traceability and artifact lineage)
- Implements: IMP-021 (per-layer verification evolution)