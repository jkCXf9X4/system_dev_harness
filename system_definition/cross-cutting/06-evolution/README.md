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
   wbs.md        — Project management WBS with effort estimates and scheduling (planning aid)
   gap-analysis.md — FBS-PBS cross-reference gap analysis (IMP-020)
   prompt-policy-extraction-tasks.md — Prompt-policy extraction task breakdown and planning notes
   undeveloped_improvements.md — Record of undeveloped improvement findings not yet formalized as candidates
```

Note: The canonical absolute path is `system_definition/cross-cutting/06-evolution/`.

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

| File | ID | Theme | Status | Date |
| --- | --- | --- | --- | --- |
| `candidates/IMP-028-process-decision-records.md` | IMP-028 | Workflow process decision records for governance decisions | Proposed | 2026-06-29 |
| `candidates/IMP-030-process-configuration-management-and-rca.md` | IMP-030 | Process configuration management and root cause analysis | Proposed | 2026-06-29 |
| `candidates/IMP-034.md` | IMP-034 | Normalize edit/modify/write terminology in agent-boundaries.md | Proposed | 2026-06-30 |
| `candidates/IMP-035.md` | IMP-035 | Require plan_approval_status lifecycle updates after reviewer gate | Proposed | 2026-06-30 |
| `candidates/IMP-036.md` | IMP-036 | Process guard against out-of-scope file modifications during delivery | Proposed | 2026-06-30 |

## Selected

| File | ID | Theme | Selected Date | Task Contract |
| --- | --- | --- | --- | --- |
| `selected/IMP-031-orchestrator-systems-engineering.md` | IMP-031 | Create orchestrator-systems-engineering subagent for ISO 15288 / SysML analytical lens | 2026-06-29 | IMP-031-impl |
| `selected/IMP-032.md` | IMP-032 | Product-breakdown alignment review against orchestrator-systems-engineering agent requirements | 2026-06-29 | IMP-032-delivery |

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
| `done/IMP-008.md` | IMP-008 | Governance / Risk Management — Pre-Execution Approval for Larger Jobs | 2026-06-10 | `.opencode/dev_harness/workflow/control-policy.md`, `.opencode/dev_harness/workflow/large-job-guidelines.md`, `.opencode/agents/orchestrator-planner.md` |
| `done/IMP-009.md` | IMP-009 | Traceability / Learning — Mandatory Plan Summary Persistence | 2026-06-10 | `.opencode/dev_harness/workflow/control-policy.md`, `.opencode/dev_harness_plans/README.md` |
| `done/IMP-010.md` | IMP-010 | Planning / Collaboration — Enhanced Planning-and-Discussion Workflow | 2026-06-10 | `.opencode/agents/orchestrator-planner.md`, `.opencode/agents/orchestrator-reviewer.md`, `.opencode/dev_harness/workflow/control-policy.md`, `.opencode/dev_harness/workflow/large-job-guidelines.md` |
| `done/IMP-011.md` | IMP-011 | Workflow Control / Pre-Execution Approval — Plan Draft Approval Cycle | 2026-06-10 | `.opencode/agents/orchestrator.md`, `.opencode/agents/orchestrator-planner.md`, `.opencode/agents/orchestrator-reviewer.md`, `.opencode/dev_harness/workflow/control-policy.md`, `.opencode/dev_harness/workflow/large-job-guidelines.md`, `.opencode/dev_harness_plans/README.md` |
| `done/IMP-012.md` | IMP-012 | PBS / Structure — Hierarchical PBS tree with SoI root, element type annotations, and subordination | 2026-06-29 | `system_definition/product-tree.md`, `system_definition/README.md`, `system_definition/traceability-map.md` |
| `done/IMP-014.md` | IMP-014 | PBS / Visualization — Formal Product Tree diagram with Mermaid and ASCII fallback | 2026-06-29 | `system_definition/product-tree.md`, `system_definition/README.md`, `system_definition/traceability-map.md` |
| `done/IMP-013.md` | IMP-013 | PBS / Verification — Move verification into horizontal views per decomposition level | 2026-06-29 | `system_definition/pbs/02-architecture/verification.md`, `system_definition/traceability-map.md` |
| `done/IMP-015.md` | IMP-015 | PBS / Metadata — Annotate leaf elements with make/buy/reuse decisions | 2026-06-29 | `system_definition/product-tree.md` (annotations), `system_definition/README.md` (annotation convention) |
| `done/IMP-016.md` | IMP-016 | PBS / Decomposition — Document FBS-PBS-WBS relationships | 2026-06-29 | `system_definition/breakdown-structures.md`, `system_definition/README.md`, `system_definition/traceability-map.md` |
| `done/IMP-017.md` | IMP-017 | PBS / Decomposition — Restructure system-definition directories for FBS-PBS separation | 2026-06-29 | FBS/PBS/cross-cutting directory restructuring; all README files, path updates across 40+ files |
| `done/IMP-018.md` | IMP-018 | PBS / Decomposition — Update guidance for FBS-PBS-WBS alignment | 2026-06-29 | `.opencode/dev_harness/systems_engineering/README.md`, traceability.md, 06-evolution/imp.md, templates, candidate-capture.md |
| `done/IMP-019.md` | IMP-019 | PBS / Decomposition — Create project management WBS with effort estimates and schedules | 2026-06-29 | `system_definition/cross-cutting/06-evolution/wbs.md` — 20 work packages, effort estimates, dependency graph, 4-phase sequencing |
| `done/IMP-020.md` | IMP-020 | PBS / Decomposition — Gap analysis and fill for FBS/PBS trees | 2026-06-29 | `system_definition/cross-cutting/06-evolution/gap-analysis.md` — cross-reference tables, unmatched items, verified gaps (none critical); no new artifacts needed |
| `done/IMP-029.md` | IMP-029 | Workflow tailoring records and documentation | 2026-06-29 | `.opencode/dev_harness/workflow/control-policy.md`, `.opencode/dev_harness/workflow/adaptive-risk-triggers.md`, `.opencode/dev_harness/workflow/plan-summary-schema.md`, `.opencode/agents/orchestrator-planner.md`, `.opencode/agents/orchestrator-reporter.md` |

## Related Files

- Improvement overview template: `.opencode/dev_harness/systems_engineering/templates/improvement-backlog-overview-template.md`
- Per-candidate template: `.opencode/dev_harness/systems_engineering/templates/improvement-candidate-template.md`
- Evaluation template: `.opencode/dev_harness/systems_engineering/templates/improvement-evaluation-template.md`
