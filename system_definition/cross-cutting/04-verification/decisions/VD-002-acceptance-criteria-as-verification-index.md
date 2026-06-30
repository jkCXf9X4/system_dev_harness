# VD-002: Acceptance Criteria As Verification Index

## Status

Accepted

## Layer

Verification

## Context

The verification layer contains multiple verification artifacts: centralized acceptance criteria, per-layer verification files, per-layer decision records, a test strategy document, and a traceability matrix. Without a designated authoritative source, there is a risk of criteria duplication, conflicting requirements, or orphaned verification expectations. Agents and maintainers need a single entry point to determine what must be verified.

## Decision

Designate `system_definition/cross-cutting/04-verification/acceptance-criteria.md` as the authoritative verification index for the system:

- It defines the overall verification approach and method.
- It lists all centralized acceptance criteria (AC-*).
- It lists and describes all per-layer verification artifacts.
- It is the source of truth for what must be verified and how.
- Per-layer verification.md files extract and scope criteria from this index.
- Decision records (VD-*) in this layer document the rationale for verification method choices.

All other verification artifacts (test-strategy.md, traceability-matrix.md) reference back to this index but do not override it.

## Alternatives Considered

- **Test-strategy.md as index**: Documents how testing is structured but not what must be verified — a method document, not a criteria document.
- **Traceability-matrix.md as index**: Satisfies the requirement-to-test mapping need but does not define acceptance criteria.
- **No authoritative index**: Criteria distributed across files without a designated entry point — risk of gaps and duplication.

## Consequences

**Positive:**
- Clear entry point for verification questions: agents and maintainers load acceptance-criteria.md first.
- Per-layer files stay scoped while the central index provides completeness.
- Criteria additions and changes have a single source of truth.

**Negative:**
- acceptance-criteria.md must be updated whenever a new criterion is added at any layer.
- Per-layer verification files must remain consistent with the central index.

## Affected Artifacts

- `system_definition/cross-cutting/04-verification/acceptance-criteria.md` — Authoritative index
- All per-layer `verification.md` files — Extract from and reference this index
- `system_definition/cross-cutting/04-verification/test-strategy.md` — References this index
- `system_definition/cross-cutting/04-verification/traceability-matrix.md` — References this index

## Verification

Every verification criterion in the system appears in acceptance-criteria.md. Per-layer verification files cross-reference criteria back to acceptance-criteria.md, not create independent criteria sets.

## Review Trigger

When a per-layer verification.md adds a criterion that is not listed in the centralized index, or when the acceptance-criteria.md diverges from observable verification practice.