# UC-003 Architecture Guardrails

Use this template to preserve architecture during agentic development.

Maps to: `UC-003`, `UC-011`

## Input

- task contract
- architecture notes
- project constraints
- existing patterns

## Prompt

You are extracting architecture guardrails.

Given:
- contract: `{{contract}}`
- architecture notes: `{{architecture_notes}}`
- project constraints: `{{project_constraints}}`
- existing patterns: `{{existing_patterns}}`

Return:
- relevant existing patterns
- architectural constraints
- integration boundaries
- modularity expectations
- simplicity expectations
- readability checks
- module responsibility risks
- forbidden shortcuts
- architecture review checks

Prefer the simplest readable solution that fits the current module boundaries.
