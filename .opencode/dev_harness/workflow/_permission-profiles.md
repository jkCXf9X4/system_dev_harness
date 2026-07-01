# Permission Profiles

Named permission profiles for agent YAML frontmatter. These define the tool access boundaries for each agent role.

> **Note**: If OpenCode does not support `profile:` references in agent YAML frontmatter, these profiles serve as documentation. The explicit `permission:` blocks in each agent file remain the source of truth.

## Profile Definitions

### `read_only`

Tools: read, glob, grep, list — allow. edit, write — deny. bash — allow.

Used by: architecture, contract, discovery, lessons, memory, reflection, reporter, researcher, review-architecture, review-completeness, review-lessons, systems-engineering, validation, verifier.

### `curator`

Tools: read, glob, grep, list, edit, write, bash — allow. external_directory — deny.

Used by: memory-curator.

### `full_access`

Tools: all tools allowed. Note: external_directory — deny (builder, build-error-resolver, cleanup all restrict external_directory).

Used by: builder, build-error-resolver, cleanup.

### `planner`

Tools: read, glob, grep, list, edit, write, bash — allow. task: allow specific planning helpers.

Used by: planner.

### `reviewer`

Tools: read, glob, grep, list, bash — allow. edit, write — deny. task: allow specific review helpers.

Used by: reviewer.

### ~~`orchestrator_router`~~ (deprecated)

This profile previously referenced the standalone "orchestrator (router)" role. That role has been consolidated into the primary `planner` entrypoint, which handles routing internally. The `planner` profile above reflects the current agent configuration. Retained here as a historical reference only; do not use for new agents.