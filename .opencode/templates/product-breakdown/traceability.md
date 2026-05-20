# Traceability Guidance

Traceability connects intent, product behavior, architecture, implementation, and verification.

Use this chain when adding or reviewing artifacts:

```text
Intent
  -> Product capability
    -> Use case
      -> Requirement
        -> Decision
          -> Architecture artifact
            -> Implementation artifact
              -> Test or verification artifact
```

Example:

```text
OUT-001 Improve team coordination
  -> CAP-001 Project collaboration
    -> UC-003 Invite collaborator
      -> REQ-021 Assign project role
        -> PD-004 Users manage access through roles
          -> AD-003 Authorization is handled by the project module
            -> modules/authorization.md
              -> TEST-PERM-001 Permission matrix tests
```

## Where To Record Links

- Use `traceability-map.md` for broad cross-layer maps.
- Use `04-verification/traceability-matrix.md` for requirement-to-test coverage.
- Use each decision's `Affected Artifacts` section for local downstream impact.

## Agent Checklist

- Does every new capability trace to intent or an accepted product choice?
- Does every durable architecture or implementation choice trace to a product need or constraint?
- Does every requirement have a verification path?
- Are deferred items captured in `06-evolution/` instead of being left implicit?
