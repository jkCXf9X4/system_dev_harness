# IMD-005: Rename product-breakdown/ to system_definition/

## Status

Accepted

## Context

The project had two directories named `product-breakdown/`:
- Root-level `product-breakdown/` — canonical product specification tree (FBS/PBS/cross-cutting layers)
- `.opencode/dev_harness/product-breakdown/` — runtime agent context with guidance copies

This naming caused persistent confusion:
- Agents and documentation needed to distinguish "canonical product-breakdown" from "runtime product-breakdown"
- New contributors and operators frequently confused the two directories
- The root-level name "product-breakdown" understated the tree's scope as a full system definition

## Decision

Rename:
- `product-breakdown/` → `system_definition/` (canonical source tree)
- `.opencode/dev_harness/product-breakdown/` → `.opencode/dev_harness/systems_engineering/` (runtime agent context)
- `docs/product-breakdown.md` → `docs/system-definition.md`

All internal cross-references were updated across ~73 files. The `product-breakdown-work.md` workflow policy filename and the `touches_product_breakdown` control flag were preserved as semantic identifiers.

## Consequences

Benefits:
- Clear naming: `system_definition/` for canonical source, `systems_engineering/` for SE-oriented runtime guidance
- Reduced confusion between the two directory trees
- SE terminology aligns with ISO 15288/INCOSE convention

Tradeoffs:
- 73+ files modified; potential for missed references
- External integrations referencing `product-breakdown/` paths must update
- Git history preserved via `git mv`

## Affected Artifacts

See the full catalog in Phase 2-7 of the rename implementation.

## Precedent Decisions

- PD-001: product-breakdown structure rationale
- IMD-002: copy product-breakdown guidance into agent payload
- IMD-004: copy architecture artifacts into agent payload

## Traceability

- Product commitments: PC-006, PC-007
- Architecture: renamed directory tree with preserved structure
- Implementation: this decision record
- Evolution: IMP-033 SE traceability evaluation