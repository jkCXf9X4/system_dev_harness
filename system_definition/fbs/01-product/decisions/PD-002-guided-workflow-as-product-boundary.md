# PD-002: Guided Workflow As Product Boundary

## Status

Accepted

## Layer

Product

## Context

The system_dev_harness package provides agent prompts, workflow policy, and system-definition context to support structured, traceable orchestration of LLM-based development work. The product scope could be defined narrowly (just the prompt files) or broadly (including the runtime execution platform, external build servers, or integration with third-party CI/CD services). An explicit product boundary was needed to focus development effort, limit blast radius, and keep the package portable.

## Decision

Define the system_dev_harness product boundary as the **guarded orchestrator workflow**:

- The product is the set of agent prompts, workflow policies, copied dev harness context, system-definition source documentation, and the sync mechanism that copies runtime context into target repositories.
- The product does NOT include: the OpenCode runtime platform, external build/CI/CD tooling, third-party MCP servers or skills, the operator's IDE environment, or any persistent infrastructure outside the repository.
- The primary product capability is the guarded delivery chain (planner → builder → reviewer → reflection → reporter) and the candidate-capture workflow mode.
- The product assumes it is deployed via `opencode.json` configuration in a target development repository, with the `.opencode/` directory copied as the runtime payload.

## Alternatives Considered

- **Full platform product**: Include OpenCode runtime, execution infrastructure, and external service integrations — increases maintenance burden, reduces portability, and expands blast radius for changes.
- **Prompt-only product**: Just the agent prompt files without workflow policy or system-definition context — insufficient for traceable, guarded delivery.
- **Sync tool only**: Just the Python sync CLI without prompt definitions — leaves the actual workflow behavior undefined.

## Consequences

**Positive:**
- Clear scope for development: only prompt, policy, context, and sync-mechanism files.
- Portable: deployable to any OpenCode-compatible repository without external infrastructure.
- Focused testing: verification targets the workflow behavior, not the runtime platform.
- Self-contained: all workflow behavior is inspectable from the repository.

**Negative:**
- Relies on OpenCode runtime to execute the prompts — product correctness is coupled to runtime behavior.
- Cannot control operator-side execution environment (model choice, temperature, tool permissions).
- External integrations (new MCP, skills, plugins) require explicit product decisions.

## Affected Artifacts

- `system_definition/README.md` — Scope and boundary documentation
- `system_definition/pbs/02-architecture/architecture.md` — Boundaries section
- `system_definition/pbs/03-implementation/implementation.md` — Mechanism storage rules
- `docs/` — Operator guidance references the guardrail model

## Verification

No system-definition artifact describes the product as including runtime infrastructure or external service dependencies. All agent prompts reference the guarded chain, not execution infrastructure.

## Review Trigger

When a proposed addition (new MCP server, skill integration, external service connector) would cross the defined product boundary, revisit whether the boundary needs extension or the addition should be documented as an operator responsibility.