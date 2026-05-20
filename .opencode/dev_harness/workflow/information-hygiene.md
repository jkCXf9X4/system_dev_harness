# Information Hygiene

Use this policy when work creates, moves, renames, rewrites, supersedes, or otherwise changes information artifacts.

## Required Evidence

Information hygiene evidence must cover:

- parent context for every new or changed artifact
- replaced or superseded information
- stale references checked or fixed
- duplicate content removed or reconciled
- orphaned artifacts checked or removed
- unresolved links checked or fixed
- traceability from source context to final artifact

## Stage Responsibilities

- Contract declares whether the task touches information artifacts and what hygiene evidence is required.
- Packet carries the required checks and affected artifacts to implementation.
- Builder performs cleanup and reports what changed.
- Verifier checks the evidence against the packet control flags.
- Reviewers fail missing, partial, or contradictory evidence.
- Gate blocks completion when required hygiene evidence is missing.
