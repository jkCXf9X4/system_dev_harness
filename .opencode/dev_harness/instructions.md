# Dev Harness Instructions

This repository provides a guarded orchestrator workflow as the default OpenCode entrypoint.

Common policies: `.opencode/dev_harness/workflow/_common-policies.md`.

When the active agent is `orchestrator-router` or an `orchestrator-*` agent, the guarded orchestrator workflow MUST be applied for every user request. `orchestrator-router` is the primary entrypoint. `orchestrator` may remain as an alias for `orchestrator-router`.

When the operator explicitly selects OpenCode's normal `build` agent, treat the currently selected agent as direct build execution outside the guarded orchestrator path. Work directly on the requested task, keep the change small, preserve unrelated work, and do not invoke planner, builder, reviewer, reporter, or other orchestrator stages.

## Task Tracking

Every task processed by the guarded workflow is tracked in a task tracking file under `.opencode/dev_harness_tasks/`. This provides continuous, stage-by-stage traceability from routing through final reporting. See `.opencode/dev_harness/workflow/task-summary-schema.md` for the schema and `.opencode/dev_harness/workflow/control-policy.md` for lifecycle rules.
