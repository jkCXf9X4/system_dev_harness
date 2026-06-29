# FBS-PBS Gap Analysis

This document cross-references Functional Breakdown Structure (FBS) elements against Product Breakdown Structure (PBS) elements, identifies unmatched items, and proposes new artifacts for verified gaps.

## Status

- Analysis date: 2026-06-29
- Coverage: UC-001 through UC-014 (FBS), PC-001 through PC-010 (FBS), agent hierarchy (PBS), product-breakdown layers (PBS)
- Methodology: Manual cross-reference against current artifacts

## FBS → PBS: Use Cases

| UC ID | Description | Implementing PBS Elements | Status |
|-------|-------------|--------------------------|--------|
| UC-001 | Normalize A Request | Planner (orchestrator-planner.md), Discovery Helper (orchestrator-discovery.md) | MAPPED |
| UC-002 | Create A Planner-Owned Work Order | Planner (orchestrator-planner.md), Contract Helper (orchestrator-contract.md) | MAPPED |
| UC-003 | Preserve Architecture During Agentic Development | Planner → Architecture Helper (orchestrator-architecture.md) | MAPPED |
| UC-004 | Check Persistent Known Mistakes | Planner → Lessons Helper (orchestrator-lessons.md), Reflection, Memory Helper (orchestrator-memory.md) | MAPPED |
| UC-005 | Produce A Builder Work Order | Planner (work order synthesis stage) | MAPPED |
| UC-006 | Implement Changes | Builder (orchestrator-builder.md), Build Error Resolver, Cleanup Helper, Researcher | MAPPED |
| UC-007 | Review Implementation Evidence | Reviewer (orchestrator-reviewer.md), Verifier, Review: Architecture, Review: Completeness, Review: Lessons | MAPPED |
| UC-008 | Enforce Completion Decision | Reviewer → Completion Gate (deterministic routing) | MAPPED |
| UC-009 | Capture New Lessons | Reflection (orchestrator-reflection.md), Memory Curator (orchestrator-memory-curator.md) | MAPPED |
| UC-010 | Produce A Final Control Report | Reporter (orchestrator-reporter.md) | MAPPED |
| UC-011 | Guard Design Quality During Architecture Work | Planner → Architecture Helper (orchestrator-architecture.md) — modularity/simplicity/readability checks | MAPPED |
| UC-012 | Drive Continuous Codebase Improvement | Builder candidate-capture mode, Planner candidate routing, Reviewer gate, Reflection, Reporter | MAPPED |
| UC-013 | Use Direct Build Execution Outside The Guarded Orchestrator | OpenCode build agent (explicit operator selection) | MAPPED |
| UC-014 | Review Current Repository State | Planner, Reviewer, Verifier (repo-state review workflow mode) | MAPPED |

**Result:** All 14 UCs map to at least one PBS element. No unmatched FBS functions.

## FBS → PBS: Product Commitments

| PC ID | Description | Satisfying PBS Elements | Status |
|-------|-------------|------------------------|--------|
| PC-001 | Anchor to planner-owned work order | Planner (work order), Contract Helper | MAPPED |
| PC-002 | Make drift visible before completion | Architecture Helper, Reviewer, Review: Architecture, Completion Gate | MAPPED |
| PC-003 | Persistent mistake memory | Memory Helper, Memory Curator, Lessons Helper, Reflection | MAPPED |
| PC-004 | Separate execution from approval | Builder, Reviewer, Completion Gate | MAPPED |
| PC-005 | Block or waive incomplete work | Completion Gate, Reporter (waiver reporting) | MAPPED |
| PC-006 | Traceability and artifact lineage | All product-breakdown layers, product-tree.md, traceability-map.md, breakdown-structures.md, Reporter, Cleanup Helper | MAPPED |
| PC-007 | Express behavior through OpenCode agents | All .opencode/agents/*.md files, opencode.json | MAPPED |
| PC-008 | Evaluate modularity and simplicity | Architecture Helper (orchestrator-architecture.md), Review: Architecture | MAPPED |
| PC-009 | Candidate capture through guarded chain | Builder (candidate-capture mode), Planner, Reviewer, Reflection, Reporter | MAPPED |
| PC-010 | Preserve orchestrator guardrails | Orchestrator (routing only), Control Policy, Agent Boundaries | MAPPED |

**Result:** All 10 PCs map to at least one PBS element. No unmatched product commitments.

## PBS → FBS: Agents

| PBS Agent | Derives From FBS Element | Status |
|-----------|-------------------------|--------|
| Orchestrator (orchestrator.md) | F-08 (Completion Decision), routing for all functions | MAPPED |
| Planner (orchestrator-planner.md) | F-01, F-02, F-03, F-04, F-05, F-11 | MAPPED |
| Discovery Helper (orchestrator-discovery.md) | F-01 | MAPPED |
| Contract Helper (orchestrator-contract.md) | F-02 | MAPPED |
| Architecture Helper (orchestrator-architecture.md) | F-03, F-11 | MAPPED |
| Lessons Helper (orchestrator-lessons.md) | F-04 | MAPPED |
| Builder (orchestrator-builder.md) | F-06, F-12, F-13 | MAPPED |
| Build Error Resolver | F-06 (sub-function: error diagnosis) | MAPPED |
| Cleanup Helper (orchestrator-cleanup.md) | F-06 (sub-function: reference reconciliation) | MAPPED |
| Researcher Helper | F-06 (sub-function: external lookup) | MAPPED |
| Reviewer (orchestrator-reviewer.md) | F-07, F-08, F-14 | MAPPED |
| Verifier (orchestrator-verifier.md) | F-07 (sub-function: focused checking) | MAPPED |
| Review: Architecture | F-03, F-11 | MAPPED |
| Review: Completeness | F-07 (sub-function: contract audit) | MAPPED |
| Review: Lessons | F-04 (sub-function: mistake audit) | MAPPED |
| Completion Gate | F-08 | MAPPED |
| Reflection (orchestrator-reflection.md) | F-04, F-09 | MAPPED |
| Memory Curator (orchestrator-memory-curator.md) | F-09 | MAPPED |
| Memory Helper (orchestrator-memory.md) | F-04 (sub-function: read-only retrieval) | MAPPED |
| Reporter (orchestrator-reporter.md) | F-10 | MAPPED |

**Result:** All 20 PBS agents map to at least one FBS function. No unmatched agents.

## PBS → FBS: Product-Breakdown Layers

| PBS Layer | Derives From FBS Element | Status |
|-----------|-------------------------|--------|
| fbs/00-intent/ (vision, use cases) | All F-01 through F-14 (provides functional source) | MAPPED |
| fbs/01-product/ (product commitments) | All functions (provides requirement constraints) | MAPPED |
| pbs/02-architecture/ (architecture) | All functions (provides structural guidance) | MAPPED |
| pbs/03-implementation/ (implementation) | All functions (provides artifact mapping) | MAPPED |
| cross-cutting/04-verification/ | F-07, F-08, F-14 | MAPPED |
| cross-cutting/05-operation/ | All functions (satisfies non-functional requirements) | MAPPED |
| cross-cutting/06-evolution/ | F-12 (Continuous Improvement) | MAPPED |

**Result:** All PBS layers map to FBS elements. No unmatched layers.

## Unmatched Items

| Direction | Item | Severity | Notes |
|-----------|------|----------|-------|
| FBS → PBS | None | — | All UCs and PCs are mapped |
| PBS → FBS | None | — | All agents and layers are mapped |
| FBS → PBS | No dedicated "external interface" use case | Informational | External integrations (GitHub, APIs) are covered implicitly by researcher helper and agent prompts but not modeled as a separate UC |
| FBS → PBS | No dedicated "configuration management" use case | Informational | Configuration (opencode.json, .opencode/ config) is a PBS artifact without an explicit FBS function |
| PBS → FBS | No FBS function for "development environment setup" | Informational | This is a docs/ concern, not a product-breakdown concern |

## Verified Gaps

After analysis, all FBS and PBS elements are mutually traceable. No critical or warning-level gaps were found.

### Informational Observations

1. **External Interface Management:** The SoI has implicit external dependencies (researcher helper fetches URLs, GitHub integration for PRs). These are covered by existing agent behavior but not modeled as explicit FBS functions. Consider a future UC-015 "Manage External Interfaces" if external integrations grow.

2. **Configuration Lifecycle:** `opencode.json` and `.opencode/` configuration is managed as a PBS artifact. No FBS function explicitly models configuration change management. This is acceptable because configuration is an implementation concern rather than a functional requirement.

3. **No-Capture Rationale:** The absence of critical or warning-level gaps is expected given the maturity of the FBS-PBS mapping. The system has been through multiple IMP cycles (IMP-012 through IMP-016) that explicitly built out the decomposition model, and the current cross-reference confirms completeness.

## Proposed New Artifacts

No new use cases, product commitments, or PBS artifacts are needed at this time. The informational observations above can be revisited if:

1. External integrations expand beyond the current researcher-helper pattern
2. Configuration management becomes a first-class workflow concern with versioning or audit requirements

## Trace Links

- Feeds from: `product-breakdown/fbs/00-intent/use-cases.md` (UC-001 through UC-014), `product-breakdown/fbs/01-product/product-commitments.md` (PC-001 through PC-010), `product-breakdown/breakdown-structures.md` (FBS/PBS mapping), `product-breakdown/pbs/02-architecture/architecture.md` (agent hierarchy)
- Informs: `product-breakdown/traceability-map.md` (trace chain completeness)
- Satisfies: PC-006 (traceability and artifact lineage)
- Implements: IMP-020