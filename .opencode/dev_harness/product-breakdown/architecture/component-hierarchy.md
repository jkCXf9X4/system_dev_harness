# Component Hierarchy

> **Runtime reference copy for agent context.** Canonical source: `product-breakdown/breakdown-structures.md`.
> **External references:** This file adapts PBS (Product Breakdown Structure) and FBS (Function Breakdown Structure) concepts from the INCOSE Systems Engineering Handbook for analytical use within this workflow. Descriptions are original summaries.

## PBS Agent Hierarchy

The agent hierarchy from the canonical breakdown-structures.md:

```
system_dev_harness [PBS Root]
 |
 +-- Orchestrator [Physical: Router]
 |    +-- Planner [Physical: Work order owner]
 |    |    +-- Discovery Helper [Physical: File finder]
 |    |    +-- Contract Helper [Physical: Requirements writer]
 |    |    +-- Architecture Helper [Physical: Guardrail extractor]
 |    |    +-- Lessons Helper [Physical: Mistake checker]
 |    |
 |    +-- Builder [Physical: Implementation agent]
 |    |    +-- Build Error Resolver [Physical: Diagnostic fixer]
 |    |    +-- Cleanup Helper [Physical: Reference reconciler]
 |    |    +-- Researcher Helper [Physical: External lookup]
 |    |
 |    +-- Reviewer [Physical: Verification coordinator]
 |    |    +-- Verifier [Physical: Focused checker]
 |    |    +-- Review: Architecture [Physical: Architecture auditor]
 |    |    +-- Review: Completeness [Physical: Contract auditor]
 |    |    +-- Review: Lessons [Physical: Mistake auditor]
 |    |    +-- Completion Gate [Physical: Decision router]
 |    |
 |    +-- Reflection [Physical: Memory triage agent]
 |    |    +-- Memory Curator [Physical: Memory writer]
 |    |
 |    +-- Reporter [Physical: Output summarizer]
 |
 +-- Memory System [Physical: Workflow memory]
 |    +-- Memory Helper [Physical: Read-only retriever]
 |    +-- Memory Files (lessons.md, patterns.md) [Physical: Storage]
 |
 +-- Product Breakdown [Physical: Source documentation]
        +-- FBS Grouping [Physical: fbs/]
        |    +-- Intent Layer [Physical: fbs/00-intent/]
        |    |    +-- verification.md [Physical: Intent verification]
        |    +-- Product Layer [Physical: fbs/01-product/]
        |         +-- verification.md [Physical: Product verification]
        +-- PBS Grouping [Physical: pbs/]
        |    +-- Architecture Layer [Physical: pbs/02-architecture/]
        |    |    +-- verification.md [Physical: Architecture verification]
        |    +-- Implementation Layer [Physical: pbs/03-implementation/]
        |         +-- verification.md [Physical: Implementation verification]
        +-- Cross-Cutting Grouping [Physical: cross-cutting/]
             +-- Verification Layer [Physical: cross-cutting/04-verification/]
             +-- Operation Layer [Physical: cross-cutting/05-operation/]
             |    +-- verification.md [Physical: Operation verification]
             +-- Evolution Layer [Physical: cross-cutting/06-evolution/]
             |    +-- verification.md [Physical: Evolution verification]
             +-- Root Artifacts [Physical: Root files]
```

## FBS Top-Level Functions

The function breakdown from the canonical breakdown-structures.md:

| Function ID | Function Name | Description |
|---|---|---|
| F-01 | Request Normalization | Transform a rough instruction into a concrete, normalized task shape. |
| F-02 | Work Order Creation | Produce a binding, checklistable planner-owned work order with objective, scope, requirements, verification criteria, and waiver rules. |
| F-03 | Architecture Preservation | Keep implementation work aligned with current architecture, module boundaries, and approved patterns. |
| F-04 | Mistake Prevention | Check persistent known mistakes before implementation to prevent repeated errors. |
| F-05 | Builder Work Order Production | Generate strict builder instructions with step-by-step guidance, tests, and definition of done. |
| F-06 | Change Implementation | Apply approved changes and collect implementation evidence. |
| F-07 | Implementation Review | Get independent support-agent feedback before treating work as complete. |
| F-08 | Completion Decision | Decide whether a task is approved, blocked, or requires waivers. |
| F-09 | Lesson Capture | Update persistent mistake memory after completed or corrected tasks. |
| F-10 | Final Control Report | Summarize the run in a concise, reviewable report. |
| F-11 | Design Quality Guarding | Actively evaluate modularity, simplicity, readability, and module responsibility during architecture work. |
| F-12 | Continuous Improvement | Run candidate-capture mode to identify and persist backlog improvement candidates. |
| F-13 | Direct Build Execution | Allow operator-chosen build execution outside the guarded orchestrator path. |
| F-14 | Repository State Review | Assess current repository state for freshness, completeness, consistency, and traceability. |

## PBS-FBS Cross-Reference

Which PBS nodes implement which FBS functions:

| PBS Node | Implements FBS Function |
|---|---|
| Orchestrator | F-08 (Completion Decision), routing for all functions |
| Planner | F-01 (Request Normalization), F-02 (Work Order Creation), F-03 (Architecture Preservation), F-04 (Mistake Prevention), F-05 (Builder Work Order Production), F-11 (Design Quality Guarding) |
| Builder | F-06 (Change Implementation), F-12 (Continuous Improvement), F-13 (Direct Build Execution) |
| Reviewer + Verifier + Review Helpers | F-07 (Implementation Review), F-08 (Completion Decision), F-14 (Repository State Review) |
| Reflection + Memory Curator | F-04 (Mistake Prevention), F-09 (Lesson Capture) |
| Reporter | F-10 (Final Control Report) |
| Intent Layer (fbs/00-intent/) | F-01 through F-14 (provides functional source) |
| Product Layer (fbs/01-product/) | All functions (provides requirement constraints) |
| Architecture Layer (pbs/02-architecture/) | All functions (provides structural guidance) |
| Implementation Layer (pbs/03-implementation/) | All functions (provides artifact mapping) |
| Verification Layer (cross-cutting/04-verification/) | F-07, F-08, F-14 |
| Evolution Layer (cross-cutting/06-evolution/) | F-12 (Continuous Improvement) |

## Trace Links

- Canonical source: `product-breakdown/breakdown-structures.md`
- Related artifacts: `architecture/interface-contracts.md` (agents documented here appear in interface tables), `architecture/agent-state-machines.md` (agent states documented here)