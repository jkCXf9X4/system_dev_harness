# Internal Documentation Map

This file maps the current solution from intent to implementation.

This docs tree is package documentation and source reference for the workflow package. It stays in this repository only; copy only `opencode.json` and `.opencode/` into a development repo.

| Layer | Source of Truth | Purpose |
| --- | --- | --- |
| Intent | `docs/00-intent/vision.md` | States why the solution exists and what problems it solves. |
| Use Cases | `docs/00-intent/use-cases.md` | Describes the actors and workflows the solution must support. |
| Product Commitments | `docs/01-product/product-commitments.md` | Captures durable promises derived from the intent. |
| System Architecture | `docs/02-architecture/architecture.md` | Describes the control flow, boundaries, and permissions. |
| Technical Decisions | `docs/decision-log.md` | Index of decisions distributed across per-layer `decisions/` directories. |
| Implementation | `docs/03-implementation/implementation.md` | Lists the repository artifacts that realize the solution. |
| Agent Templates | `.opencode/templates/*` | Reusable prompt and supporting templates copied into the active payload. |
| Product Breakdown Agent Context | `.opencode/templates/product-breakdown/README.md` | Layered guidance for intent, product, architecture, implementation, verification, operation, and evolution work. |
| Workflow Policy Agent Context | `.opencode/templates/workflow/` | Shared control, information hygiene, and review-output policy for copied agents. |

The docs tree itself is not copied into development repos.

## How To Use

Start at the intent docs, then walk downward through commitments, architecture, decisions, and implementation. Use `docs/02-architecture/architecture.md` as the canonical workflow policy and `docs/03-implementation/implementation.md` as the artifact map. Reviewers should verify that changes preserve the chain in both directions: from implementation back to intent, and from intent down to the package docs in this repository.

For product breakdown work in copied target repos, agents should use `.opencode/templates/product-breakdown/` as the runtime guidance because `docs/` is not copied into target repos.

For guarded workflow control in copied target repos, agents should use `.opencode/templates/workflow/` as the runtime policy source for stage applicability, waivers, information hygiene, and review output.

## Directory Structure

This tree follows the product-breakdown template layer numbering. Each numbered directory corresponds to a template layer:

- `docs/00-intent/` — Why does this product exist?
- `docs/01-product/` — What should it do?
- `docs/02-architecture/` — How is it structurally organized? (includes `decisions/` for architecture decisions)
- `docs/03-implementation/` — How is it built in code and configuration? (includes `decisions/` for implementation decisions)
- `docs/04-verification/` — (to be created)
- `docs/05-operation/` — (to be created)
- `docs/06-evolution/` — How should it change over time?
- `docs/decision-log.md` — Index of all decisions across layers

See `.opencode/templates/product-breakdown/README.md` for the full layer definitions.
