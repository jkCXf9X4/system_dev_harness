# Internal Documentation Map

This file maps the current solution from intent to implementation.

This tree is the product-breakdown source documentation and traceability set for the workflow package. It stays in this repository only; copy only `opencode.json` and `.opencode/` into a development repo.

## Boundary With `docs/`

Use `product-breakdown/` for product source information: what the workflow package is, who it serves, what is in or out of scope, which stable decisions constrain it, and how intent traces through architecture, implementation, verification, operation, and evolution.

Use `docs/` for runnable and contributor-facing guidance: installation, deployment refreshes, command examples, usage instructions, troubleshooting, verification commands, and concrete examples for operators or maintainers.

Do not duplicate the same example, command, or policy text in both places. When a guide needs product context, link to the relevant `product-breakdown/` artifact instead of copying the product text. When a product artifact needs operational detail, state the durable product requirement and link to the matching `docs/` page for steps.

| Layer | Source of Truth | Purpose |
| --- | --- | --- |
| Intent | `product-breakdown/00-intent/vision.md` | States why the solution exists and what problems it solves. |
| Use Cases | `product-breakdown/00-intent/use-cases.md` | Describes the actors and workflows the solution must support. |
| Product Commitments | `product-breakdown/01-product/product-commitments.md` | Captures durable promises derived from the intent. |
| System Architecture | `product-breakdown/02-architecture/architecture.md` | Describes the control flow, boundaries, and permissions. |
| Technical Decisions | `product-breakdown/decision-log.md` | Index of decisions distributed across per-layer `decisions/` directories. |
| Implementation | `product-breakdown/03-implementation/implementation.md` | Lists the repository artifacts that realize the solution. |
| Verification | `product-breakdown/04-verification/` | Captures acceptance criteria, test strategy, and traceability. |
| Operation | `product-breakdown/05-operation/` | Captures operational product requirements and support constraints; runnable steps live in `docs/`. |
| Evolution | `product-breakdown/06-evolution/` | Captures roadmap, candidates, selected improvements, completed improvements, risks, and changelog history. |
| Dev Harness Context | `.opencode/dev_harness/*` | Reusable prompt, workflow, and supporting context copied into the active payload. |
| Product Breakdown Agent Context | `.opencode/dev_harness/product-breakdown/README.md` | Layered guidance for intent, product, architecture, implementation, verification, operation, and evolution work. |
| Workflow Policy Agent Context | `.opencode/dev_harness/workflow/` | Shared control, information hygiene, and review-output policy for copied agents. |
| Repo-Local Workflow Memory | `.opencode/dev_harness_memories/` | Durable lessons, reusable patterns, and decision pointers that should not be copied from the dev harness package. |

This tree itself is not copied into development repos.

## How To Use

Start at the intent docs, then walk downward through commitments, architecture, decisions, and implementation. Use `product-breakdown/02-architecture/architecture.md` as the canonical product architecture and `product-breakdown/03-implementation/implementation.md` as the artifact map. Reviewers should verify that changes preserve the chain in both directions: from implementation back to intent, and from intent down to the product-breakdown source docs in this repository.

For install, build, usage, verification command, and contributor workflow instructions, use `docs/`. Product-breakdown artifacts may link to those guides, but should not restate their step-by-step procedures.

For product breakdown work in copied target repos, agents should use `.opencode/dev_harness/product-breakdown/` as the runtime guidance because `product-breakdown/` is not copied into target repos.

When improvement work is active, `product-breakdown/06-evolution/candidates/` is the landing zone for backlog candidates before they become implementation work.

For guarded workflow control in copied target repos, agents should use `.opencode/dev_harness/workflow/` as the runtime policy source for stage applicability, waivers, information hygiene, and review output.

For durable workflow memory in this repository, agents should use `.opencode/dev_harness_memories/`. That directory is intentionally repo-local and is not part of the copied payload.

## Directory Structure

This tree follows the product-breakdown template layer numbering. Each numbered directory corresponds to a template layer:

- `product-breakdown/00-intent/` — Why does this product exist?
- `product-breakdown/01-product/` — What should it do?
- `product-breakdown/02-architecture/` — How is it structurally organized? (includes `decisions/` for architecture decisions)
- `product-breakdown/03-implementation/` — How is it built in code and configuration? (includes `decisions/` for implementation decisions)
- `product-breakdown/04-verification/` — How do we know it works?
- `product-breakdown/05-operation/` — What operational behavior and support constraints must the product satisfy?
- `product-breakdown/06-evolution/` — How should it change over time?
- `product-breakdown/decision-log.md` — Index of all decisions across layers

See `.opencode/dev_harness/product-breakdown/README.md` for the full layer definitions.
