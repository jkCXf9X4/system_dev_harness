# AD-004: Decline Adding Agent SKILLS To Primary Agents

## Status

Declined

## Context

An improvement evaluation proposed adding SKILLS declarations to agent definitions within `.opencode/agents/` to give agents specialized skill-based behavior. The evaluation assessed whether the project would benefit from agent SKILLS.

## Decision

Do NOT add SKILLS. The improvement evaluation found NO benefit. Adding SKILLS would create parallel responsibility structures and violate KM-004 (minimize parallel structures). The existing orchestrator primary-agent design with dedicated subagents for domain tasks is sufficient and should remain the canonical mechanism.

## Consequences

- Positive: Avoids architectural drift and maintenance overhead of dual context-delivery structures.
- Negative: Agents rely on their system prompt and available subagent routing for domain context; there is no shortcut for skill injection.

## Traceability

- Dev-harness workflow — declined SKILLS for agent definitions to uphold KM-004 guardrail.
