# Traceability Map

This map documents the cross-layer traceability chain for the workflow package. Each capability traces from intent through product commitments, architecture, decisions, implementation, verification, operation, and evolution.

## Core Trace Chain

```
Vision.md (fbs/00-intent)
  -> Product Commitments PC-001 through PC-010 (fbs/01-product)
    -> Use Cases UC-001 through UC-014 (fbs/00-intent)
  -> Architecture (pbs/02-architecture)
        -> Decisions AD-001 through AD-005 (pbs/02-architecture/decisions/)
        -> Decisions IMD-001 through IMD-003 (pbs/03-implementation/decisions/)
          -> Implementation Artifacts (pbs/03-implementation)
            -> Verification (cross-cutting/04-verification)
              -> Operation (cross-cutting/05-operation)
                -> Evolution (cross-cutting/06-evolution)
```

## Per-Capability Traces

### Guarded Delivery

| Step | Trace |
| --- | --- |
| Intent | Vision.md — Core Thesis, Desired Outcomes |
| Product | PC-001 through PC-005, PC-007, PC-008, PC-010 |
| Architecture | Architecture.md — Control Flow, Stable Concepts, Boundaries |
| Decisions | AD-001 (agent workflow), AD-003 (handoff structure) |
| Implementation | orchestrator.md, orchestrator-*.md agents |
| Verification | Reviewer-coordinated verifier helper, review helpers, completion gate, final reflection |

### Candidate Capture

| Step | Trace |
| --- | --- |
| Intent | Vision.md — UC-012 |
| Product | PC-009 |
| Architecture | Architecture.md — Candidate capture mode |
| Decisions | ED-001 (backlog location), IMD-002 (product breakdown guidance in payload) |
| Implementation | orchestrator-planner.md, orchestrator-builder.md, reviewer helpers |
| Verification | Candidate-capture workflow-mode probes and backlog path assertions |
| Evolution | `product-breakdown/cross-cutting/06-evolution/` when present, plus `candidates/`, `selected/`, `done/`, `decisions/`, `roadmap.md`, `risks.md`, and `changelog.md` |

### Repo-Local Workflow Memory

| Step | Trace |
| --- | --- |
| Intent | Vision.md — Core Thesis, Desired Outcomes |
| Product | PC-003, PC-006, PC-007 |
| Architecture | Architecture.md — Workflow memory, Memory helper, Memory curator, Reflection, Persistence And Context Mechanisms |
| Decisions | IMD-001 (versioned lessons), IMD-003 (repo-local workflow memory) |
| Implementation | orchestrator-memory.md, orchestrator-memory-curator.md, orchestrator-reflection.md, `.opencode/dev_harness_memories/` |
| Verification | Workflow memory probe coverage, review/helper routing checks, final reflection output |

### Subagent Lifecycle And Context Freshness

| Step | Trace |
| --- | --- |
| Intent | Vision.md - Core Thesis, Desired Outcomes |
| Product | PC-003, PC-006, PC-007 |
| Architecture | Architecture.md - Subagent lifecycle policy, Boundaries, Persistence And Context Mechanisms |
| Decisions | AD-005 (fresh helper handoffs for context rot) |
| Implementation | `.opencode/dev_harness/workflow/subagent-lifecycle.md`, planner/builder/reviewer/reflection prompt references, helper lifecycle schema fields |
| Verification | Subagent lifecycle policy probe coverage and top-level stage reference checks |

### Traceability & Information Hygiene

| Step | Trace |
| --- | --- |
| Intent | Vision.md — PC-006 |
| Product | PC-006 |
| Architecture | Architecture.md — Information hygiene, Boundaries, Persistence And Context Mechanisms |
| Decisions | AD-002 (versioned markdown) |
| Implementation | information-hygiene.md, orchestrator-verifier.md, Mechanism Storage Rules |
| Verification | Information hygiene checks in reviewer-coordinated verifier + cleanliness/completeness review |

### Product Tree

| Step | Trace |
| --- | --- |
| Intent | Vision.md — traceable product-breakdown structure |
| Product | PC-006 — traceability and artifact lineage |
| Architecture | Architecture.md — Stable Concepts, Boundaries |
| Decisions | AD-002 (versioned markdown) |
| Implementation | product-tree.md — hierarchical PBS decomposition |
| Verification | Visual inspection of diagram accuracy against directory structure |
| Evolution | IMP-012 (hierarchical tree structure), IMP-014 (visual diagram), IMP-015 (element annotations), IMP-016 (decomposition relationships)

### Breakdown Structures

| Step | Trace |
| --- | --- |
| Intent | Vision.md — traceable decomposition from function to physical to work |
| Product | PC-006 — traceability and artifact lineage |
| Architecture | Architecture.md — Stable Concepts, Boundaries |
| Decisions | AD-002 (versioned markdown) |
| Implementation | breakdown-structures.md — FBS, PBS, WBS mapping |
| Verification | Cross-reference check that FBS, PBS, and WBS entries match existing artifacts |
| Evolution | IMP-016 (decomposition relationships)

### Architecture Verification

| Step | Trace |
| --- | --- |
| Intent | Vision.md — verifiable architecture layer |
| Product | PC-006 — traceability and artifact lineage |
| Architecture | Architecture.md — Boundaries, Mechanisms |
| Decisions | AD-002 (versioned markdown) |
| Implementation | 02-architecture/verification.md — horizontal verification artifact |
| Verification | Centralized criteria at 04-verification/acceptance-criteria.md (authoritative source); local extraction in pbs/02-architecture/verification.md |
| Evolution | IMP-013 (horizontal verification)

### Per-Layer Verification

| Step | Trace |
| --- | --- |
| Intent | fbs/00-intent/verification.md — AC-INTENT-01 through AC-INTENT-05 (vision.md, use-cases.md) |
| Product | fbs/01-product/verification.md — AC-PRODUCT-01 through AC-PRODUCT-08 (product-commitments.md) |
| Architecture | pbs/02-architecture/verification.md — AC-ARCH-01 through AC-ARCH-06 (architecture.md) |
| Implementation | pbs/03-implementation/verification.md — AC-IMPL-01 through AC-IMPL-03 (implementation.md) |
| Operation | cross-cutting/05-operation/verification.md — AC-OPS-01 through AC-OPS-12 (runbook.md, deployment-process.md) |
| Evolution | cross-cutting/06-evolution/verification.md — AC-EVOL-01 through AC-EVOL-06 (roadmap.md, changelog.md, risks.md, gap-analysis.md) |

This map is consolidated from per-file `## Trace Links` sections. Update the source file's trace links when adding or changing artifacts. This map is a summary — per-file sections contain the detailed links.
