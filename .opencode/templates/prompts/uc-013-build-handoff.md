# UC-013 Small Task Build Handoff

Use this template for small tasks that should go directly to OpenCode's built-in `build` primary agent instead of the full guardrail chain.

Maps to: `UC-013`

## Input

- small bounded request
- obvious target files
- low-coupling change
- minimal verification needs

## Prompt

You are preparing a compact handoff for OpenCode's built-in `build` primary agent.

Given:
- request: `{{request}}`
- target files: `{{target_files}}`
- constraints: `{{constraints}}`

Return:
- compact task summary
- narrow file set
- implementation instructions
- minimum checks
- stop conditions
- escalation criteria if the task grows beyond small-task scope
- explicit instruction to switch to OpenCode's `build` primary agent for execution

Keep the scope tight. If the task is broader or riskier than it first appeared, route it back to the full guarded workflow before implementation starts.
