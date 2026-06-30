# Project Management WBS

This document provides a project management Work Breakdown Structure (WBS) derived from the FBS-PBS-WBS mapping in `breakdown-structures.md`. It includes work packages, effort estimates, dependencies, and suggested sequencing.

> **Disclaimer:** This is a planning aid, not a commitment — not an authoritative schedule or budget document. Effort estimates are t-shirt sizes for relative comparison only. Actual effort depends on scope, complexity, and context at implementation time.

## Work Packages

| WP ID | Name | Description | Effort | Dependencies | Suggested Phase |
|-------|------|-------------|--------|--------------|-----------------|
| WP-01 | Request normalization pipeline | Implement F-01 (Request Normalization): transform rough instructions into concrete task shapes with execution order and agent routing | M | — | Phase 1 |
| WP-02 | Planner work order system | Implement F-02 (Work Order Creation): planner-owned contract with objective, scope, requirements, criteria, checklist, waiver rules | L | WP-01 | Phase 1 |
| WP-03 | Architecture preservation checks | Implement F-03 (Architecture Preservation) and F-11 (Design Quality Guarding): drift detection, modularity, simplicity, readability checks | M | WP-02 | Phase 2 |
| WP-04 | Mistake memory integration | Implement F-04 (Mistake Prevention): persistent known mistake checking before implementation; integrate with workflow memory | S | WP-02 | Phase 1 |
| WP-05 | Builder work order synthesis | Implement F-05 (Builder Work Order Production): generate strict builder instructions with step-by-step guidance | S | WP-02, WP-03, WP-04 | Phase 2 |
| WP-06 | Change implementation engine | Implement F-06 (Change Implementation): apply approved changes, coordinate helpers, collect evidence | L | WP-05 | Phase 2 |
| WP-07 | Implementation review system | Implement F-07 (Implementation Review): independent reviewer helpers, contract/architecture/mistake review | M | WP-06 | Phase 3 |
| WP-08 | Completion gate | Implement F-08 (Completion Decision): deterministic approved/blocked/waiver-required routing | S | WP-07 | Phase 3 |
| WP-09 | Lesson capture and memory curation | Implement F-09 (Lesson Capture): reflect on runs, extract durable lessons, persist to memory | S | WP-07, WP-08 | Phase 3 |
| WP-10 | Final control report | Implement F-10 (Final Control Report): summarize run state, evidence, and next actions | S | WP-08, WP-09 | Phase 3 |
| WP-11 | Candidate capture mode | Implement F-12 (Continuous Improvement): run guarded chain in candidate-capture mode, persist backlog | M | WP-02 through WP-10 | Phase 4 |
| WP-12 | Direct build execution | Implement F-13 (Direct Build Execution): operator escape hatch without weakening orchestrator guardrails | S | WP-02 | Phase 1 |
| WP-13 | Repository state review | Implement F-14 (Repository State Review): assess freshness, completeness, consistency, traceability | S | WP-02 | Phase 2 |
| WP-14 | Agent definition and prompting | PBS: Define orchestrator, planner, builder, reviewer, reflection, reporter agent prompts and roles | XL | — | Phase 1 |
| WP-15 | Product breakdown documentation | PBS: Write and maintain system_definition/ artifacts across all layers | L | WP-14 | Ongoing |
| WP-16 | Verification infrastructure | PBS: Acceptance criteria, test strategy, traceability matrix, per-layer verification | M | WP-01 through WP-13 | Phase 3 |
| WP-17 | Operation and deployment | PBS: Runbook, deployment process, operational requirements | S | WP-14 | Phase 4 |
| WP-18 | Evolution lifecycle management | PBS: Roadmap, candidates, selected, done, risks, changelog | S | WP-15 | Ongoing |
| WP-19 | Dev harness and workflow policy | PBS: .opencode/dev_harness/ maintenance, guidance updates, template improvements | M | WP-14 | Ongoing |
| WP-20 | Information hygiene and traceability | Cross-cutting: Stale reference cleanup, duplicate reconciliation, orphaned artifact removal, traceability maintenance | S | WP-15 | Ongoing |

## Effort Key

| Size | Approximate Relative Effort |
|------|---------------------------|
| S (Small) | Days to 1 week |
| M (Medium) | 1–3 weeks |
| L (Large) | 3–6 weeks |
| XL (Extra Large) | 6+ weeks or multi-phase |

## Dependency Graph

```
Phase 1 (Foundation)        Phase 2 (Core)           Phase 3 (Quality)        Phase 4 (Maturity)
────────────────────        ──────────────           ────────────────         ─────────────────
WP-01 (Normalization)       WP-03 (Architecture)     WP-07 (Review)           WP-11 (Candidate capture)
WP-02 (Work order)    ──▶   WP-05 (Builder order)    WP-08 (Gate)             WP-17 (Operation)
WP-04 (Mistakes)      ──▶   WP-06 (Implementation)   WP-09 (Lessons)          WP-18 (Evolution)
WP-12 (Direct build)        WP-13 (Repo review)      WP-10 (Report)
WP-14 (Agent defs)          WP-15 (Product docs)     WP-16 (Verification)
WP-19 (Dev harness)
WP-20 (Hygiene) [ongoing]
```

## Sequencing Notes

1. **Phase 1 (Foundation):** Agent definition (WP-14) and the core planning pipeline (WP-01, WP-02, WP-04, WP-12) establish the basic workflow. Dev harness and hygiene (WP-19, WP-20) are ongoing from the start.
2. **Phase 2 (Core):** Architecture preservation (WP-03), builder work (WP-05, WP-06), product documentation (WP-15), and repo review (WP-13) build on Phase 1.
3. **Phase 3 (Quality):** Review, gate, lessons, report, and verification (WP-07, WP-08, WP-09, WP-10, WP-16) add independent quality checks.
4. **Phase 4 (Maturity):** Candidate capture (WP-11), operation (WP-17), and evolution lifecycle management (WP-18) add continuous improvement capability.

## FBS/PBS/WBS Mapping

Each work package traces to its originating decomposition element:

| WP ID | Originates From | Decomposition Type |
|-------|-----------------|--------------------|
| WP-01 | F-01 (Request Normalization) | FBS → WBS |
| WP-02 | F-02 (Work Order Creation) | FBS → WBS |
| WP-03 | F-03 (Architecture Preservation), F-11 (Design Quality Guarding) | FBS → WBS |
| WP-04 | F-04 (Mistake Prevention) | FBS → WBS |
| WP-05 | F-05 (Builder Work Order Production) | FBS → WBS |
| WP-06 | F-06 (Change Implementation) | FBS → WBS |
| WP-07 | F-07 (Implementation Review) | FBS → WBS |
| WP-08 | F-08 (Completion Decision) | FBS → WBS |
| WP-09 | F-09 (Lesson Capture) | FBS → WBS |
| WP-10 | F-10 (Final Control Report) | FBS → WBS |
| WP-11 | F-12 (Continuous Improvement) | FBS → WBS |
| WP-12 | F-13 (Direct Build Execution) | FBS → WBS |
| WP-13 | F-14 (Repository State Review) | FBS → WBS |
| WP-14 | PBS: Agent hierarchy | PBS → WBS |
| WP-15 | PBS: Product breakdown layers | PBS → WBS |
| WP-16 | PBS: 04-verification/ layer | PBS → WBS |
| WP-17 | PBS: 05-operation/ layer | PBS → WBS |
| WP-18 | PBS: 06-evolution/ layer | PBS → WBS |
| WP-19 | PBS: .opencode/dev_harness/ | PBS → WBS |
| WP-20 | Cross-cutting: Information hygiene | PBS → WBS |

## Trace Links

- Feeds from: `system_definition/breakdown-structures.md` (WBS section), `system_definition/cross-cutting/06-evolution/breakdown-structures.md` (via IMP-016)
- Informs: Implementation planning for future work packages
- Satisfies: PC-006 (traceability and artifact lineage)
- Implements: IMP-019