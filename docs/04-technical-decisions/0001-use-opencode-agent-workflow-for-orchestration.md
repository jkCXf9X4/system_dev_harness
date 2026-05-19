# ADR-0001: Use OpenCode Agent Workflow For Orchestration

## Status

Accepted

## Context

The solution needs explicit workflow roles, controlled transitions, review gating, future support for interrupts and replay, and a way to separate exploratory improvement discovery from contained implementation. A hidden runtime would make the process harder to inspect and harder to update.

## Decision

Use OpenCode's primary-agent and subagent model as the orchestration layer. Represent guarded development roles as markdown agents under `.opencode/agents/`, with repository instructions and traceability docs providing shared context.

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

- Product commitments: PC-001, PC-002, PC-004, PC-005, PC-006, PC-007, PC-008, PC-009
- Use cases: UC-001 through UC-012
