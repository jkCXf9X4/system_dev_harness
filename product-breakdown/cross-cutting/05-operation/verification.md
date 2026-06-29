# Operation Verification

> **Note:** Per IMP-021, verification uses a dual pattern: the centralized Verification Strategy at `cross-cutting/04-verification/acceptance-criteria.md` is the authoritative index; per-layer artifacts are authoritative for their element. This artifact covers the Operation layer (`cross-cutting/05-operation/`).

This document extracts and scopes verification criteria for the Operation layer. It co-locates operational verification with the operational artifacts it verifies (`runbook.md`, `deployment-process.md`), following the INCOSE §1.3.5 horizontal-view model.

## Operation-Scoped Acceptance Criteria

The following criteria are extracted from the centralized acceptance criteria and from operational artifact requirements. Each entry cross-references the original source.

### Criterion AC-OPS-01: Stale references, duplicates, orphans reconciled before completion

| Property | Value |
|---|---|
| **Original Reference** | `product-breakdown/cross-cutting/04-verification/acceptance-criteria.md` — criterion 9 |
| **Scope** | `cross-cutting/05-operation/runbook.md` |
| **Description** | Stale references, status trackers, duplicates, superseded content, unresolved links, traceability, and orphaned artifacts must be reconciled before completion. |
| **Verification** | Confirm the completion checklist includes reconciliation of stale references, duplicates, superseded content, orphaned artifacts, unresolved links, and traceability. |

### Criterion AC-OPS-02: Workflow executable from target repository after payload copy

| Property | Value |
|---|---|
| **Original Reference** | `cross-cutting/05-operation/runbook.md` — Requirement 1 |
| **Scope** | `cross-cutting/05-operation/runbook.md` |
| **Description** | Operators must be able to run the workflow from a target repository after copying the runtime payload. |
| **Verification** | Confirm the runtime payload (opencode.json + .opencode/) is self-contained and that no additional repository-specific setup is required beyond the copy step. |

### Criterion AC-OPS-03: Blocked work preserves gate findings for planner re-scoping

| Property | Value |
|---|---|
| **Original Reference** | `cross-cutting/05-operation/runbook.md` — Requirement 2 |
| **Scope** | `cross-cutting/05-operation/runbook.md` |
| **Description** | Blocked work must preserve gate findings, stable gap identifiers, and the next required action for planner re-scoping. |
| **Verification** | Confirm blocked gate output includes findings, gap identifiers, and a next-action statement consumable by planner. |

### Criterion AC-OPS-04: Revision loops stop at configured cap or no-improvement signal

| Property | Value |
|---|---|
| **Original Reference** | `cross-cutting/05-operation/runbook.md` — Requirement 3 |
| **Scope** | `cross-cutting/05-operation/runbook.md` |
| **Description** | Revision loops must stop at the configured cap or no-improvement signal and return the decision to the human operator. |
| **Verification** | Confirm the workflow enforces a revision loop cap and that reaching the cap (or a no-improvement signal) returns control to the operator with a decision. |

### Criterion AC-OPS-05: Waiver handling exposes risk, scope, expiry, and user decision

| Property | Value |
|---|---|
| **Original Reference** | `cross-cutting/05-operation/runbook.md` — Requirement 4 |
| **Scope** | `cross-cutting/05-operation/runbook.md` |
| **Description** | Waiver handling must expose the named risk, waiver scope, follow-up or expiry condition, and user decision before completion. |
| **Verification** | Confirm waiver output includes named risk, waiver scope, follow-up/expiry condition, and requires explicit user decision. |

### Criterion AC-OPS-06: Stage feedback explicit when user input required

| Property | Value |
|---|---|
| **Original Reference** | `cross-cutting/05-operation/runbook.md` — Requirement 5 |
| **Scope** | `cross-cutting/05-operation/runbook.md` |
| **Description** | Stage feedback must be explicit when user input is required before continuing. |
| **Verification** | Confirm workflow stages that pause for user input produce explicit feedback indicating what is needed and why. |

### Criterion AC-OPS-07: Stage failures have conservative recovery path

| Property | Value |
|---|---|
| **Original Reference** | `cross-cutting/05-operation/runbook.md` — Requirement 6 |
| **Scope** | `cross-cutting/05-operation/runbook.md` |
| **Description** | Stage failures or unexpected output must have a conservative recovery path that preserves the guarded workflow contract. |
| **Verification** | Confirm the workflow defines a recovery path for each stage that maintains the guarded workflow integrity (no silent skips, no weakened gate). |

### Criterion AC-OPS-08: Deployable by copying opencode.json and .opencode/

| Property | Value |
|---|---|
| **Original Reference** | `cross-cutting/05-operation/deployment-process.md` — Requirement 1 |
| **Scope** | `cross-cutting/05-operation/deployment-process.md` |
| **Description** | The package must remain deployable by copying only `opencode.json` and `.opencode/` into a target development repository. |
| **Verification** | Confirm deployment instructions reference only `opencode.json` and `.opencode/` as the copy source. |

### Criterion AC-OPS-09: product-breakdown/ stays as source docs, not required at runtime

| Property | Value |
|---|---|
| **Original Reference** | `cross-cutting/05-operation/deployment-process.md` — Requirement 2 |
| **Scope** | `cross-cutting/05-operation/deployment-process.md` |
| **Description** | The package `product-breakdown/` tree must remain source documentation for this repository and must not be required at runtime in target repositories. |
| **Verification** | Confirm deployment excludes `product-breakdown/` from the runtime payload. Confirm workflow agents do not require `product-breakdown/` to be present in target repositories. |

### Criterion AC-OPS-10: Copied payload includes agent prompts, workflow policy, templates, and metadata

| Property | Value |
|---|---|
| **Original Reference** | `cross-cutting/05-operation/deployment-process.md` — Requirement 3 |
| **Scope** | `cross-cutting/05-operation/deployment-process.md` |
| **Description** | The copied payload must include the agent prompts, workflow policy, reusable prompt templates, product-breakdown guidance for agents, and package-local runtime dependency metadata needed by OpenCode. |
| **Verification** | Confirm the deployment payload contains agent prompt files, workflow policy files, reusable template files, agent-relevant product-breakdown guidance, and runtime dependency metadata. |

### Criterion AC-OPS-11: Refresh without overwriting repo-local workflow memory

| Property | Value |
|---|---|
| **Original Reference** | `cross-cutting/05-operation/deployment-process.md` — Requirement 4 |
| **Scope** | `cross-cutting/05-operation/deployment-process.md` |
| **Description** | Target repositories must be able to refresh the workflow payload from a newer package commit without overwriting repo-local workflow memory under `.opencode/dev_harness_memories/`. |
| **Verification** | Confirm the refresh process preserves `.opencode/dev_harness_memories/` content. Confirm the deployment payload does not include repo-local memory files. |

### Criterion AC-OPS-12: Deployment updates reviewable as ordinary diffs

| Property | Value |
|---|---|
| **Original Reference** | `cross-cutting/05-operation/deployment-process.md` — Requirement 5 |
| **Scope** | `cross-cutting/05-operation/deployment-process.md` |
| **Description** | Deployment updates should be reviewable as ordinary repository diffs in the target repository. |
| **Verification** | Confirm the deployment payload does not include generated, minified, or binary files that would prevent meaningful diff review. |

## Cross-Reference to Centralized Criteria and Source Artifacts

| Operation Criterion | Original Source |
|---|---|
| AC-OPS-01 | Centralized criterion 9 |
| AC-OPS-02 | runbook.md Requirement 1 |
| AC-OPS-03 | runbook.md Requirement 2 |
| AC-OPS-04 | runbook.md Requirement 3 |
| AC-OPS-05 | runbook.md Requirement 4 |
| AC-OPS-06 | runbook.md Requirement 5 |
| AC-OPS-07 | runbook.md Requirement 6 |
| AC-OPS-08 | deployment-process.md Requirement 1 |
| AC-OPS-09 | deployment-process.md Requirement 2 |
| AC-OPS-10 | deployment-process.md Requirement 3 |
| AC-OPS-11 | deployment-process.md Requirement 4 |
| AC-OPS-12 | deployment-process.md Requirement 5 |

## Relationship to Operation Layer

Per IMP-021, each PBS layer has its own local verification artifact. This file (`cross-cutting/05-operation/verification.md`) is the verification artifact for the Operation layer. It covers verification of runbook.md and deployment-process.md, ensuring operational requirements satisfy the centralized acceptance criteria scoped to this layer.

## Trace Links

- Feeds from: `product-breakdown/cross-cutting/04-verification/acceptance-criteria.md` (centralized criteria), `product-breakdown/cross-cutting/05-operation/runbook.md` (operational requirements), `product-breakdown/cross-cutting/05-operation/deployment-process.md` (deployment requirements)
- Informs: `product-breakdown/traceability-map.md`
- Satisfies: PC-006 (traceability and artifact lineage)
- Implements: IMP-021 (per-layer verification evolution)