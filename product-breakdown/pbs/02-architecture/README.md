# 02 Architecture Layer — PBS

This layer belongs to the **Product Breakdown Structure (PBS)**. It describes the stable system structure that supports the product: agents, control flow, boundaries, permissions, and mechanisms.

## Role in the Decomposition Model

| Aspect | Description |
| --- | --- |
| Decomposition role | PBS — Physical architecture |
| Primary question | How is it structurally organized? |
| Upstream sources | FBS: intent layers (00-intent, 01-product) |

## Contents

- `architecture.md` — Control flow, stable concepts, boundaries, completion model, persistence mechanisms
- `verification.md` — Architecture-scoped acceptance criteria (horizontal verification view)
- `decisions/` — Architecture-level decision records (AD-001 through AD-005)

## Traceability

Architecture elements trace back to functional requirements (PC-001 through PC-010) and use cases (UC-001 through UC-014). Implementation artifacts in `03-implementation/` realize the architecture.