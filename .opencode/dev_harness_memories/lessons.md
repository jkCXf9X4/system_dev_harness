# Lessons Memory

This file is repo-local workflow memory. It is intentionally stored outside the copied dev-harness tree so package updates do not overwrite it.

Each lesson should be concrete enough to become a review check.

## Template

```text
### KM-000: Short title

Metadata:
Scope:
Source:
Last verified:
Confidence:
Revalidation trigger:
Environment notes:

Decision pointer:

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

Metadata:
Scope: delivery and review
Source: repeated workflow tuning and review cycles
Last verified: 2026-06-01
Confidence: high
Revalidation trigger: whenever a task feels mostly done before all contract items, checks, and cleanup are verified
Environment notes: applies to guarded workflow tasks in any repository

Decision pointer: Reviewers must verify each contract item is complete, explicitly waived, or blocking.

Pattern:
Agents may satisfy the most visible part of a task while leaving edge cases, integration points, documentation, or tests unfinished.

Why it matters:
The result looks complete but creates hidden follow-up work and repeated review cycles.

Prevention rule:
Every planner work order must include a completion checklist tied to the requirement contract.

Completion check:
Reviewers must verify each contract item is complete, explicitly waived, or blocking.

### KM-002: Do Not Ignore Architecture Constraints

Metadata:
Scope: planning, architecture, and review
Source: repeated workflow tuning and architecture review
Last verified: 2026-06-01
Confidence: high
Revalidation trigger: whenever a task could tempt the agent to take the locally easiest implementation path
Environment notes: applies to module-boundary, dependency-shape, and responsibility-shape changes

Decision pointer: Architecture reviewer must confirm the implementation plan preserves integration boundaries and existing patterns.

Pattern:
Agents may choose the fastest local implementation even when it conflicts with existing architecture, patterns, or boundaries.

Why it matters:
Short-term progress creates long-term inconsistency and maintenance risk.

Prevention rule:
Every task must identify architecture constraints and forbidden shortcuts before coding handoff.

Completion check:
Architecture reviewer must confirm the implementation plan preserves integration boundaries and existing patterns.

### KM-003: Do Not Lose Track During Long Tasks

Metadata:
Scope: delivery and completion review
Source: repeated workflow tuning and revision loops
Last verified: 2026-06-01
Confidence: high
Revalidation trigger: whenever a task spans multiple iterations, corrections, or reviewer revisions
Environment notes: applies to guarded workflows with revision input

Decision pointer: Completeness reviewer must compare final work against the original contract, not only the latest local change.

Pattern:
Agents may start aligned with the task but drift after several steps or corrections.

Why it matters:
The final output may no longer satisfy the original task contract.

Prevention rule:
External coding-agent handoff must require the agent to re-check the contract before final response.

Completion check:
Completeness reviewer must compare final work against the original contract, not only the latest local change.

### KM-004: Minimize Parallel Solutions In Hierarchy And Code

Metadata:
Scope: documentation and implementation
Source: repeated repository hygiene and navigation issues
Last verified: 2026-06-01
Confidence: high
Revalidation trigger: before adding a second path for the same concern, file type, or helper
Environment notes: especially relevant when creating package roots, entrypoints, or mirrored documentation trees

Pattern:
Agents may create parallel package solutions, duplicate entrypoints, or mirrored helper modules that solve the same concern in different places.

Why it matters:
Parallel solutions make ownership unclear, increase maintenance cost, and cause future agents to update one path while missing the other.

Prevention rule:
Prefer one canonical solution for each concern. Before adding a new top-level package, entrypoint, helper module, config path, or documentation section, check whether the existing artifacts should be extended or moved instead.

Completion check:
Reviewers must verify that new code and documentation do not introduce duplicate package roots, competing CLI paths, mirrored utilities, or parallel documentation locations for the same concept unless an ADR explicitly justifies the split.

### KM-005: Preserve Abstraction Separation And Backward Traceability

Metadata:
Scope: system-definition and documentation maintenance
Source: repeated documentation layering and traceability issues
Last verified: 2026-06-01
Confidence: high
Revalidation trigger: whenever a change touches multiple documentation layers or trace links
Environment notes: applies to intent, product, architecture, implementation, and verification artifacts

Pattern:
Agents may mix intent, commitments, architecture, decisions, implementation, and verification in the same artifact, or add trace links from higher-level documents down into lower-level implementation details.

Why it matters:
Mixed documentation layers make ownership unclear, cause higher-level product intent to churn with implementation changes, and make traceability harder to audit.

Prevention rule:
Keep the documentation chain separated: Intent -> Product Decisions -> System Architecture -> Technical Decisions -> Implementation -> Verification. Trace links should point backward to the layer being satisfied. Higher layers describe intent and constraints without linking down into lower-level implementation details.

Completion check:
Reviewers must verify that product vision captures intent, product commitments/decisions translate intent into durable product promises, system architecture describes stable guarantees and boundaries, technical decisions bridge architecture to build details, and implementation or verification artifacts trace backward to the requirement, decision, or architecture they satisfy.

### KM-006: Keep Folder Layout Hierarchical And Easy To Scan

Metadata:
Scope: repository organization and documentation structure
Source: repeated navigation and file-placement issues
Last verified: 2026-06-01
Confidence: high
Revalidation trigger: whenever a new top-level folder or peer path is proposed
Environment notes: applies to source docs, copied runtime context, and local memory

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

Metadata:
Scope: content maintenance and cleanup
Source: repeated move/rename/rewrite hygiene issues
Last verified: 2026-06-01
Confidence: high
Revalidation trigger: after any move, rename, rewrite, replacement, or deletion that changes the canonical location or wording
Environment notes: applies to markdown docs, prompts, and tracker files

Pattern:
Agents may move, rename, or rewrite information but leave behind obsolete links, duplicated copies, stale headings, or references to the old location or name.

Why it matters:
The repository ends up with conflicting sources of truth, broken navigation, and extra rework when future tasks follow stale references.

Prevention rule:
After moving or significantly rewriting information, update all in-repo references, remove duplicate or orphaned copies, and verify the old location or name no longer appears where it should not.

Completion check:
Reviewers must verify that moved or rewritten information has no stale references, obsolete links, or duplicate content left behind in the touched scope.

### KM-008: Avoid Orphaned Information Nodes

Metadata:
Scope: documentation, traceability, and repository hygiene
Source: repeated information-chain gaps
Last verified: 2026-06-01
Confidence: high
Revalidation trigger: whenever a new artifact is created, moved, or replaced without an obvious parent or downstream destination
Environment notes: applies to traceable markdown artifacts and backlog entries

Pattern:
Agents may create or move artifacts without maintaining an obvious parent, child, or trace link in the information chain, leaving loose notes or isolated documents behind.

Why it matters:
Orphaned nodes are easy to miss, hard to classify, and often become stale because nothing points back to them or forward from them.

Prevention rule:
When creating, moving, or rewriting an artifact, assign it a clear source, purpose, and next-hop trace link in the chain. Prefer linking backward to the artifact or decision it satisfies and forward to the artifact it enables.

Completion check:
Reviewers must verify that touched artifacts are traceable to a parent context and that no loose, unlinked, or unowned artifact was introduced in the touched scope.

### KM-009: Verify Interface Consistency On Shared Boundaries

Metadata:
Scope: planning, delivery, and completeness review
Source: repeated interface-mismatch regressions in minimal-edit workflows
Last verified: 2026-06-30
Confidence: high
Revalidation trigger: whenever a task modifies an exported function, public type, shared config, serialization contract, or message format
Environment notes: applies to any task where `touches_shared_interface` is set in the planner work order

Decision pointer:
Planner must set `touches_shared_interface: true` when the task touches a shared boundary; builder must verify all known consumers remain consistent; reviewer must check for silent breaks, semantic mismatches, and shifted interface burden.

Pattern:
Agents implementing a minimal change to a shared interface may update only the direct target of the change while leaving callers, consumers, interface docs, and downstream modules inconsistent with the new contract.

Why it matters:
Minimal-edit implementations on shared interfaces are a recurring source of regressions. The changed interface appears complete in isolation but silently breaks consumers, causing cascading failures in later tasks.

Prevention rule:
Apply `.opencode/dev_harness/workflow/interface-consistency.md` for the builder verification procedure and reviewer mismatch checks.

Completion check:
Reviewers must verify that every changed interface surface has been checked against all known consumers, that no callers were silently broken, and that the interface-consumer verification result is documented in the builder evidence.

### KM-010: Reference Workflow Files Instead Of Duplicating Rules In Agent Prompts

Metadata:
Scope: agent-prompt maintenance and workflow hygiene
Source: completed context-minimization delivery run across all dev_harness agent prompts
Last verified: 2026-06-30
Confidence: medium (first-hand evidence from a single delivery run)
Revalidation trigger: agent prompts are restructured or workflow reference files under `.opencode/dev_harness/workflow/` are reorganized
Environment notes: applies to the dev_harness workflow agent prompts; does not apply to canonical locations (`instructions.md`, `orchestrator.md`) where the rule originated

Decision pointer:
When removing a duplicated rule from an agent prompt, first verify the rule still exists in the canonical workflow reference file. The canonical location is authoritative, not the copy.

Pattern:
Agents may duplicate behavioral rules, constraints, or guardrails that already exist in canonical workflow reference files (under `.opencode/dev_harness/workflow/`) into individual agent prompts instead of referencing the canonical source.

Why it matters:
Duplication causes:
- Context bloat in agent prompts, increasing token usage and cognitive load
- Inconsistency when the canonical rule is updated but copies are not, leading to contradictory directives
- Confusion about which version is authoritative, undermining the workflow hierarchy

Prevention rule:
When a rule, constraint, or behavioral guardrail already exists in a canonical workflow reference file under `.opencode/dev_harness/workflow/`, agent prompts should reference that file rather than duplicate the rule. Before adding a rule to an agent prompt, check whether it is already defined in a canonical location. If it is, remove the duplication and add a reference or rely on the orchestrated inclusion mechanism.

Completion check:
Reviewers must verify that any rule, constraint, or guardrail appearing in an agent prompt is not a verbatim or near-verbatim duplicate of content already present in a canonical workflow reference file. Evidence of the duplicate-check and the canonical reference location must be documented.
