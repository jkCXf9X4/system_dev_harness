# UC-013 Shortcut Loop

Use this template for small tasks that can use a lightweight workflow instead of the full guardrail chain.

Maps to: `UC-013`

## Input

- small bounded request
- obvious target files
- low-coupling change
- minimal verification needs

## Prompt

You are routing a small task through the shortcut workflow.

Given:
- request: `{{request}}`
- target files: `{{target_files}}`
- constraints: `{{constraints}}`

Return:
- compact task summary
- narrow file set
- minimal implementation steps
- minimum checks
- stop conditions
- escalation criteria if the task grows beyond shortcut scope

Keep the scope tight and do not promote this into a full guarded workflow unless the task becomes broader or riskier than it first appeared.
