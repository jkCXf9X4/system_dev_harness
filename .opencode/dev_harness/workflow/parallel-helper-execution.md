# Parallel Helper Execution

Use this policy when planner or reviewer helpers can run independently.

Planner and reviewer helpers should be grouped into parallel-safe helper packets whenever their inputs are available and their outputs do not depend on each other.

Apply `.opencode/dev_harness/workflow/subagent-lifecycle.md` before reusing helper context across packets or follow-up calls. Parallel helper packets are usually easiest to reason about as fresh, self-contained helper calls with compact handoffs.

Parallel-safe planner helpers are read-only and can run together when they inspect different concerns from the same user request and repository evidence. Typical parallel planning packets include discovery, contract, architecture, lessons, memory, researcher, and systems-engineering, unless one helper explicitly depends on another helper's output.

Parallel-safe reviewer helpers are read-only and can run together after builder evidence is available. Typical parallel review packets include verifier, review-completeness, review-architecture, review-lessons, memory, and researcher, unless a check needs another helper's result first.

Do not parallelize helper work when:

- a helper must consume another helper's output before it can produce useful evidence
- two helpers would write or mutate the same artifact
- the task requires a user clarification or waiver before helper work is meaningful
- external research must decide which files, checks, or standards another helper should inspect

Planner and reviewer outputs should include:

```text
parallel_helper_plan:
- packet_id: <short-id>
  helpers: <helper agents that can run together>
  dependencies: <packet IDs or none>
  reason: <why this packet is parallel-safe>
  expected_outputs: <evidence each helper must return>
```

Each helper disposition should report `parallel_safe: true|false`, `dependencies`, `file_write_set`, and `helper_lifecycle`. Read-only helpers normally use `file_write_set: none`.

Use the lifecycle values from `subagent-lifecycle.md`:

```text
helper_lifecycle:
  reuse_decision: reuse_existing|start_fresh|not_applicable
```
