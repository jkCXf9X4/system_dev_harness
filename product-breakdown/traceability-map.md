# Traceability Map

This map documents the cross-layer traceability chain for the workflow package. Each capability traces from intent through product commitments, architecture, decisions, implementation, verification, operation, and evolution.

## Core Trace Chain

```
Vision.md (00-intent)
  -> Product Commitments PC-001 through PC-010 (01-product)
    -> Use Cases UC-001 through UC-013 (00-intent)
  -> Architecture (02-architecture)
        -> Decisions AD-001 through AD-003 (02-architecture/decisions/)
        -> Decisions IMD-001 through IMD-003 (03-implementation/decisions/)
          -> Implementation Artifacts (03-implementation)
            -> Verification (04-verification)
              -> Operation (05-operation)
                -> Evolution (06-evolution)
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
| Evolution | `product-breakdown/06-evolution/` when present, plus `candidates/`, `selected/`, `done/`, `decisions/`, `roadmap.md`, `risks.md`, and `changelog.md` |

### Repo-Local Workflow Memory

| Step | Trace |
| --- | --- |
| Intent | Vision.md — Core Thesis, Desired Outcomes |
| Product | PC-003, PC-006, PC-007 |
| Architecture | Architecture.md — Workflow memory, Memory helper, Memory curator, Reflection, Persistence And Context Mechanisms |
| Decisions | IMD-001 (versioned lessons), IMD-003 (repo-local workflow memory) |
| Implementation | orchestrator-memory.md, orchestrator-memory-curator.md, orchestrator-reflection.md, `.opencode/dev_harness_memories/` |
| Verification | Workflow memory probe coverage, review/helper routing checks, final reflection output |

### Traceability & Information Hygiene

| Step | Trace |
| --- | --- |
| Intent | Vision.md — PC-006 |
| Product | PC-006 |
| Architecture | Architecture.md — Information hygiene, Boundaries, Persistence And Context Mechanisms |
| Decisions | AD-002 (versioned markdown) |
| Implementation | information-hygiene.md, orchestrator-verifier.md, Mechanism Storage Rules |
| Verification | Information hygiene checks in reviewer-coordinated verifier + cleanliness/completeness review |

## Maintenance

This map is consolidated from per-file `## Trace Links` sections. Update the source file's trace links when adding or changing artifacts. This map is a summary — per-file sections contain the detailed links.
