# 01 Product Layer

The product layer describes what the product does from the perspective of users, capabilities, workflows, and domain concepts.

## Typical Artifacts



```text
scope.md        - defines what is in and out of scope
capabilities.md - summarizes the product capabilities and behaviors
use-cases/      - contains user workflows and scenario descriptions
requirements/   - captures functional and non-functional requirements
experience/     - describes journeys, interactions, and UX notes
domain-model.md - documents the core concepts and their relationships
glossary.md     - standardizes the terms used across the product
decisions/      - stores product-level decisions and rationale
```

## Questions Answered

- What is in scope?
- What capabilities does the product provide?
- What use cases should the product support?
- What are the main domain concepts?
- What language should be used consistently?

## Example Decisions

```text
PD-001-projects-are-the-primary-organizing-unit.md
PD-002-collaboration-is-invite-only-in-v1.md
PD-003-reporting-is-in-scope-but-dashboards-are-not.md
PD-004-users-manage-access-through-roles.md
```

Product decisions affect capabilities, use cases, requirements, user journeys, and the domain model.
