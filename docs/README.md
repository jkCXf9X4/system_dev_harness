# System Dev Harness Documentation

This documentation captures the reason for the harness before the implementation grows. Design decisions should trace back to the vision, use cases, and explicit requirements here.

## Reading Order

1. [Vision](vision.md)
2. [Product Commitments](product-commitments.md)
3. [Use Cases](use-cases.md)
4. [Requirements](requirements.md)
5. [Architecture Overview](architecture.md)
6. [Decision Records](decisions/README.md)
7. [Traceability Matrix](traceability.md)
8. [Roadmap](roadmap.md)
9. [Known Mistakes](lessons/known-mistakes.md)
10. [Execution Adapters](execution-adapters.md)

## Decision Records

Architecture and product decisions live in [decisions](decisions/README.md).

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
