# Execution Adapters

Execution adapters connect the harness control loop to external coding tools.

The harness remains responsible for:

- task contract
- architecture guardrails
- known mistake checks
- implementation handoff packet
- evidence intake
- independent reviewer agents
- deterministic gate

Adapters are responsible for:

- starting or preparing an external coding-agent session
- returning a session reference
- collecting available output as evidence

## Adapter Contract

```python
class ExecutionAdapter:
    def execute(self, handoff, *, title, workdir) -> ExecutionResult:
        ...
```

`ExecutionResult` contains:

- `session`: adapter name, session id, attach command, export command, transcript path
- `evidence`: changed files, diff summary, test output, agent output, waiver requests
- `raw_output`: unprocessed adapter output

## Manual Adapter

The manual adapter does not run a coding tool. It returns a session reference with instructions to paste the handoff packet into a coding agent.

Use it when:

- testing the harness flow
- using a tool without automation support
- manually controlling the coding session

```bash
python app.py --backlog examples/backlog_item.md --executor manual
```

## OpenCode Adapter

The opencode adapter runs `opencode run --format json` and captures stdout/stderr as agent output evidence.

Use it headlessly:

```bash
python app.py \
  --backlog examples/backlog_item.md \
  --executor opencode \
  --execution-mode headless
```

Use it with an existing opencode server:

```bash
opencode serve

python app.py \
  --backlog examples/backlog_item.md \
  --executor opencode \
  --opencode-attach http://localhost:4096
```

If a session id can be parsed from JSON events, the adapter records attach/export commands. If not, it creates a local fallback id and still stores raw output as evidence.

## User Interaction

The intended interactive flow is:

```text
harness creates handoff
  -> opencode starts/continues session
  -> user can attach to session
  -> opencode produces output
  -> harness reviews evidence
  -> deterministic gate approves, blocks, or requests waivers
```

The adapter boundary keeps the harness independent from opencode-specific session mechanics.
