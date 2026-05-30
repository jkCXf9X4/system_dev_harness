# AD-001: Use OpenCode Agent Workflow For Orchestration

## Status

Accepted

## Context

The solution needs explicit workflow roles, controlled transitions, review gating, a guarded revision loop, and a way to separate exploratory improvement discovery from contained implementation while still allowing an explicit operator-chosen direct build path outside the orchestrator. A hidden runtime would make the process harder to inspect and harder to update.

## Decision

Use OpenCode's primary-agent and subagent model as the orchestration layer. Represent guarded development roles as markdown agents under `.opencode/agents/`, with repository instructions and the product-breakdown source docs providing shared context.

## Consequences

Benefits:

- workflow state is visible in repository files
- roles are versioned markdown
- permissions can be expressed per agent
- the solution stays OpenCode-native instead of embedding a separate runtime

Tradeoffs:

- orchestration behavior lives in agent prompts and config, not compiled code
- the workflow depends on OpenCode semantics
- changes to agent prompts must be reviewed like other solution artifacts

## Traceability

- Product commitments: PC-001, PC-002, PC-004, PC-005, PC-006, PC-007, PC-008, PC-009, PC-010
- Use cases: UC-001 through UC-013
