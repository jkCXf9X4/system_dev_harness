# 06 Evolution — Improvement Lifecycle

This directory hosts the three-stage improvement lifecycle for continuous improvement candidates.

## Folder Structure

```
06-evolution/
  candidates/   — Proposed improvements not yet selected for development
  selected/     — Improvements approved and waiting or being implemented
  done/         — Historical tracking of completed improvements
  evaluations/  — Rejected or deferred improvement suggestions kept for future reference
  changelog.md  — Notable changes over time
  risks.md      — Known risks, tradeoffs, and open concerns
  roadmap.md    — Planned future work and sequencing
```

## Lifecycle

1. **Candidate** (`candidates/`): Any improvement finding that is backlog-worthy but has no task contract yet. Persisted by builder candidate-capture mode.
2. **Selected** (`selected/`): A candidate that has been approved for implementation via a scoped task contract. The candidate file is added here (or symlinked/moved) when contract creation triggers the transition.
3. **Done** (`done/`): An improvement whose implementation is verified complete. The file is moved here for historical tracking.

Rejected or deferred suggestions are stored under `evaluations/` so future agents can inspect why a suggestion did not become a candidate without polluting the candidate backlog.

## Transition Triggers

| Transition | Trigger | Responsible Stage |
|---|---|---|
| `candidates/` → `selected/` | A task contract is created for the candidate | Planner / builder candidate-capture workflow |
| `selected/` → `done/` | Implementation is verified complete | Reviewer / verifier |

## Candidates

| File | ID | Theme | Priority | Proposed Date |
| --- | --- | --- | --- | --- |
| `candidates/IMP-010.md` | IMP-010 | Collaboration / Iteration — Enhanced Planning-and-Discussion Workflow | Medium | 2026-06-10 |


## Selected

| File | ID | Theme | Selected Date | Task Contract |
| --- | --- | --- | --- | --- |
| `selected/IMP-008.md` | IMP-008 | Governance / Risk Management — Pre-Execution Approval for Larger Jobs | 2026-06-10 | Implemented via this coordinated pass |
| `selected/IMP-009.md` | IMP-009 | Traceability / Learning — Mandatory Plan Summary Persistence | 2026-06-10 | Implemented via this coordinated pass |

## Evaluations

No rejected or deferred evaluations are currently recorded.

## Done

| File | ID | Theme | Completed Date | Implementation Reference |
| --- | --- | --- | --- | --- |
| `done/IMP-001.md` | IMP-001 | Memory trust metadata and revalidation | 2026-06-01 | `.opencode/dev_harness_memories/README.md`, `.opencode/dev_harness_memories/lessons.md`, `.opencode/dev_harness_memories/patterns.md`, `.opencode/agents/orchestrator-memory.md`, `.opencode/agents/orchestrator-memory-curator.md`, `.opencode/dev_harness/workflow/control-policy.md` |
| `done/IMP-002.md` | IMP-002 | Memory save/skip and rejection reasons | 2026-06-01 | `.opencode/agents/orchestrator-memory-curator.md`, `.opencode/dev_harness/workflow/control-policy.md`, `.opencode/agents/orchestrator-reporter.md` |
| `done/IMP-003.md` | IMP-003 | Durable memory versus searchable task history | 2026-06-01 | `.opencode/dev_harness_memories/README.md`, `.opencode/agents/orchestrator-memory.md`, `.opencode/agents/orchestrator-memory-curator.md`, `.opencode/dev_harness/workflow/control-policy.md`, `.opencode/agents/orchestrator-reporter.md` |
| `done/IMP-004.md` | IMP-004 | Memory hygiene checks in review and reporting | 2026-06-01 | `.opencode/agents/orchestrator-reviewer.md`, `.opencode/agents/orchestrator-review-lessons.md`, `.opencode/agents/orchestrator-reporter.md`, `.opencode/dev_harness/workflow/review-output.md`, `.opencode/dev_harness/workflow/control-policy.md` |
| `done/IMP-005.md` | IMP-005 | Procedural patterns versus factual memory | 2026-06-01 | `.opencode/dev_harness_memories/README.md`, `.opencode/dev_harness_memories/patterns.md`, `.opencode/agents/orchestrator-memory-curator.md`, `.opencode/dev_harness/workflow/control-policy.md` |
| `done/IMP-006.md` | IMP-006 | Initial clarification gate for ambiguous requests | 2026-06-01 | `.opencode/agents/orchestrator.md`, `.opencode/agents/orchestrator-planner.md`, `.opencode/dev_harness/workflow/control-policy.md` |
| `done/IMP-007.md` | IMP-007 | Final reflection stage for memory incorporation ownership | 2026-06-01 | `.opencode/agents/orchestrator-reflection.md`, `.opencode/dev_harness/workflow/control-policy.md` |
| `done/IMP-011.md` | IMP-011 | Workflow Control / Pre-Execution Approval — Plan Draft Approval Cycle | 2026-06-10 | `.opencode/agents/orchestrator.md`, `.opencode/agents/orchestrator-planner.md`, `.opencode/agents/orchestrator-reviewer.md`, `.opencode/dev_harness/workflow/control-policy.md`, `.opencode/dev_harness/workflow/large-job-guidelines.md`, `.opencode/dev_harness_plans/README.md` |

## Related Files

- Improvement overview template: `.opencode/dev_harness/product-breakdown/templates/improvement-backlog-overview-template.md`
- Per-candidate template: `.opencode/dev_harness/product-breakdown/templates/improvement-candidate-template.md`
- Evaluation template: `.opencode/dev_harness/product-breakdown/templates/improvement-evaluation-template.md`
