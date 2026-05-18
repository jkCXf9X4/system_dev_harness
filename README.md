# System Dev Harness

A guarded agentic development harness starter that uses:

- LangGraph for explicit workflow control and state.
- OpenRouter as the OpenAI-compatible model access layer.
- Role-based support agents for requirement contracts, architecture guardrails, known mistake checks, implementation handoff, and reviewer approval.

The harness is designed to keep agentic development on track. It focuses on preventing shortcuts, partial implementations, lost requirements, architecture drift, and repeated mistakes. It does not edit code directly yet; instead it produces strict implementation packets for external coding agents such as Codex or opencode.

## Documentation

Start here for the broader product and engineering intent:

- [Documentation Index](docs/README.md)
- [Vision](docs/vision.md)
- [Use Cases](docs/use-cases.md)
- [Traceability Matrix](docs/traceability.md)
- [Architecture Overview](docs/architecture.md)
- [Decision Records](docs/decisions/README.md)

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
```

Edit `.env` and set `OPENROUTER_API_KEY`.

## Run

```bash
python app.py --backlog examples/backlog_item.md
```

Optional context:

```bash
python app.py \
  --backlog examples/backlog_item.md \
  --context "Stakeholders care about short feedback loops and maintainability." \
  --context-file docs/vision.md \
  --lessons docs/lessons/known-mistakes.md \
  --thread-id demo-001
```

By default, the harness grounds architecture context from `docs/architecture.md`, `docs/requirements.md`, and ADRs under `docs/decisions/`. Use `--no-default-context` to disable that behavior.

Review an external coding-agent result by adding evidence:

```bash
python app.py \
  --backlog examples/backlog_item.md \
  --agent-output tmp/agent-output.md \
  --diff tmp/diff.patch \
  --test-output tmp/test-output.txt \
  --waivers tmp/waivers.json \
  --changed-file harness/graph.py
```

Run through an execution adapter:

```bash
python app.py \
  --backlog examples/backlog_item.md \
  --executor manual
```

Run opencode headlessly:

```bash
python app.py \
  --backlog examples/backlog_item.md \
  --executor opencode \
  --execution-mode headless \
  --opencode-agent build
```

Run opencode against an existing server:

```bash
opencode serve

python app.py \
  --backlog examples/backlog_item.md \
  --executor opencode \
  --opencode-attach http://localhost:4096
```

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
