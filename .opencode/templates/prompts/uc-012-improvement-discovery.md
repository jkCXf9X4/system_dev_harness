# UC-012 Improvement Discovery

Use this template for exploratory continuous-improvement work that should feed a backlog rather than change code.

Maps to: `UC-012`

## Input

- current feature set
- current requirements
- implementation evidence
- reviewer findings
- module friction or repeated pain

## Prompt

You are discovering backlog-worthy improvement work.

Given:
- feature set: `{{feature_set}}`
- requirements: `{{requirements}}`
- implementation evidence: `{{implementation_evidence}}`
- review findings: `{{review_findings}}`
- module friction: `{{module_friction}}`

Return:
- improvement theme
- evidence and source files
- current pain or risk
- proposed refactoring, pattern switch, module responsibility switch, or tuning
- expected benefit
- risk and blast radius
- suggested priority
- backlog-ready task seed
- what must stay out of the current contained feature diffs

This workflow is exploratory and read-only. Do not recommend bundling the work into an unrelated implementation task.
