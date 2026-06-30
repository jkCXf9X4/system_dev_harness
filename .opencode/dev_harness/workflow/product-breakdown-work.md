# Product Breakdown Work

Use this policy when a workflow touches `system_definition/` or copied system-definition guidance under `.opencode/dev_harness/systems_engineering/`.

## Loading Rules

- Load only system-definition guidance relevant to the planner work order.
- Use `.opencode/dev_harness/systems_engineering/README.md` to select focused layer, template, decision, and traceability guidance.
- Do not bulk-load system-definition context when `touches_product_breakdown` is false.

## Placement Rules

- Product intent, commitments, architecture, decisions, verification expectations, operation requirements, evolution state, and traceability belong in `system_definition/`.
- Runnable how-to steps, examples, and operational usage guidance belong in `docs/`.
- Decision work should use `decision-placement.md`, decision templates, and the relevant decision log.
- Improvement backlog work should use the evolution layer and improvement backlog templates.

## Required Evidence

When `touches_product_breakdown` is true, stage output should include:

- primary system-definition layer
- affected downstream layers
- placement rationale
- traceability updates or `not_applicable` rationale
- decision-record update or `not_applicable` rationale
- stale reference, duplicate, orphan, and index checks

Use `not_applicable` only when the planner work order or verified evidence shows the system-definition obligation does not apply.
