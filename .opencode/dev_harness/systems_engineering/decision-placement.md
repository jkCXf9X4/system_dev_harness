# Decision Placement

Use this rule when adding, moving, or reviewing a decision:

> Place the decision in the layer where its consequences are most directly felt.

The root `decision-log.md` is only an index. It should not own decision content.

## Placement Guide

| Decision effect | Location |
| --- | --- |
| Purpose, audience, success, constraints | `00-intent/decisions/` |
| Scope, capabilities, use cases, domain concepts | `01-product/decisions/` |
| System boundaries, components, data ownership, deployment shape | `02-architecture/decisions/` |
| Code structure, tools, frameworks, libraries, conventions | `03-implementation/decisions/` |
| Test strategy, acceptance criteria, validation methods | `04-verification/decisions/` |
| Deployment, monitoring, support, reliability, recovery | `05-operation/decisions/` |
| Roadmap, deferred scope, accepted risks, future change | `06-evolution/decisions/` |

## Multi-Layer Decisions

If a decision affects multiple layers:

1. Place it in the highest layer where the decision is introduced.
2. List downstream affected artifacts in the decision.
3. Add it to the global decision log.
4. Add traceability links where relevant.

Example:

```text
01-product/decisions/PD-004-users-manage-access-through-roles.md
```

This can affect:

```text
01-product/domain-model.md
01-product/use-cases/invite-collaborator.md
02-architecture/component-view.md
03-implementation/modules/authorization.md
04-verification/test-cases/permission-matrix.md
05-operation/audit-logging.md
```

It still belongs in product because the role model is primarily a product/domain decision.
