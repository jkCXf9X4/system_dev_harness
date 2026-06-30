# Permission Profiles

Named permission profiles for agent YAML frontmatter. These define the tool access boundaries for each agent role.

> **Note**: If OpenCode does not support `profile:` references in agent YAML frontmatter, these profiles serve as documentation. The explicit `permission:` blocks in each agent file remain the source of truth.

## Profile Definitions

### `read_only`

Tools: read, glob, grep, list — allow. edit, write, bash — deny.

Used by: discovery, contract, architecture, lessons, memory, memory-curator, researcher, verifier, review-architecture, review-completeness, review-lessons, systems-engineering, reflection, reporter.

### `full_access`

Tools: all tools allowed.

Used by: builder, build-error-resolver, cleanup.

### `planner`

Tools: read, glob, grep, list, edit, write, bash — allow. task: allow specific planning helpers.

Used by: planner.

### `reviewer`

Tools: read, glob, grep, list, bash — allow. edit, write — deny. task: allow specific review helpers.

Used by: reviewer.

### `orchestrator_router`

Tools: all deny. task: allow specific stage agents.

Used by: orchestrator (router).