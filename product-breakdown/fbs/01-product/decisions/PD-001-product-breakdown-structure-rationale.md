# PD-001: Product Breakdown Structure Rationale

## Status

Accepted

## Layer

Product

## Context

The system_dev_harness workflow package requires a structured approach to documenting product intent, architecture, implementation, verification, operation, and evolution decisions. The initial product breakdown documentation was organized in a flat directory structure without clear separation between functional requirements (FBS), physical/structural design (PBS), and transversal concerns. As the workflow grew to include multiple agent types, helper stages, and improvement candidates, the lack of a formal decomposition model made it difficult to trace decisions across layers, identify gaps, and maintain consistency.

## Decision

Adopt a three-way product breakdown decomposition for documentation source:

- **FBS (Functional Breakdown Structure)**: Captures intent and product-layer artifacts — vision, use cases, scope, capabilities, requirements, domain concepts, and product-level decisions.
- **PBS (Product Breakdown Structure)**: Captures physical/structural layers — architecture boundaries, implementation maps, and their respective decisions.
- **Cross-cutting layers**: Capture transversal concerns — verification, operation, and evolution artifacts that span both FBS and PBS.

Each layer is documented in a dedicated directory under `product-breakdown/` and maintains its own local `decisions/` directory for layer-specific decision records.

## Alternatives Considered

- **Flat decision log**: All decisions in a single file — loses layer context and makes traceability harder as the system grows.
- **Single decomposition model (FBS-only)**: Captures functional intent but does not distinguish physical implementation structure and transversal concerns.
- **Single decomposition model (PBS-only)**: Captures structural hierarchy but loses functional intent traceability from user needs to implementation.
- **No formal decomposition**: Relies on implicit conventions — unsustainable beyond a small set of artifacts.

## Consequences

**Positive:**
- Clear separation of concerns between what the product should do (FBS), how it is built (PBS), and how it is verified/operated/evolved (cross-cutting).
- Localized decision storage keeps each layer self-contained while the global decision-log.md serves as a cross-layer index.
- Supports INCOSE-aligned product tree visualization.
- New artifacts can be placed with clear parent context.

**Negative:**
- Requires discipline to place new artifacts in the correct layer.
- Cross-layer concerns (e.g., a verification criterion that references implementation) must be explicitly traced between layer boundaries.

## Affected Artifacts

- `product-breakdown/README.md` — describes the decomposition model
- `product-breakdown/breakdown-structures.md` — formal FBS-PBS-WBS relationship model
- `product-breakdown/product-tree.md` — hierarchical product tree visualization
- `product-breakdown/decision-placement.md` — placement rules reference layer model
- All layer README files under `fbs/`, `pbs/`, and `cross-cutting/`

## Verification

The directory structure matches the decomposition model described in product-breakdown/README.md. Every artifact file exists in a directory matching its layer classification. The product-tree.md Mermaid diagram correctly reflects the on-disk structure.

## Review Trigger

When a new artifact type is proposed that does not clearly fit into one of the three decomposition categories, or when the directory structure diverges from the documented model, revisit and clarify the placement rules.