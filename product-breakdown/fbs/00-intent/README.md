# 00 Intent Layer — FBS

This layer belongs to the **Functional Breakdown Structure (FBS)**. It explains why the product exists, who it serves, what problems it solves, and what success means.

## Role in the Decomposition Model

| Aspect | Description |
| --- | --- |
| Decomposition role | FBS — Functional architecture |
| Primary question | Why does this product exist? |
| Downstream consumers | PBS architecture, implementation, verification, operation |

## Contents

- `vision.md` — Core thesis, desired outcomes, and motivating principles
- `use-cases.md` — Actor definitions and workflow descriptions (UC-001 through UC-014)

## Traceability

FBS elements in this layer constrain all subsequent layers. Changes here should be traceable to PBS elements in `02-architecture/` and `03-implementation/`.