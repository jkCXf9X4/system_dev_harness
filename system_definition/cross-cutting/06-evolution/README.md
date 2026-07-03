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
| `candidates/IMP-027-quantitative-workflow-metrics.md` | IMP-027 | Quantitative Workflow Metrics | Proposed | 2026-06-29 |
| `candidates/IMP-054-god-planner-anti-pattern.md` | IMP-054 | God Planner Anti-Pattern — Decompose Planner Responsibilities | Proposed | 2026-06-30 |
| `candidates/IMP-058-error-recovery-path.md` | IMP-058 | Error Recovery Path — Defined Recovery for Stage Failures | Proposed | 2026-07-01 |
| `candidates/IMP-059-pre-stage-readiness-verification.md` | IMP-059 | Pre-Stage Readiness Verification — Stage Gate Readiness Checks | Proposed | 2026-07-01 |

## Selected

No items currently selected.

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
| `done/IMP-021.md` | IMP-021 | Verification / INCOSE Alignment — Evolve verification artifact pattern to dual INCOSE pattern (centralized strategy + per-element horizontal-view criteria) | 2026-06-30 | See file for details |
| `done/IMP-022.md` | IMP-022 | Verification / INCOSE — Evaluation of a fourth decomposition tree (VBS) running parallel to FBS/PBS/WBS | 2026-06-30 | See file for details |
| `done/IMP-026-validation-gate-integration.md` | IMP-026 | Add a validation gate between contract and builder stages to close the verification-only gap | 2026-07-01 | See file for details |
| `done/IMP-029.md` | IMP-029 | Workflow tailoring records and documentation | 2026-06-29 | `.opencode/dev_harness/workflow/control-policy.md`, `.opencode/dev_harness/workflow/planner-triggers.md`, `.opencode/dev_harness/workflow/plan-summary-schema.md`, `.opencode/agents/orchestrator-planner.md`, `.opencode/agents/orchestrator-reporter.md` |
| `done/IMP-031-orchestrator-systems-engineering.md` | IMP-031 | Create orchestrator-systems-engineering subagent for ISO 15288 / SysML analytical lens | 2026-07-02 | See file for details |
| `done/IMP-032.md` | IMP-032 | PBS/SE — Product-breakdown alignment review against orchestrator-systems-engineering agent requirements | 2026-07-02 | See file for details |
| `done/IMP-033-se-traceability-evaluation.md` | IMP-033 | Systems engineering traceability structure evaluation for the renamed system_definition/ tree | 2026-06-30 | See file for details |
| `done/IMP-034.md` | IMP-034 | Terminology normalization | 2026-07-01 | IMP-034 — terminology normalization in agent-boundaries.md |
| `done/IMP-037.md` | IMP-037 | Workflow token-efficiency optimization | 2026-07-01 | See file for details |
| `done/IMP-038.md` | IMP-038 | Agent prompt de-duplication | 2026-07-01 | IMP-038 — stripped duplicated rules from 3 agent prompts; 17 agents audited with no duplication found |
| `done/IMP-039.md` | IMP-039 | Policy file modularization | 2026-07-01 | IMP-039 — plan: `.opencode/dev_harness_plans/2026-07-01_000600-IMP-039.md` |
| `done/IMP-040.md` | IMP-040 | Cross-stage token efficiency | 2026-07-01 | Plan: `.opencode/dev_harness_plans/2026-07-01_000800-IMP-040.md`; Changes: stage-output-schema.md, orchestrator-planner.md |
| `done/IMP-044.md` | IMP-044 | Output field minimization | 2026-07-01 | Plan: `.opencode/dev_harness_plans/2026-07-01_000700-IMP-044.md`; Files: stage-output-schema.md, orchestrator-planner.md |
| `done/IMP-045.md` | IMP-045 | Fix stale system-definition documentation — C05 Stage Order Invariant in sequence-parametric.md | 2026-07-01 | IMP-045 — C05 invariant update in sequence-parametric.md |
| `done/IMP-046.md` | IMP-046 | Reconcile candidate-capture chain definition in control-policy.md with planner routing behavior | 2026-07-01 | IMP-046 — candidate-capture chain reconciliation in control-policy.md |
| `done/IMP-048.md` | IMP-048 | Document validation stage fail outcome consistency with PD-003 single-gate-authority model | 2026-07-01 | IMP-048 — AD-006 validation advisory decision record |
| `done/IMP-049.md` | IMP-049 | Fold orchestrator-validation stage into reviewer as parallel helper to eliminate serial latency | 2026-07-01 | IMP-049 — Fold validation into reviewer as parallel helper |
| `done/IMP-050.md` | IMP-050 | Remove redundant contract fields after planner-orchestrator consolidation | 2026-07-01 | IMP-050 implementation: trimmed planner output contract |
| `done/IMP-051.md` | IMP-051 | Profile-vs-frontmatter documentation gap | 2026-07-01 | IMP-051 — permission profiles reconciliation |
| `done/IMP-053.md` | IMP-053 | Workflow information contract — plan file as durable context for downstream stages | 2026-07-01 | See file for details |
| `done/IMP-055-consolidate-helper-triggers.md` | IMP-055 | Consolidate overlapping helper trigger policies to eliminate conflicts and duplication | 2026-07-02 | Combined task IMP-055-056-057-060-062-063 |
| `done/IMP-056-eliminate-inline-duplication.md` | IMP-056 | Eliminate duplication between planner inline output schema and plan file content | 2026-07-02 | Combined task IMP-055-056-057-060-062-063 |
| `done/IMP-057-external-boundary-enforcement.md` | IMP-057 | Add external enforcement for planner edit/write permission boundary | 2026-07-02 | Combined task IMP-055-056-057-060-062-063 |
| `done/IMP-060-plan-file-archive-hygiene.md` | IMP-060 | Add error handling for plan file write failures and improve archive integrity | 2026-07-02 | Combined task IMP-055-056-057-060-062-063 |
| `done/IMP-062-stale-artifacts-cleanup.md` | IMP-062 | Clean up stale artifacts: typo files, stale tracked files, empty directories | 2026-07-02 | Combined task IMP-055-056-057-060-062-063 |
| `done/IMP-063-framework-self-consistency-audit.md` | IMP-063 | Audit agent framework to verify it follows its own rules and quality standards | 2026-07-02 | Combined task IMP-055-056-057-060-062-063 |
| `done/IMP-064-stale-readme-candidates-table.md` | IMP-064 | Stale README Candidates Table — Update Lifecycle State References | 2026-07-03 | `.opencode/dev_harness_plans/2026-07-03_000000-IMP-064.md` |

## Related Files

- Improvement overview template: `.opencode/dev_harness/systems_engineering/templates/improvement-backlog-overview-template.md`
- Per-candidate template: `.opencode/dev_harness/systems_engineering/templates/improvement-candidate-template.md`
- Evaluation template: `.opencode/dev_harness/systems_engineering/templates/improvement-evaluation-template.md`
