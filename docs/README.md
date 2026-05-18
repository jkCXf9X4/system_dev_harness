# System Dev Harness Documentation

This documentation captures the reason for the harness before the implementation grows. Lower-level artifacts should trace back to product commitments, use cases, requirements, architecture, or decisions.

## Reading Order

1. [01 Intent](01-intent/README.md)
2. [02 Product Commitments](02-product-commitments/README.md)
3. [03 System Architecture](03-system-architecture/README.md)
4. [04 Technical Decisions](04-technical-decisions/README.md)
5. [05 Implementation](05-implementation/README.md)
6. [06 Verification](06-verification/README.md)
7. [07 Lessons](07-lessons/README.md)

## Folder Layout

- `docs/01-intent/` holds vision and intent.
- `docs/02-product-commitments/` holds durable product promises.
- `docs/03-system-architecture/` holds use cases, requirements, architecture, and glossary.
- `docs/04-technical-decisions/` holds ADRs and decision templates.
- `docs/05-implementation/` holds implementation notes and execution adapters.
- `docs/06-verification/` holds traceability and verification records.
- `docs/07-lessons/` holds persistent known mistakes and lesson examples.
- `plans/` holds feature, implementation, and delivery plans outside `docs/`.
- If a folder contains an ordered sequence, use numeric prefixes on folders or files to make the reading order obvious.

## Decision Records

Architecture and product decisions live in [04-technical-decisions](04-technical-decisions/README.md).

Use decision records when a choice is likely to matter later, for example:

- orchestration framework
- model routing strategy
- persistence backend
- human approval model
- code execution permissions
- integration with GitHub, Jira, Linear, or opencode

## Documentation Principles

- Vision explains why the harness exists.
- Product commitments translate intent into durable product promises.
- Use cases explain who benefits and what they do.
- Requirements explain what the system must support.
- Architecture explains stable system concepts, guarantees, and boundaries.
- Decisions explain why a concrete design was chosen.
- Implementation artifacts satisfy decisions, requirements, and architecture constraints.
- Verification proves whether implementation satisfies the documented contract.
- Traceability links point backward to the layer being satisfied.
