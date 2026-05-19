# UC-001 Normalize Request

Use this template to turn a rough request into a concrete task shape and work order.

Maps to: `UC-001`

## Input

- project intent
- user request
- surrounding context
- relevant constraints

## Prompt

You are normalizing a request into a concrete task.

Given:
- request: `{{request}}`
- project context: `{{project_context}}`
- constraints: `{{constraints}}`

Return:
- normalized task summary
- execution order
- likely follow-up agents
- open questions or missing context
- obvious scope risks

Keep the result specific enough to start the workflow, but do not invent implementation details.
