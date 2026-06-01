# Hermes Agent Memory Handling

This note captures implementation lessons from NousResearch Hermes Agent for future prompt and workflow design. It is an implementation reference, not primary research evidence. Use it alongside `AK-005` and `AK-009`, and cite research sources for durable product decisions.

## Sources Reviewed

- Repository: https://github.com/nousresearch/hermes-agent
- Memory documentation: https://hermes-agent.nousresearch.com/docs/user-guide/features/memory
- Skills documentation: https://hermes-agent.nousresearch.com/docs/user-guide/features/skills

## Relevant Ideas

### Bounded Always-On Memory

Hermes separates always-in-context memory from searchable history. Its documented default memory has two bounded stores:

- `MEMORY.md` for agent notes, environment facts, conventions, and lessons.
- `USER.md` for user preferences, communication style, expectations, and profile details.

Both are injected as a frozen snapshot at session start, with visible capacity usage. This supports a useful design principle for this project: keep the always-loaded workflow memory small, explicit, and curated rather than letting every prior observation enter the prompt.

Reusable lesson:

- Always-on memory should be compact and curated.
- Memory capacity should be visible to the agent or curator.
- Memory should have a consolidation path when capacity is high.

### Separate Critical Memory From Searchable Session History

Hermes distinguishes persistent memory from session search:

- persistent memory is for critical facts that should always be present
- session search is for finding specific prior conversations on demand

This distinction maps well to this project's workflow memory:

- `.opencode/dev_harness_memories/` should hold durable prevention rules, reusable patterns, and decision pointers.
- Task-local logs, review histories, and one-off investigation details should remain searchable or traceable elsewhere, not promoted into always-loaded memory.

Reusable lesson:

- Do not overload durable memory with historical transcripts.
- Add a retrieval path for past task evidence only when needed.
- Treat "important enough to search later" as different from "important enough to inject every run."

### Explicit Save/Skip Criteria

Hermes documents what to save and what to skip. Save candidates include user preferences, environment facts, project conventions, corrections, completed work, and explicit remember requests. Skip candidates include vague facts, easily rediscovered information, raw data dumps, session ephemera, and information already stored in context files.

This reinforces the current memory-curator rules and suggests a useful refinement: memory candidates should carry a type and a skip reason when rejected.

Reusable lesson:

- Accepted memory should state why it belongs in durable memory.
- Rejected memory should state whether it was vague, rediscoverable, duplicated, too large, session-specific, or already represented elsewhere.
- Memory review should distinguish stable project conventions from transient implementation state.

### Frozen Snapshot With Live Persistence

Hermes persists memory edits immediately but does not update the system-prompt memory block until the next session. This avoids mid-session prompt mutation while still recording durable changes.

This project already uses versioned files rather than hidden memory. The relevant lesson is to avoid assuming newly written memory has affected the current run. If a memory curator writes a new lesson during a review, downstream agents in the same run should use the curator output directly, not assume the global memory read path has refreshed.

Reusable lesson:

- Report memory writes as side effects in the current run.
- Do not rely on newly persisted memory unless it is explicitly passed forward.
- Treat next-run memory availability as separate from current-run evidence.

### Memory Security And Hygiene

Hermes documentation says memory entries are scanned for injection, exfiltration patterns, and invisible Unicode because memory is injected into the system prompt.

This is directly relevant to this project. Workflow memory can influence planning, implementation, and review, so memory curation should reject prompt-injection text, credential material, hidden characters, untrusted command output, and unverified external claims.

Reusable lesson:

- Treat memory as executable influence over future agent behavior.
- Memory curation should include safety screening, not only usefulness screening.
- Untrusted external content should not become durable memory without review and sanitization.

### Skills As Procedural Memory

Hermes treats skills as on-demand knowledge documents loaded through progressive disclosure. Skills are not the same as memory: skills preserve reusable procedures, while memory preserves durable facts, preferences, conventions, and lessons.

This distinction is useful for future project evolution:

- durable fact or prevention rule -> workflow memory
- repeatable procedure or operating pattern -> pattern entry or skill-like artifact
- future work item -> improvement candidate
- one-off evidence -> task report or searchable history

Reusable lesson:

- Do not force procedural knowledge into fact memory.
- Keep memory, patterns, skills, and backlog candidates separate because they operate on different timescales.
- Use progressive disclosure for larger procedural artifacts instead of injecting them by default.

## Project Fit

The project should not copy Hermes' exact flat-file memory design because this repository already has versioned markdown memory, product-breakdown traceability, and review gates. The useful transferable ideas are:

- strict memory capacity and consolidation pressure
- separate always-on memory from searchable historical evidence
- explicit save/skip criteria
- current-run reporting for newly written memory
- memory safety screening
- separation between memory, procedural patterns, and backlog candidates

These map most directly to `AK-005` and `AK-009`.
