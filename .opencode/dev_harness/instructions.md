# Dev Harness Instructions

This repository provides a guarded orchestrator workflow as the default OpenCode entrypoint.

When the active agent is `orchestrator` or an `orchestrator-*` agent, the guarded orchestrator workflow MUST be applied for every user request. Start by calling `orchestrator-planner`.

When the operator explicitly selects OpenCode's normal `build` agent, treat the currently selected agent as direct build execution outside the guarded orchestrator path. Work directly on the requested task, keep the change small, preserve unrelated work, and do not invoke planner, builder, reviewer, reporter, or other orchestrator stages.
