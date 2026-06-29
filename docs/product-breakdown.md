# Product Breakdown

The source documentation tree stays in `product-breakdown/`. The copied runtime guidance lives in `.opencode/dev_harness/product-breakdown/`.

Use product-breakdown pages for product facts, scope, stable decisions, traceability, acceptance criteria, operational constraints, and evolution direction. Use the rest of `docs/` for runnable instructions, command examples, install and deploy steps, contributor workflow, and troubleshooting.

If an operator guide needs product context, link to these product-breakdown pages. If a product-breakdown page needs practical steps, link back to the relevant guide instead of copying the procedure.

## Source Map

- [Intent (FBS)](../product-breakdown/fbs/00-intent/vision.md)
- [Use Cases (FBS)](../product-breakdown/fbs/00-intent/use-cases.md)
- [Product Commitments (FBS)](../product-breakdown/fbs/01-product/product-commitments.md)
- [Architecture (PBS)](../product-breakdown/pbs/02-architecture/architecture.md)
- [Implementation (PBS)](../product-breakdown/pbs/03-implementation/implementation.md)
- [Verification (Cross-cutting)](../product-breakdown/cross-cutting/04-verification/acceptance-criteria.md)
- [Operation (Cross-cutting)](../product-breakdown/cross-cutting/05-operation/runbook.md)
- [Evolution (Cross-cutting)](../product-breakdown/cross-cutting/06-evolution/roadmap.md)
- [Decision Log](../product-breakdown/decision-log.md)
- [Traceability Map](../product-breakdown/traceability-map.md)

## Read Order

Start at intent, then move through product, architecture, implementation, verification, operation, and evolution. That keeps the traceability chain easy to follow in both directions.
