# Product Verification

> **Note:** Per IMP-021, verification uses a dual pattern: the centralized Verification Strategy at `cross-cutting/04-verification/acceptance-criteria.md` is the authoritative index; per-layer artifacts are authoritative for their element. This artifact covers the Product layer (`fbs/01-product/`).

This document extracts and scopes the acceptance criteria from `product-breakdown/cross-cutting/04-verification/acceptance-criteria.md` that are relevant to the Product layer. It co-locates product verification with the product commitments it verifies (PC-001 through PC-010), following the INCOSE §1.3.5 horizontal-view model.

## Product-Scoped Acceptance Criteria

The following criteria are extracted from the centralized acceptance criteria and scoped to the Product layer. Each entry cross-references the original criterion.

### Criterion AC-PRODUCT-01: Workflow memory includes trust metadata, revalidation cues, and boundary

| Property | Value |
|---|---|
| **Original Reference** | `product-breakdown/cross-cutting/04-verification/acceptance-criteria.md` — criterion 5 |
| **Scope** | `fbs/01-product/product-commitments.md` (PC-003) |
| **Description** | Workflow memory must include trust metadata, revalidation cues, and an explicit boundary between durable memory, task-local evidence, run history, and improvement backlog items. |
| **Verification** | Confirm `.opencode/dev_harness_memories/` contains trust metadata and revalidation cues. Verify that durable memory, task-local evidence, run history, and backlog items are stored in distinct locations. |

### Criterion AC-PRODUCT-02: Memory curation reports decision taxonomy; review/report surface hygiene

| Property | Value |
|---|---|
| **Original Reference** | `product-breakdown/cross-cutting/04-verification/acceptance-criteria.md` — criterion 6 |
| **Scope** | `fbs/01-product/product-commitments.md` (PC-003) |
| **Description** | Memory curation must report a concrete decision taxonomy, and review/report outputs must surface memory hygiene whenever memory influenced the task. |
| **Verification** | Confirm memory curator output includes a concrete decision taxonomy. Verify that review or report outputs include memory hygiene information when memory was used. |

### Criterion AC-PRODUCT-03: Product-breakdown docs define canonical storage mechanisms

| Property | Value |
|---|---|
| **Original Reference** | `product-breakdown/cross-cutting/04-verification/acceptance-criteria.md` — criterion 7 |
| **Scope** | `fbs/01-product/product-commitments.md` (PC-006) |
| **Description** | Product-breakdown source docs must define the canonical storage mechanism for product rationale, runtime prompts, dev harness context, workflow memory, improvement backlog items, task-local evidence, skills/plugins, and external research. |
| **Verification** | Confirm `product-breakdown/` documents specify where each information type is stored. Verify each mechanism documents what it stores and what it does not store. |

### Criterion AC-PRODUCT-04: Backlog candidates persisted to 06-evolution/candidates/ by builder

| Property | Value |
|---|---|
| **Original Reference** | `product-breakdown/cross-cutting/04-verification/acceptance-criteria.md` — criterion 11 |
| **Scope** | `fbs/01-product/product-commitments.md` (PC-009) |
| **Description** | Backlog-worthy improvement candidates must be persisted to `product-breakdown/cross-cutting/06-evolution/candidates/` by builder candidate-capture mode before the builder returns, without changing implementation files. |
| **Verification** | Confirm builder candidate-capture mode writes candidate files to `06-evolution/candidates/`. Verify implementation files are not modified during candidate persistence. |

### Criterion AC-PRODUCT-05: Each candidate-capture run receives reviewed disposition

| Property | Value |
|---|---|
| **Original Reference** | `product-breakdown/cross-cutting/04-verification/acceptance-criteria.md` — criterion 12 |
| **Scope** | `fbs/01-product/product-commitments.md` (PC-009) |
| **Description** | Every deliberate candidate-capture run must receive a reviewed disposition before final reporting: accepted candidate or no candidate. |
| **Verification** | Confirm the guarded workflow includes a review gate for candidate-capture mode that produces a disposition (accepted or no candidate) before reporting. |

### Criterion AC-PRODUCT-06: Bug/fix/feature subjects use workflow_mode: candidate_capture

| Property | Value |
|---|---|
| **Original Reference** | `product-breakdown/cross-cutting/04-verification/acceptance-criteria.md` — criterion 13 |
| **Scope** | `fbs/01-product/product-commitments.md` (PC-009) |
| **Description** | Bug, fix, regression, feature, and documentation subjects must use `workflow_mode: candidate_capture` when the user asks for proposal, evaluation, candidate, future-task-seed, or backlog capture instead of implementation. |
| **Verification** | Confirm the workflow policy defines `workflow_mode: candidate_capture` routing for proposal/evaluation/candidate/future-task-seed/backlog-capture requests in the specified subject areas. |

### Criterion AC-PRODUCT-07: Agents surface incidental candidates; deliberate requires candidate-capture

| Property | Value |
|---|---|
| **Original Reference** | `product-breakdown/cross-cutting/04-verification/acceptance-criteria.md` — criterion 14 |
| **Scope** | `fbs/01-product/product-commitments.md` (PC-009) |
| **Description** | Working agents can surface incidental improvement candidates without persisting them; deliberate persistence requires a candidate-capture work order. |
| **Verification** | Confirm agents may mention candidates without persisting them. Confirm candidate-capture mode is required for disk persistence. |

### Criterion AC-PRODUCT-08: Review-only uses candidate_capture; review-and-change uses delivery

| Property | Value |
|---|---|
| **Original Reference** | `product-breakdown/cross-cutting/04-verification/acceptance-criteria.md` — criterion 17 |
| **Scope** | `fbs/01-product/product-commitments.md` (PC-006, PC-009) |
| **Description** | Review-only repo-state assessment requests must use `workflow_mode: candidate_capture`; review-and-change requests must use `workflow_mode: delivery`. |
| **Verification** | Confirm the workflow routes review-only requests to candidate-capture mode and review-and-change requests to delivery mode. |

### Criterion AC-PRODUCT-09: Workflow tailoring records are preserved in work orders and reports

| Property | Value |
|---|---|
| **Original Reference** | `product-breakdown/cross-cutting/04-verification/acceptance-criteria.md` — criterion 18 |
| **Scope** | `fbs/01-product/product-commitments.md` (PC-001, PC-004, PC-006, PC-008) |
| **Description** | Planner work orders and final reports must preserve a task-tailoring record with the selected workflow profile, applied triggers, helper or stage deviations, and rationale so task-specific process adaptation is auditable. |
| **Verification** | Confirm planner outputs a `tailoring_record` section. Verify reporter output summarizes the tailored profile and rationale from the plan summary. |

## Cross-Reference to Centralized Criteria

| Product Criterion | Centralized Criterion (cross-cutting/04-verification/acceptance-criteria.md) |
|---|---|
| AC-PRODUCT-01 | Criterion 5 |
| AC-PRODUCT-02 | Criterion 6 |
| AC-PRODUCT-03 | Criterion 7 |
| AC-PRODUCT-04 | Criterion 11 |
| AC-PRODUCT-05 | Criterion 12 |
| AC-PRODUCT-06 | Criterion 13 |
| AC-PRODUCT-07 | Criterion 14 |
| AC-PRODUCT-08 | Criterion 17 |
| AC-PRODUCT-09 | Criterion 18 |

## Relationship to FBS

Per IMP-021, each FBS layer has its own local verification artifact. This file (`fbs/01-product/verification.md`) is the verification artifact for the Product layer. It covers verification of product-commitments.md (PC-001 through PC-010), ensuring that product-level requirements satisfy the centralized acceptance criteria scoped to this layer.

## Trace Links

- Feeds from: `product-breakdown/cross-cutting/04-verification/acceptance-criteria.md` (centralized criteria)
- Informs: `product-breakdown/traceability-map.md`
- Satisfies: PC-006 (traceability and artifact lineage)
- Implements: IMP-021 (per-layer verification evolution)
