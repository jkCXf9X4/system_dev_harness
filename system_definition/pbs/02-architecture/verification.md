# Architecture Verification

> **Note:** Per IMP-021, verification uses a dual pattern: the centralized Verification Strategy at `cross-cutting/04-verification/acceptance-criteria.md` is the authoritative index; per-layer artifacts are authoritative for their element. This artifact was the pilot per IMP-013.

This document extracts and refines the acceptance criteria from `system_definition/cross-cutting/04-verification/acceptance-criteria.md` that are scoped to the architecture layer (`pbs/02-architecture/`). It co-locates architecture verification with the architecture it verifies, following the INCOSE §1.3.5 horizontal-view model.

## Architecture-Scoped Acceptance Criteria

The following criteria are extracted from the centralized acceptance criteria and scoped to the architecture layer. Each entry cross-references the original criterion.

### Criterion AC-ARCH-01: Architecture boundaries preserve agent roles

| Property | Value |
|---|---|
| **Original Reference** | `system_definition/cross-cutting/04-verification/acceptance-criteria.md` — criterion 1 (work order), criterion 7 (actionable findings) |
| **Scope** | `pbs/02-architecture/architecture.md`, `.opencode/dev_harness/workflow/agent-boundaries.md` |
| **Description** | The architecture documentation must define clear read/write/edit boundaries for each agent role. Every top-level stage (orchestrator, planner, builder, reviewer, reflection, reporter) must have a documented scope of responsibility and a list of agents or artifacts it may and may not modify. |
| **Verification** | Cross-reference each agent's documented boundaries against its prompt file permissions. No agent should be documented as having permission to perform work outside its stated scope. |

### Criterion AC-ARCH-02: Control flow is inspectable without hidden runtime

| Property | Value |
|---|---|
| **Original Reference** | `system_definition/cross-cutting/04-verification/acceptance-criteria.md` — criterion 1 (work order), criterion 13 (information hygiene) |
| **Scope** | `pbs/02-architecture/architecture.md` |
| **Description** | The architecture must express the guarded workflow control flow (task intake → orchestrator → planner → builder → reviewer → reflection → reporter) as a static, inspectable diagram or text flow. There must be no hidden Python runtime that controls stage routing. |
| **Verification** | Confirm the architecture document contains an explicit control-flow diagram or text flow. Verify that gate routing (approved, blocked, waiver-required) is documented without reference to runtime code. |

### Criterion AC-ARCH-03: Verification is a per-level horizontal view

| Property | Value |
|---|---|
| **Original Reference** | `system_definition/cross-cutting/04-verification/acceptance-criteria.md` — criterion 11 (candidate capture) |
| **Scope** | `pbs/02-architecture/architecture.md`, `system_definition/pbs/02-architecture/verification.md` (this file) |
| **Description** | The architecture should support verification as a horizontal view at each PBS decomposition level. The centralized verification layer (`cross-cutting/04-verification/`) may serve as a cross-cutting view, but each PBS layer should have its own local verification artifact. |
| **Verification** | Confirm that at least one PBS layer (e.g., `pbs/02-architecture/`) has a local verification artifact. Verify that the centralized verification criteria remain intact and authoritative. |

### Criterion AC-ARCH-04: Architecture guardrails include design quality

| Property | Value |
|---|---|
| **Original Reference** | `system_definition/cross-cutting/04-verification/acceptance-criteria.md` — criterion 7 (actionable findings) |
| **Scope** | `pbs/02-architecture/architecture.md` |
| **Description** | Architecture guardrails must cover modularity, simplicity, readability, and module responsibility fit — not only preservation of the current shape. The architecture document must state these as explicit concerns during architecture review. |
| **Verification** | Search `pbs/02-architecture/architecture.md` for explicit mentions of modularity, simplicity, readability, and module responsibility. Confirm each is stated as an architecture guardrail. |

### Criterion AC-ARCH-05: Mechanism storage boundaries are explicit

| Property | Value |
|---|---|
| **Original Reference** | `system_definition/cross-cutting/04-verification/acceptance-criteria.md` — criterion 11 (system-definition storage), criterion 13 (stale references) |
| **Scope** | `pbs/02-architecture/architecture.md`, `pbs/03-implementation/implementation.md` |
| **Description** | The architecture must define canonical storage mechanisms for each information type: product rationale, runtime prompts, dev harness context, workflow memory, improvement backlog items, task-local evidence, skills/plugins, and external research. Each mechanism must document what it stores and what it does not store. |
| **Verification** | Review `pbs/02-architecture/architecture.md` — Persistence And Context Mechanisms section. Confirm each mechanism has a documented canonical location, stored types, and excluded types. |

### Criterion AC-ARCH-06: Completion evidence covers information hygiene

| Property | Value |
|---|---|
| **Original Reference** | `system_definition/cross-cutting/04-verification/acceptance-criteria.md` — criterion 13 (stale references) |
| **Scope** | `pbs/02-architecture/architecture.md`, `.opencode/dev_harness/workflow/information-hygiene.md` |
| **Description** | The architecture must require that completion evidence covers stale-reference cleanup, status tracker updates, duplicate-content reconciliation, orphaned-artifact handling, and traceability for changed information artifacts. |
| **Verification** | Confirm `pbs/02-architecture/architecture.md` states information hygiene as a completion-evidence requirement. Cross-reference with `.opencode/dev_harness/workflow/information-hygiene.md` for detailed rules. |

## Cross-Reference to Centralized Criteria

| Architecture Criterion | Centralized Criterion (cross-cutting/04-verification/acceptance-criteria.md) |
|---|---|
| AC-ARCH-01 | Criteria 1, 7 |
| AC-ARCH-02 | Criteria 1, 13 |
| AC-ARCH-03 | Criterion 11 |
| AC-ARCH-04 | Criterion 7 |
| AC-ARCH-05 | Criteria 11, 13 |
| AC-ARCH-06 | Criterion 13 |

## Relationship to PBS

Per IMP-021, the following verification artifacts have been created:

- `fbs/00-intent/verification.md` — verification criteria for intent docs
- `fbs/01-product/verification.md` — verification criteria for product commitments
- `pbs/02-architecture/verification.md` — this pilot artifact
- `pbs/03-implementation/verification.md` — verification criteria for implementation artifacts
- `cross-cutting/05-operation/verification.md` — verification criteria for operational requirements
- `cross-cutting/06-evolution/verification.md` — verification criteria for evolution lifecycle

The centralized `cross-cutting/04-verification/acceptance-criteria.md` remains the authoritative source and cross-cutting view.

## Trace Links

- Feeds from: `system_definition/cross-cutting/04-verification/acceptance-criteria.md` (centralized criteria), `system_definition/pbs/02-architecture/architecture.md` (architecture boundaries)
- Informs: `system_definition/traceability-map.md`
- Satisfies: PC-006 (traceability and artifact lineage)
- Implements: IMP-013 (pilot horizontal verification artifact)