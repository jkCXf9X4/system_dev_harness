# Internal Documentation Map

This file maps the current solution from intent to implementation.

This docs tree is package documentation and source reference for the workflow package. It stays in this repository only; copy only `opencode.json` and `.opencode/` into a development repo.

| Layer | Source of Truth | Purpose |
| --- | --- | --- |
| Intent | `docs/01-intent/vision.md` | States why the solution exists and what problems it solves. |
| Use Cases | `docs/01-intent/use-cases.md` | Describes the actors and workflows the solution must support. |
| Product Commitments | `docs/02-product-commitments/product-commitments.md` | Captures durable promises derived from the intent. |
| System Architecture | `docs/03-system-architecture/architecture.md` | Describes the control flow, boundaries, and permissions. |
| Technical Decisions | `docs/04-technical-decisions/*.md` | Explains why the current structure exists. |
| Implementation | `docs/05-implementation/implementation.md` | Lists the repository artifacts that realize the solution. |
| Templates | `.opencode/templates/*` | Reusable prompt and supporting templates copied into the active payload. |

The docs tree itself is not copied into development repos.

## How To Use

Start at the intent docs, then walk downward through commitments, architecture, decisions, and implementation. Use `docs/03-system-architecture/architecture.md` as the canonical workflow policy and `docs/05-implementation/implementation.md` as the artifact map. Reviewers should verify that changes preserve the chain in both directions: from implementation back to intent, and from intent down to the package docs in this repository.
