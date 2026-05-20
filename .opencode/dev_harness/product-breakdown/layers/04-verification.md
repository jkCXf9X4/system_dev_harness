# 04 Verification Layer

The verification layer explains how the product and system are proven to work.

## Typical Artifacts



```text
acceptance-criteria.md - states the conditions for product acceptance
test-strategy.md       - explains the overall verification approach
test-cases/            - contains concrete test scenarios and cases
traceability-matrix.md  - links requirements, tests, and evidence
decisions/             - stores verification-level decisions and rationale
```

## Questions Answered

- How do we know the product works?
- How are use cases verified?
- What types of tests are required?
- Which quality attributes need verification?
- How is traceability maintained?

## Example Decisions

```text
VD-001-use-use-case-level-acceptance-tests.md
VD-002-require-contract-tests-for-public-apis.md
VD-003-check-architecture-rules-in-ci.md
VD-004-maintain-a-requirement-to-test-traceability-matrix.md
```

Verification decisions affect acceptance tests, automated test coverage, manual validation, CI checks, and release confidence.
