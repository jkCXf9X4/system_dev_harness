# Known Mistakes

This file is persistent mistake memory for the OpenCode workflow. Add project-specific repeated failures here so future tasks can check against them.

Each lesson should be concrete enough to become a review check.

## Template

```text
### KM-000: Short title

Pattern:
What mistake tends to happen?

Why it matters:
What risk or rework does it cause?

Prevention rule:
What must future agents do differently?

Completion check:
How should reviewers verify this did not happen again?
```

## Current Lessons

### KM-001: Do Not Implement Plausible Partial Solutions

Pattern:
Agents may satisfy the most visible part of a task while leaving edge cases, integration points, documentation, or tests unfinished.

Why it matters:
The result looks complete but creates hidden follow-up work and repeated review cycles.

Prevention rule:
Every planner work order must include a completion checklist tied to the requirement contract.

Completion check:
Reviewers must verify each contract item is complete, explicitly waived, or blocking.

### KM-002: Do Not Ignore Architecture Constraints

Pattern:
Agents may choose the fastest local implementation even when it conflicts with existing architecture, patterns, or boundaries.

Why it matters:
Short-term progress creates long-term inconsistency and maintenance risk.

Prevention rule:
Every task must identify architecture constraints and forbidden shortcuts before coding handoff.

Completion check:
Architecture reviewer must confirm the implementation plan preserves integration boundaries and existing patterns.

### KM-003: Do Not Lose Track During Long Tasks

Pattern:
Agents may start aligned with the task but drift after several steps or corrections.

Why it matters:
The final output may no longer satisfy the original task contract.

Prevention rule:
External coding-agent handoff must require the agent to re-check the contract before final response.

Completion check:
Completeness reviewer must compare final work against the original contract, not only the latest local change.

### KM-004: Minimize Parallel Structures In Hierarchy And Code

Pattern:
Agents may create parallel package trees, duplicate entrypoints, or mirrored helper modules that solve the same concern in different places.

Why it matters:
Parallel structures make ownership unclear, increase maintenance cost, and cause future agents to update one path while missing the other.

Prevention rule:
Prefer one canonical hierarchy for each concern. Before adding a new top-level package, entrypoint, helper module, config path, or documentation section, check whether the existing structure should be extended or moved instead.

Completion check:
Reviewers must verify that new code and documentation do not introduce duplicate package roots, competing CLI paths, mirrored utilities, or parallel documentation locations for the same concept unless an ADR explicitly justifies the split.

### KM-005: Preserve Documentation Layer Separation And Backward Traceability

Pattern:
Agents may mix intent, commitments, architecture, decisions, implementation, and verification in the same artifact, or add trace links from higher-level documents down into lower-level implementation details.

Why it matters:
Mixed documentation layers make ownership unclear, cause higher-level product intent to churn with implementation changes, and make traceability harder to audit.

Prevention rule:
Keep the documentation chain separated: Intent -> Product Decisions -> System Architecture -> Technical Decisions -> Implementation -> Verification. Trace links should point backward to the layer being satisfied. Higher layers describe intent and constraints without linking down into lower-level implementation details.

Completion check:
Reviewers must verify that product vision captures intent, product commitments/decisions translate intent into durable product promises, system architecture describes stable guarantees and boundaries, technical decisions bridge architecture to build details, and implementation or verification artifacts trace backward to the requirement, decision, or architecture they satisfy.

### KM-006: Keep Folder Layout Hierarchical And Easy To Scan

Pattern:
Agents may scatter related files across multiple folders, use inconsistent naming, or add new locations without a clear parent-child relationship.

Why it matters:
Scattered folders make the project harder to navigate, hide the canonical location for a concern, and increase the chance that future changes land in the wrong place.

Prevention rule:
Group related artifacts under a single obvious home, keep naming consistent, and prefer a simple hierarchy over ad hoc folder growth. Before adding a new folder or top-level file, check whether the concern belongs in an existing directory or whether a named subfolder should be created for it.
If sequential order matters, prefer imposing that order at the folder level with numbering so the scan path matches the intended reading order.

Completion check:
Reviewers must verify that the repository has a clear folder hierarchy, that each artifact type has one obvious location, and that new files improve readability and findability instead of creating a second path for the same concern.

### KM-007: Clean Up Stale References After Moves Or Rewrites

Pattern:
Agents may move, rename, or rewrite information but leave behind obsolete links, duplicated copies, stale headings, or references to the old location or name.

Why it matters:
The repository ends up with conflicting sources of truth, broken navigation, and extra rework when future tasks follow stale references.

Prevention rule:
After moving or significantly rewriting information, update all in-repo references, remove duplicate or orphaned copies, and verify the old location or name no longer appears where it should not.

Completion check:
Reviewers must verify that moved or rewritten information has no stale references, obsolete links, or duplicate content left behind in the touched scope.

### KM-008: Avoid Orphaned Information Nodes

Pattern:
Agents may create or move artifacts without maintaining an obvious parent, child, or trace link in the information chain, leaving loose notes or isolated documents behind.

Why it matters:
Orphaned nodes are easy to miss, hard to classify, and often become stale because nothing points back to them or forward from them.

Prevention rule:
When creating, moving, or rewriting an artifact, assign it a clear source, purpose, and next-hop trace link in the chain. Prefer linking backward to the artifact or decision it satisfies and forward to the artifact it enables.

Completion check:
Reviewers must verify that touched artifacts are traceable to a parent context and that no loose, unlinked, or unowned artifact was introduced in the touched scope.
