# System Dev Harness Documentation

This documentation captures the reason for the harness before the implementation grows. Design decisions should trace back to the vision, use cases, and explicit requirements here.

## Reading Order

1. [Vision](vision.md)
2. [Use Cases](use-cases.md)
3. [Requirements](requirements.md)
4. [Traceability Matrix](traceability.md)
5. [Architecture Overview](architecture.md)
6. [Roadmap](roadmap.md)
7. [Known Mistakes](lessons/known-mistakes.md)

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
- Use cases explain who benefits and what they do.
- Requirements explain what the system must support.
- Decisions explain why a concrete design was chosen.
- Traceability connects implementation decisions back to outcomes.
