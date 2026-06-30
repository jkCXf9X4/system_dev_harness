# Agent Boundaries

Use this policy for agent read/write boundaries, scope containment, and no-edit responsibilities.

## Common Scope Rules

- Stay inside the approved work order or helper assignment.
- Do not broaden scope unless the planner work order is revised through the guarded workflow.
- Do not treat improvement candidates, memory candidates, waivers, or helper findings as permission to implement extra work.
- Preserve unrelated user changes and unrelated repository state.

## Read-Only Agents

These agents do not modify files: orchestrator, discovery, contract, architecture, lessons, memory, reviewer, verifier, review-architecture, review-completeness, review-lessons, researcher, systems-engineering, reflection, and reporter.

Read-only agents should inspect only the minimum useful evidence for their role. When discovery has named exact files, helper agents should prefer those files over broad repository search.

## Limited-Write Agents

The planner may write only the current task's standardized plan summary under `.opencode/dev_harness_plans/`, as required by `.opencode/dev_harness/workflow/plan-summary-schema.md` and `.opencode/dev_harness/workflow/control-policy.md`. It must not edit implementation files, system-definition artifacts, runtime prompts, tests, or memory files.

## Editing Agents

The builder may edit files within the approved work order.

The build error resolver may edit only files needed to fix build, test, type-check, or dependency failures caused by the current implementation or explicitly assigned by the builder.

The cleanup helper may edit only stale references, trackers, indexes, duplicate or superseded content, orphaned artifacts, links, and traceability inside the builder-assigned scope.

The memory curator may edit only `.opencode/dev_harness_memories/lessons.md` and `.opencode/dev_harness_memories/patterns.md` unless the workflow memory policy is explicitly extended.

In `workflow_mode: candidate_capture`, the builder may write only improvement backlog artifacts allowed by `.opencode/dev_harness/workflow/candidate-capture.md`.

## No-Edit Reporting

Agents that cannot edit files should return blocking gaps, required follow-up, or `improvement_candidates` instead of silently changing artifacts.
