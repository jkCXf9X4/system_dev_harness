# System Dev Harness

A guarded agentic development harness starter that uses:

- LangGraph for explicit workflow control and state.
- OpenRouter as the OpenAI-compatible model access layer.
- Role-based support agents for requirement contracts, architecture guardrails, known mistake checks, implementation handoff, and reviewer approval.

The harness is designed to keep agentic development on track. It focuses on preventing shortcuts, partial implementations, lost requirements, architecture drift, and repeated mistakes. It does not edit code directly yet; instead it produces strict implementation packets for external coding agents such as Codex or opencode.

## Documentation

Start here for the broader product and engineering intent:

- [Documentation Index](docs/README.md)
- [Plans](plans/README.md)
- [Intent](docs/01-intent/README.md)
- [Product Commitments](docs/02-product-commitments/README.md)
- [System Architecture](docs/03-system-architecture/README.md)
- [Technical Decisions](docs/04-technical-decisions/README.md)
- [Implementation](docs/05-implementation/README.md)
- [Verification](docs/06-verification/README.md)
- [Lessons](docs/07-lessons/README.md)

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pip install -e .
cp .env.example .env
```

Edit `.env` and set `OPENROUTER_API_KEY`.

## Run

```bash
devfix --prompt examples/backlog_item.md
```

Optional context:

```bash
devfix \
  --prompt examples/backlog_item.md \
  --context "Stakeholders care about short feedback loops and maintainability." \
  --context-file docs/01-intent/vision.md \
  --lessons docs/07-lessons/known-mistakes.md \
  --thread-id demo-001
```

By default, the harness grounds architecture context from `docs/03-system-architecture/architecture.md`, `docs/03-system-architecture/requirements.md`, and ADRs under `docs/04-technical-decisions/`. Use `--no-default-context` to disable that behavior.

Review an external coding-agent result by adding evidence:

```bash
devfix \
  --prompt examples/backlog_item.md \
  --agent-output tmp/agent-output.md \
  --diff tmp/diff.patch \
  --test-output tmp/test-output.txt \
  --waivers tmp/waivers.json \
  --changed-file src/devfix/harness/graph.py
```

Run through an execution adapter:

```bash
devfix \
  --prompt examples/backlog_item.md \
  --executor manual
```

Run opencode headlessly:

```bash
devfix \
  --prompt examples/backlog_item.md \
  --executor opencode \
  --execution-mode headless \
  --opencode-agent build
```

Run opencode against an existing server:

```bash
opencode serve

devfix \
  --prompt examples/backlog_item.md \
  --executor opencode \
  --opencode-attach http://localhost:4096
```

## Devfix Entrypoint

After editable install, `devfix` reads `.agents/devfix/PROMPT.md` and runs the harness.

```bash
devfix
```

Override the prompt:

```bash
devfix --prompt path/to/PROMPT.md
```

Use an execution adapter:

```bash
devfix --executor opencode --opencode-agent build
```

The command uses `.agents/devfix/` for local storage and creates `.env` from `.env.example` if `.env` is missing.

## Workflow

```text
task input
  -> requirement contract
  -> architecture context
  -> known mistake check
  -> implementation packet
  -> external agent handoff
  -> optional execution adapter
  -> evidence intake
  -> independent reviewer agents
  -> deterministic completion gate
  -> revise / waiver / approve route
  -> final control report
```

Each step appends an artifact into graph state. The graph is compiled with an in-memory checkpointer, so a `thread_id` is required for resumable execution during a process lifetime.

Completion is contract-driven: reviewer approval cannot silently override missing requirements. Missing contract items require explicit waivers.

## Model Configuration

Model IDs are config, not code. OpenRouter model availability changes, so check the OpenRouter model catalog before pinning a model.

```bash
OPENROUTER_API_KEY=...
OPENROUTER_BASE_URL=https://openrouter.ai/api/v1

PLANNER_MODEL=openai/gpt-5.2
REVIEWER_MODEL=anthropic/claude-sonnet-4
FAST_MODEL=google/gemini-2.5-flash
```

## References

- LangGraph quickstart: https://docs.langchain.com/oss/python/langgraph/quickstart
- LangGraph persistence: https://docs.langchain.com/oss/python/langgraph/persistence
- OpenRouter quickstart: https://openrouter.ai/docs/quickstart
