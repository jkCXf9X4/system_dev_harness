# Roadmap

## Phase 0: Guarded Handoff CLI Harness

Status: current.

Scope:

- CLI input from markdown backlog item.
- LangGraph contract-driven workflow.
- OpenRouter model access.
- In-memory checkpointing.
- versioned markdown known-mistakes file.
- external coding-agent handoff packet.
- reviewer council and completion decision.
- Markdown final control report.
- Documentation structure and decision traceability.

Exit criteria:

- A user can run one development task through the workflow.
- The output is useful enough to paste into an external coding agent.
- The final report states approved, blocked, or waiver_required.
- Design decisions are documented.

## Phase 1: Better Inputs And Context

Scope:

- multiple input files
- repository summary context
- architecture document context
- stakeholder context files
- output artifact directory

Possible additions:

- `--context-file`
- `--output-dir`
- project profile config
- reusable requirement contract template
- reusable waiver template

## Phase 2: Human Approval Gates

Scope:

- explicit approval checkpoints
- interrupt/resume behavior
- editable state before continuing

Candidate gates:

- approve value framing
- approve first slice
- approve architecture constraints
- approve QA plan

## Phase 3: Durable Runs

Scope:

- durable checkpointer
- inspectable run history
- restart and resume
- compare prior runs

Candidate stores:

- SQLite for local single-user usage
- Postgres for team usage


## Phase 5: Controlled Built-In Implementation Agents

Scope:

- code-editing agent behind explicit approval
- narrow write scopes
- test execution
- review and rollback guidance

Safety constraints:

- no broad destructive commands
- file ownership per task
- required tests or explicit test gap statement
- generated PR brief tied back to the use case and requirements
