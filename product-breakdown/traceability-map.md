# Traceability Map

This map documents the cross-layer traceability chain for the workflow package. Each capability traces from intent through product commitments, architecture, decisions, implementation, verification, operation, and evolution.

## Core Trace Chain

```
Vision.md (00-intent)
  -> Product Commitments PC-001 through PC-010 (01-product)
    -> Use Cases UC-001 through UC-013 (00-intent)
      -> Architecture (02-architecture)
        -> Decisions AD-001 through AD-003 (02-architecture/decisions/)
        -> Decisions IMD-001 through IMD-002 (03-implementation/decisions/)
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
| Verification | Verifier stage, review agents, completion gate |

### Continuous Improvement

| Step | Trace |
| --- | --- |
| Intent | Vision.md — UC-012 |
| Product | PC-009 |
| Architecture | Architecture.md — Improvement workflow |
| Decisions | ED-001 (backlog location), IMD-002 (product breakdown guidance in payload) |
| Implementation | orchestrator-improvement.md |
| Verification | Improvement smoke test and backlog path assertions |
| Evolution | `product-breakdown/06-evolution/backlog/` when present, plus `decisions/`, `roadmap.md`, `risks.md`, and `changelog.md` |

### Traceability & Information Hygiene

| Step | Trace |
| --- | --- |
| Intent | Vision.md — PC-006 |
| Product | PC-006 |
| Architecture | Architecture.md — Information hygiene, Boundaries |
| Decisions | AD-002 (versioned markdown) |
| Implementation | information-hygiene.md, orchestrator-verifier.md |
| Verification | Information hygiene checks in verifier + completeness review |

## Maintenance

This map is consolidated from per-file `## Trace Links` sections. Update the source file's trace links when adding or changing artifacts. This map is a summary — per-file sections contain the detailed links.
