# Review Output Protocol

Use this protocol for independent review stages.

Return exactly one status:

```text
pass
fail
needs_waiver
```

Include:

- findings with stable item ids
- brief evidence for each finding
- waiver request details when status is `needs_waiver`
- when memory is relevant, memory hygiene input evidence covering retrieved entries, revalidation status, stale or conflicting memory, new memory candidates for reflection, and whether memory influenced the review outcome

Use `fail` when evidence is missing, contradictory, or does not prove completion. Use `needs_waiver` only when the implementation is intentionally incomplete or risky and requires explicit user approval under `.opencode/dev_harness/workflow/control-policy.md`.
