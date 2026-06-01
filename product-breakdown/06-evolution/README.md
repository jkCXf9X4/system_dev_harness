# 06 Evolution — Improvement Lifecycle

This directory hosts the three-stage improvement lifecycle for continuous improvement candidates.

## Folder Structure

```
06-evolution/
  candidates/   — Proposed improvements not yet selected for development
  selected/     — Improvements approved and waiting or being implemented
  done/         — Historical tracking of completed improvements
  changelog.md  — Notable changes over time
  risks.md      — Known risks, tradeoffs, and open concerns
  roadmap.md    — Planned future work and sequencing
```

## Lifecycle

1. **Candidate** (`candidates/`): Any improvement finding that is backlog-worthy but has no task contract yet. Persisted by the improvement workflow or focused evaluator.
2. **Selected** (`selected/`): A candidate that has been approved for implementation via a scoped task contract. The candidate file is added here (or symlinked/moved) when contract creation triggers the transition.
3. **Done** (`done/`): An improvement whose implementation is verified complete. The file is moved here for historical tracking.

## Transition Triggers

| Transition | Trigger | Responsible Stage |
|---|---|---|
| `candidates/` → `selected/` | A task contract is created for the candidate | Planner / improvement workflow |
| `selected/` → `done/` | Implementation is verified complete | Reviewer / verifier |

## Candidates

| File | ID | Theme | Status | Priority | Blast radius |
| --- | --- | --- | --- | --- | --- |
| `candidates/IMP-001.md` | IMP-001 | Memory trust metadata and revalidation | Proposed | High | Medium |
| `candidates/IMP-002.md` | IMP-002 | Memory save/skip and rejection reasons | Proposed | Medium | Low to medium |
| `candidates/IMP-003.md` | IMP-003 | Durable memory versus searchable task history | Proposed | Medium | Medium |
| `candidates/IMP-004.md` | IMP-004 | Memory hygiene checks in review and reporting | Proposed | High | Low to medium |
| `candidates/IMP-005.md` | IMP-005 | Procedural patterns versus factual memory | Proposed | Medium | Low |

## Done

| File | ID | Theme | Completed Date | Implementation Reference |
| --- | --- | --- | --- | --- |
| `done/IMP-006.md` | IMP-006 | Initial clarification gate for ambiguous requests | 2026-06-01 | `.opencode/agents/orchestrator.md`, `.opencode/agents/orchestrator-planner.md`, `.opencode/dev_harness/workflow/control-policy.md` |

## Related Files

- Improvement overview template: `.opencode/dev_harness/product-breakdown/templates/improvement-backlog-overview-template.md`
- Per-candidate template: `.opencode/dev_harness/product-breakdown/templates/improvement-candidate-template.md`
