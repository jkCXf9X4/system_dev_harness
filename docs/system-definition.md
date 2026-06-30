# System Definition

The source documentation tree stays in `system_definition/`. The copied runtime guidance lives in `.opencode/dev_harness/system_definition/`.

Use system-definition pages for product facts, scope, stable decisions, traceability, acceptance criteria, operational constraints, and evolution direction. Use the rest of `docs/` for runnable instructions, command examples, install and deploy steps, contributor workflow, and troubleshooting.

If an operator guide needs product context, link to these system-definition pages. If a system-definition page needs practical steps, link back to the relevant guide instead of copying the procedure.

## Source Map

- [Intent (FBS)](../system_definition/fbs/00-intent/vision.md)
- [Use Cases (FBS)](../system_definition/fbs/00-intent/use-cases.md)
- [Product Commitments (FBS)](../system_definition/fbs/01-product/product-commitments.md)
- [Architecture (PBS)](../system_definition/pbs/02-architecture/architecture.md)
- [Implementation (PBS)](../system_definition/pbs/03-implementation/implementation.md)
- [Verification (Cross-cutting)](../system_definition/cross-cutting/04-verification/acceptance-criteria.md)
- [Operation (Cross-cutting)](../system_definition/cross-cutting/05-operation/runbook.md)
- [Evolution (Cross-cutting)](../system_definition/cross-cutting/06-evolution/roadmap.md)
- [Decision Log](../system_definition/decision-log.md)
- [Traceability Map](../system_definition/traceability-map.md)

## Read Order

Start at intent, then move through product, architecture, implementation, verification, operation, and evolution. That keeps the traceability chain easy to follow in both directions.
