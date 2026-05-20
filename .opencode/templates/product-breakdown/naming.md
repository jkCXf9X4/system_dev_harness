# Naming Conventions

Use short, stable IDs for artifacts.

| Prefix | Meaning |
| --- | --- |
| `INT` | Intent |
| `OUT` | Outcome |
| `ASM` | Assumption |
| `CON` | Constraint |
| `CAP` | Capability |
| `UC` | Use case |
| `REQ` | Requirement |
| `PD` | Product decision |
| `AD` | Architecture decision |
| `IMD` | Implementation decision |
| `TD` | Technology decision |
| `VD` | Verification decision |
| `OD` | Operational decision |
| `ED` | Evolution decision |
| `RISK` | Risk |
| `TEST` | Test or verification artifact |

## Decision Filenames

Use lowercase kebab-case after the stable ID.

```text
PD-001-projects-are-the-primary-organizing-unit.md
AD-001-use-a-modular-monolith-for-v1.md
IMD-001-use-feature-folders-in-the-frontend.md
VD-001-use-use-case-level-acceptance-tests.md
OD-001-use-feature-flags-for-risky-releases.md
```
