# Traceability

This file maps the current solution from intent to implementation.

| Layer | Source of Truth | Purpose |
| --- | --- | --- |
| Intent | `.opencode/01-intent/vision.md` | States why the solution exists and what problems it solves. |
| Use Cases | `.opencode/01-intent/use-cases.md` | Describes the actors and workflows the solution must support. |
| Product Commitments | `.opencode/02-product-commitments/product-commitments.md` | Captures durable promises derived from the intent. |
| System Architecture | `.opencode/03-system-architecture/architecture.md` | Describes the control flow, boundaries, and permissions. |
| Technical Decisions | `.opencode/04-technical-decisions/*.md` | Explains why the current structure exists. |
| Implementation | `.opencode/05-implementation/implementation.md` | Lists the repository artifacts that realize the solution. |

## How To Use

Start at the intent docs, then walk downward through commitments, architecture, decisions, and implementation. Reviewers should verify that changes preserve the chain in both directions: from implementation back to intent, and from intent down to the actual artifacts.
