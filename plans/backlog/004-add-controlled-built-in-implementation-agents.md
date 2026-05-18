# Task: Add Controlled Built-In Implementation Agents

Status: todo

Goal:
Add built-in code-editing support behind explicit approval, with narrow write scope and reviewable evidence.

Current state:
- The harness only supports external execution adapters.
- It does not write to the repository directly.
- There is no built-in implementation agent.

Scope:
- Add an explicit approval step before any write operation.
- Restrict edits to a narrow, declared file scope.
- Require tests or an explicit test gap statement.
- Capture changed files, diffs, and execution evidence.
- Keep rollback and review guidance attached to the task.

Out of scope:
- Unrestricted autonomous repository edits.
- Broad destructive commands.

Acceptance criteria:
- The harness can produce a controlled edit plan or write packet.
- The edit flow requires approval before repository mutation.
- The resulting task output includes bounded scope, test expectations, and rollback guidance.
- The implementation remains traceable back to the contract and review output.

