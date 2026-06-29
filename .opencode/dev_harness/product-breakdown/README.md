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
| Perform systems-engineering analysis | `architecture/interface-contracts.md`, `architecture/agent-state-machines.md`, `architecture/sequence-parametric.md`, `architecture/component-hierarchy.md` |
| Assess system risks | `verification/risk-framework.md` |
| Verify acceptance criteria | `verification/acceptance-criteria.md` |

## Core Rule

A decision belongs in the layer where its consequences are most directly felt.

Do not collect decisions in one central decisions directory. Keep decisions beside the artifacts they constrain, and maintain a root-level decision log only as an index.

## External References

This folder adapts concepts from the following standards for analytical use within the workflow. Descriptions are original summaries; for authoritative definitions, consult the standards directly.

- **ISO/IEC 15288** (ISO/IEC): Systems and software engineering — System life cycle processes. Referenced for staged pipeline concepts and verification/validation distinction.
- **INCOSE Systems Engineering Handbook, 5th Edition** (INCOSE): Referenced for product breakdown structure hierarchy conventions and verification pattern guidance.
- **OMG SysML** (Object Management Group): SysML is a trademark of OMG. Referenced for diagram-adapted text artifacts (BDD, IBD, state machines, sequence diagrams, parametric constraints).

## Expected Product Breakdown Tree

Each top-level folder below is a separate layer. Use the matching layer file for the compact description and the layer questions.

```text
product-breakdown/
  README.md
  decision-log.md
  traceability-map.md

  fbs/
    00-intent/
    01-product/
  pbs/
    02-architecture/
    03-implementation/
  cross-cutting/
    04-verification/
    05-operation/
    06-evolution/
```

Each layer may contain a local `decisions/` directory.

## Layer Questions

| Layer | Decomposition | Main question |
| --- | --- | --- |
| `fbs/00-intent/` | FBS | Why does this product exist? |
| `fbs/01-product/` | FBS | What should it do? |
| `pbs/02-architecture/` | PBS | How is it structurally organized? |
| `pbs/03-implementation/` | PBS | How is it built in code and configuration? |
| `cross-cutting/04-verification/` | Cross-cutting | How do we know it works? |
| `cross-cutting/05-operation/` | Cross-cutting | What operational behavior and support constraints must the product satisfy? |
| `cross-cutting/06-evolution/` | Cross-cutting | How should it change over time? |

## Layer Summary

| Layer | Decomposition | Use |
| --- | --- | --- |
| `fbs/00-intent/` | FBS | Capture purpose, users, outcomes, constraints, and assumptions. |
| `fbs/01-product/` | FBS | Capture scope, capabilities, use cases, requirements, domain, and glossary. |
| `pbs/02-architecture/` | PBS | Capture boundaries, components, data flow, integrations, deployment, and quality attributes. |
| `pbs/03-implementation/` | PBS | Capture code structure, modules, interfaces, configuration, and environments. |
| `cross-cutting/04-verification/` | Cross-cutting | Capture acceptance criteria, test strategy, test cases, and traceability. |
| `cross-cutting/05-operation/` | Cross-cutting | Capture operational requirements, support constraints, incident expectations, and deployment constraints; runnable procedures belong in `docs/`. |
| `cross-cutting/06-evolution/` | Cross-cutting | Capture roadmap, candidates, selected improvements, completed improvements, risks, changelog, and future change. |

## Agent Usage

0. For systems-engineering analysis, load the architecture artifacts (`architecture/interface-contracts.md`, `architecture/agent-state-machines.md`, `architecture/sequence-parametric.md`, `architecture/component-hierarchy.md`) and the risk framework (`verification/risk-framework.md`).
1. Identify the task layer before reading broadly.
2. Load that layer file and any directly linked support file.
3. If adding a decision, apply `decision-placement.md` before writing.
4. Update local artifacts first, then update the global indexes.
5. Keep traces explicit when an artifact affects downstream layers.
6. Put command examples, install steps, usage guides, and contributor workflow in `docs/`, linking back to product-breakdown artifacts for context.
