# Dev Harness Instructions

This repository provides a guarded orchestrator workflow as the default OpenCode entrypoint.

Follow the currently selected agent. Do not apply the guarded orchestrator workflow unless the active agent is `orchestrator` or an `orchestrator-*` agent.

When the operator explicitly selects OpenCode's normal `build` agent, treat it as direct build execution outside the guarded orchestrator path. Work directly on the requested task, keep the change small, preserve unrelated work, and do not invoke planner, builder, reviewer, reporter, or other orchestrator stages.
