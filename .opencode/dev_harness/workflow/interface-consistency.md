# Interface Consistency Policy

Use this policy when a task modifies a shared interface surface. Centralizes the identification, verification, and review rules to avoid duplication across planner, contract, architecture, builder, and review-completeness agents.

## Interface Surface Definition

A shared interface surface is any of:

- exported function or method signature (name, parameters, return type)
- public type or data structure (struct fields, enum variants, type aliases)
- shared configuration schema or environment variable contract
- serialization contract (wire format, JSON/YAML shape, protocol buffer schema)
- message or event format (IPC payload, callback signature, webhook contract)
- module or package entrypoint (importable symbol, CLI command, plugin hook)

## The `touches_shared_interface` Control Flag

The planner sets `touches_shared_interface: true` in the work order control flags when the task touches one or more of the surfaces above.

When `touches_shared_interface` is true, the planner must also include an `interface_impact_statement` in the work order listing each touched surface and its known consumer files.

## Consumer Enumeration

When discovery is invoked and the task touches a shared interface, discovery must find all files that directly consume the changed interface. The planner includes the resolved consumer paths in the `interface_impact_statement`.

When discovery is not invoked, the planner enumerates consumers itself using repository search.

## Contract Fields

When `touches_shared_interface` is true, the contract agent must produce these fields:

- `interface_surfaces_touched`: list of public API, exported types, config schemas, serialization contracts, or message formats the task modifies
- `known_consumers`: files that consume each touched interface surface, as identified by discovery
- `backward_compatibility_requirements`: explicit acceptance criteria for each changed interface
- `interface_test_obligation`: criterion that each touched interface is verified against its consumers

When no shared interface is touched, all fields above use `none`.

## Builder Verification Procedure

When `touches_shared_interface` is set in the work order, after implementation:

1. **Verify**: read every known consumer file and verify the modified interface remains consistent
2. **Fix**: invoke `orchestrator-cleanup` to fix any interface mismatches found in consumer files, keeping fixes inside the approved scope
3. **Escalate**: if a mismatch cannot be resolved without expanding scope, surface it as a blocking finding rather than silently leaving the mismatch

Report the result in the builder evidence using this taxonomy:

- `consistent` — all consumers verified, no mismatches
- `mismatches_found_and_fixed` — mismatches existed but were resolved via cleanup
- `mismatches_unresolved` — mismatches exist and could not be resolved within scope (blocking)
- `not_applicable` — when `touches_shared_interface` is not set

## Reviewer Mismatch Check

When the work order or contract includes `touches_shared_interface` or an `interface_impact_statement`, the completeness reviewer must check for these patterns:

1. **Silent signature breaks**: function signatures changed without updating all callers
2. **Semantic consumer mismatches**: data structures modified without updating consumers' expectations
3. **Missing interface documentation**: interface specs or docs not updated to match semantic changes
4. **False minimalism**: a minimal change that shifts interface burden onto other modules instead of updating them

Fail on silent interface breaks, semantic mismatches, missing interface documentation updates, or shifted interface burden.

## Architecture Ripple Analysis

When `touches_shared_interface` is true, the architecture agent must produce:

- `ripple_analysis`: for each changed interface surface, assess which modules or layers could break silently, considering both compile-time and semantic contract compatibility; use `none` when no shared interface is touched
- `interface_risk_level`: `none | low | medium | high` with rationale
- `interface_risk_details`: specific risks per touched interface surface, or `none`