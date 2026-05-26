# Product Breakdown Agent Context

The product breakdown preserves intent, product behavior, architecture, implementation, verification, operation, and evolution as traceable layers.

Use this directory as small, load-on-demand context for product breakdown work.

## Boundary With `docs/`

Use `product-breakdown/` for product source information: intent, users, scope, capabilities, stable decisions, architecture, implementation mapping, verification expectations, operational product requirements, and evolution direction.

Use `docs/` for runnable guidance and concrete examples: install, build, deploy, usage, verification commands, troubleshooting, contributor workflow, and operator walkthroughs.

Do not duplicate the same example, command, or policy text in both places. If a guide needs product context, link to product-breakdown artifacts. If a product artifact needs practical steps, state the durable requirement and link to the relevant guide under `docs/`.

Load only the files needed for the current task:

| Need | Load |
| --- | --- |
| Work within one layer | `layers/<layer>.md` |
| Place or write a decision | `decision-placement.md`, `templates/decision-template.md` |
| Update decision indexes | `decision-log.md` |
| Connect intent to tests | `traceability.md` |
| Name artifacts consistently | `naming.md` |
| Create an improvement backlog | `layers/06-evolution.md`, `templates/improvement-backlog-overview-template.md`, `templates/improvement-candidate-template.md` |

## Core Rule

A decision belongs in the layer where its consequences are most directly felt.

Do not collect decisions in one central decisions directory. Keep decisions beside the artifacts they constrain, and maintain a root-level decision log only as an index.

## Expected Product Breakdown Tree

Each top-level folder below is a separate layer. Use the matching layer file for the compact description and the layer questions.

```text
product-breakdown/
  README.md
  decision-log.md
  traceability-map.md

  00-intent/
  01-product/
  02-architecture/
  03-implementation/
  04-verification/
  05-operation/
  06-evolution/
```

Each layer may contain a local `decisions/` directory.

## Layer Questions

| Layer | Main question |
| --- | --- |
| `00-intent/` | Why does this product exist? |
| `01-product/` | What should it do? |
| `02-architecture/` | How is it structurally organized? |
| `03-implementation/` | How is it built in code and configuration? |
| `04-verification/` | How do we know it works? |
| `05-operation/` | What operational behavior and support constraints must the product satisfy? |
| `06-evolution/` | How should it change over time? |

## Layer Summary

| Layer | Use |
| --- | --- |
| `00-intent/` | Capture purpose, users, outcomes, constraints, and assumptions. |
| `01-product/` | Capture scope, capabilities, use cases, requirements, domain, and glossary. |
| `02-architecture/` | Capture boundaries, components, data flow, integrations, deployment, and quality attributes. |
| `03-implementation/` | Capture code structure, modules, interfaces, configuration, and environments. |
| `04-verification/` | Capture acceptance criteria, test strategy, test cases, and traceability. |
| `05-operation/` | Capture operational requirements, support constraints, incident expectations, and deployment constraints; runnable procedures belong in `docs/`. |
| `06-evolution/` | Capture roadmap, candidates, selected improvements, completed improvements, risks, changelog, and future change. |

## Agent Usage

1. Identify the task layer before reading broadly.
2. Load that layer file and any directly linked support file.
3. If adding a decision, apply `decision-placement.md` before writing.
4. Update local artifacts first, then update the global indexes.
5. Keep traces explicit when an artifact affects downstream layers.
6. Put command examples, install steps, usage guides, and contributor workflow in `docs/`, linking back to product-breakdown artifacts for context.
