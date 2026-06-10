# Large Job Guidelines — Pre-Execution Approval Thresholds

Use this artifact to help the planner classify a work order as a "larger job" that requires operator pre-approval before implementation begins.

## Classification Criteria

Any **single** criterion match triggers large-job classification (OR logic). When triggered, the planner must set `user_feedback_required: true`, present the matching details to the operator, and stop for approval.

### 1. File-Count Threshold

- **Threshold**: more than 10 files changed (>10 files touched).
- Count includes creates, modifications, moves, renames, and deletions.
- Exclude files that are purely informational (e.g., README edits, doc-only changes) when they are incidental to the core change.

### 2. Blast-Radius Categories

| Category | Definition |
|---|---|
| **Local** | Changes are confined to a single module, agent, or functional area with no side effects outside the module boundaries. |
| **Cross-module** | Changes span two or more modules, agents, or functional areas, introducing coordination risk or interface coupling. |
| **Destructive** | Changes alter existing behavior, data, schemas, or contracts in ways that may break dependent consumers or require migration. |

Large-job classification is triggered by **Cross-module** or **Destructive** blast radius.

### 3. Destructive-Operation Flag List

The following operations are always flagged as destructive:

- File or directory **renames** that break import paths, references, or symlinks
- File or directory **deletions** (not including temporary or generated files)
- **Schema changes**: data format changes, JSON/YAML structure changes, database schema changes, interface/API signature changes
- **Behavioral contract changes**: function signature rewrites, return type changes, error-handling contract modifications
- **Configuration renames or removals** that affect runtime behavior
- **Dependency upgrades or replacements** that may introduce incompatibility
- **Workflow or routing changes** that alter stage sequencing or agent invocation

### 4. Cost / Time Threshold

- **Threshold**: estimated execution time > 15 minutes.
- Estimate is based on the planner's risk assessment, scope size, and previous task duration patterns.
- When uncertain, assume the upper bound and flag conservatively.

## Small-Task Exemption

Tasks clearly below **all** of the above thresholds proceed without the pre-approval gate. The planner evaluates the criteria and, if none match, continues routing by emitting a non-large work order.

## Evaluation Procedure

1. Planner loads this artifact and the work order.
2. Planner counts files touched, checks blast-radius category, scans for destructive ops, and estimates time.
3. If any criterion matches:
   - Set `user_feedback_required: true`
   - Set `user_feedback_request` with the matching criteria and details
   - Stop, present to the operator, and wait for approval
4. If no criteria match:
   - Set `large_job_triggered: false`
   - Proceed to implementation routing
