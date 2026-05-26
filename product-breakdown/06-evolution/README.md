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
  imp.md        — Improvement tracking index
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

## Related Files

- Improvement overview template: `.opencode/dev_harness/product-breakdown/templates/improvement-backlog-overview-template.md`
- Per-candidate template: `.opencode/dev_harness/product-breakdown/templates/improvement-candidate-template.md`
