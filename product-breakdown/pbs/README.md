# PBS — Product Breakdown Structure

This directory groups artifacts that describe **how the system is structured** — the physical decomposition of the System of Interest (SoI). Per INCOSE §2.3.4.1, the PBS decomposes the SoI into successively lower-level details of its physical architecture.

## Contents

| Layer | Description |
| --- | --- |
| `02-architecture/` | Architecture control flow, boundaries, decisions, and verification criteria |
| `03-implementation/` | Implementation artifacts, artifact map, and implementation-level decisions |

## Relationship to FBS

- PBS artifacts describe **physical** architecture (agents, files, directories, decisions).
- FBS artifacts describe **functional** requirements and constraints.
- Each PBS element should trace back to one or more FBS elements.

## Links

- [FBS directory](../fbs/README.md) — functional architecture
- [Cross-cutting directory](../cross-cutting/README.md) — transversal artifacts
- [Breakdown structures](../breakdown-structures.md) — FBS/PBS/WBS relationship model