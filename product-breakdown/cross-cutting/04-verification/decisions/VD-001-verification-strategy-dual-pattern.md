# VD-001: Verification Strategy Dual Pattern

## Status

Accepted

## Layer

Verification

## Context

The system_dev_harness product uses a layered product-breakdown structure (FBS/PBS/cross-cutting) with seven layers (intent, product, architecture, implementation, verification, operation, evolution). Initial verification documentation was centralized in a single acceptance-criteria.md file. As the system grew, per-layer verification requirements became tightly coupled to central criteria, making it difficult to add layer-specific details without overloading the central file.

## Decision

Adopt a dual INCOSE-aligned verification pattern:

- **Centralized strategy** (`cross-cutting/04-verification/acceptance-criteria.md`): Defines the overall verification approach, methods, cross-cutting concerns, and the authoritative index of all verification criteria.
- **Per-layer verification artifacts**: Each FBS/PBS/cross-cutting layer contains a local `verification.md` that extracts and scopes the criteria relevant to that element. These per-layer artifacts are authoritative for their element.

The centralized file serves as the entry point and cross-reference index. Per-layer files contain the detailed verification criteria applicable to that layer's artifacts.

## Alternatives Considered

- **Fully centralized verification**: All criteria in one file — becomes unwieldy as the product grows; no layer-specific scoping.
- **Fully distributed verification**: Each layer owns its criteria without a central index — makes cross-layer verification gaps harder to detect.
- **Test files only**: Rely on automated tests without document-level verification criteria — insufficient for architectural and process-level verification.

## Consequences

**Positive:**
- Each layer can be verified independently against its own criteria.
- Central index prevents gaps and duplication.
- Aligns with INCOSE horizontal verification views.
- Per-layer files can be loaded on demand by agents working in that layer.

**Negative:**
- Requires maintenance discipline to keep centralized and per-layer criteria in sync.
- Cross-layer criteria must be explicitly listed in each relevant layer's verification.md.

## Affected Artifacts

- `product-breakdown/cross-cutting/04-verification/acceptance-criteria.md` — Centralized authority
- `product-breakdown/fbs/00-intent/verification.md` — Intent layer extraction
- `product-breakdown/fbs/01-product/verification.md` — Product layer extraction
- `product-breakdown/pbs/02-architecture/verification.md` — Architecture layer extraction
- `product-breakdown/pbs/03-implementation/verification.md` — Implementation layer extraction
- `product-breakdown/cross-cutting/05-operation/verification.md` — Operation layer extraction
- `product-breakdown/cross-cutting/06-evolution/verification.md` — Evolution layer extraction

## Verification

Every FBS/PBS/cross-cutting layer directory contains a verification.md file. Each per-layer verification.md cross-references its criteria back to the centralized acceptance-criteria.md.

## Review Trigger

When a new layer is added to the product breakdown without a corresponding verification.md, or when criteria drift between centralized and per-layer files exceeds a threshold.