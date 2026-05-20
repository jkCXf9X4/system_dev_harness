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
| Agent Templates | `.opencode/templates/*` | Reusable prompt and supporting templates copied into the active payload. |
| Product Breakdown Agent Context | `.opencode/templates/product-breakdown/README.md` | Layered guidance for intent, product, architecture, implementation, verification, operation, and evolution work. |

The docs tree itself is not copied into development repos.

## How To Use

Start at the intent docs, then walk downward through commitments, architecture, decisions, and implementation. Use `docs/03-system-architecture/architecture.md` as the canonical workflow policy and `docs/05-implementation/implementation.md` as the artifact map. Reviewers should verify that changes preserve the chain in both directions: from implementation back to intent, and from intent down to the package docs in this repository.

For product breakdown work in copied target repos, agents should use `.opencode/templates/product-breakdown/` as the runtime guidance because `docs/` is not copied into target repos.

## Layer Mapping

The package docs currently use compact names, but they map to the product breakdown layers:

| Product breakdown layer | Package docs source |
| --- | --- |
| `00-intent/` | `docs/01-intent/` |
| `01-product/` | `docs/02-product-commitments/` |
| `02-architecture/` | `docs/03-system-architecture/` |
| `03-implementation/` | `docs/05-implementation/` |
| `04-verification/` | workflow verifier and review evidence in `.opencode/agents/` |
| `05-operation/` | package usage and copied-payload operation in `README.md` |
| `06-evolution/` | `docs/06-backlog/` and improvement workflow artifacts |
