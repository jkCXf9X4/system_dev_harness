# FBS — Functional Breakdown Structure

This directory groups artifacts that describe **what the system does** and **why** — the functional decomposition of the System of Interest (SoI). Per INCOSE §2.3.4.1, the FBS decomposes the functions of the required SoI into successively lower levels of its functional architecture.

## Contents

| Layer | Description |
| --- | --- |
| `00-intent/` | Vision, use cases — why the solution exists, what problems it solves, which actors and workflows it supports |
| `01-product/` | Product commitments — durable promises derived from the intent, bridging functional intent and physical architecture |

## Relationship to PBS

- FBS artifacts describe **functional** requirements and constraints.
- PBS artifacts describe **physical** architecture (agents, files, directories).
- Traceability between FBS and PBS is maintained through `product-breakdown/traceability-map.md` and `product-breakdown/breakdown-structures.md`.

## Links

- [PBS directory](../pbs/README.md) — physical architecture
- [Cross-cutting directory](../cross-cutting/README.md) — transversal artifacts
- [Breakdown structures](../breakdown-structures.md) — FBS/PBS/WBS relationship model