# UC-005 Implementation Handoff

Use this template to generate a strict implementation brief from the approved contract and guardrails.

Maps to: `UC-005`, `UC-006`

## Input

- requirement contract
- architecture guardrails
- known mistakes
- relevant files

## Prompt

You are preparing an implementation handoff.

Given:
- contract: `{{contract}}`
- architecture guardrails: `{{architecture_guardrails}}`
- known mistakes: `{{known_mistakes}}`
- relevant files: `{{relevant_files}}`

Return:
- mission
- source material
- required implementation behavior
- execution steps
- architecture constraints
- required tests and checks
- definition of done
- stop conditions

Keep the brief narrow. Do not include out-of-contract refactoring or exploratory improvements.
