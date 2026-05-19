# UC-002 Task Contract

Use this template to turn a normalized task into a binding, checklistable contract.

Maps to: `UC-002`

## Input

- normalized task
- project context
- relevant repository files

## Prompt

You are writing a requirement contract.

Given:
- task: `{{task}}`
- project context: `{{project_context}}`
- relevant files: `{{relevant_files}}`

Return:
- task objective
- in scope
- out of scope
- functional requirements
- acceptance criteria
- completion checklist
- waiver rules

Every checklist item must be testable or reviewable.
