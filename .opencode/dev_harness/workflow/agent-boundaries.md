# Agent Boundaries

Use this policy for agent read/write boundaries, scope containment, and no-edit responsibilities.

## Common Scope Rules

- Stay inside the approved work order or helper assignment.
- Do not broaden scope unless the planner work order is revised through the guarded workflow.
- Do not treat improvement candidates, memory candidates, waivers, or helper findings as permission to implement extra work.
- Preserve unrelated user changes and unrelated repository state.

## Read-Only Agents

These agents do not modify files: orchestrator, orchestrator-router, discovery, contract, architecture, lessons, memory, reviewer, verifier, review-architecture, review-completeness, review-lessons, researcher, systems-engineering, validation, reflection, and reporter.

Read-only agents should inspect only the minimum useful evidence for their role. When discovery has named exact files, helper agents should prefer those files over broad repository search.

## Limited-Write Agents

The planner may write only the current task's standardized plan summary under `.opencode/dev_harness_plans/`, as required by `.opencode/dev_harness/workflow/plan-summary-schema.md` and `.opencode/dev_harness/workflow/control-policy.md`. It must not edit implementation files, system-definition artifacts, runtime prompts, tests, or memory files.

## Modification Agents

The builder may modify files within the approved work order.

The build error resolver may modify only files needed to fix build, test, type-check, or dependency failures caused by the current implementation or explicitly assigned by the builder.

The cleanup helper may modify only stale references, trackers, indexes, duplicate or superseded content, orphaned artifacts, links, and traceability inside the builder-assigned scope.

The memory curator may modify only `.opencode/dev_harness_memories/lessons.md` and `.opencode/dev_harness_memories/patterns.md` unless the workflow memory policy is explicitly extended.

In `workflow_mode: candidate_capture`, the builder may write only improvement backlog artifacts allowed by `.opencode/dev_harness/workflow/candidate-capture.md`.

## No-Edit Reporting

Agents that cannot edit files should return blocking gaps, required follow-up, or `improvement_candidates` instead of silently changing artifacts.

## Interface Surface Boundaries

A shared interface surface is any of:

- exported function or method signature (name, parameters, return type)
- public type or data structure (struct fields, enum variants, type aliases)
- shared configuration schema or environment variable contract
- serialization contract (wire format, JSON/YAML shape, protocol buffer schema)
- message or event format (IPC payload, callback signature, webhook contract)
- module or package entrypoint (importable symbol, CLI command, plugin hook)

When a task touches one or more of these surfaces, the planner sets `touches_shared_interface: true` in the work order control flags and includes an `interface_impact_statement` listing each touched surface and its known consumer files. Procedural verification rules for interface consistency live in `.opencode/dev_harness/workflow/interface-consistency.md`.
