# 01 Product Layer — FBS

This layer belongs to the **Functional Breakdown Structure (FBS)**. It captures durable product requirements and promises derived from the vision and use cases.

## Role in the Decomposition Model

| Aspect | Description |
| --- | --- |
| Decomposition role | FBS — Functional requirement nodes |
| Primary question | What should it do? |
| Downstream consumers | PBS architecture, implementation, verification |

## Contents

- `product-commitments.md` — Durable promises (PC-001 through PC-010) that should survive implementation changes

## Traceability

Each product commitment constrains one or more functions (F-01 through F-14) and traces to PBS elements in `02-architecture/` and `03-implementation/`.