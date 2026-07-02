# Permission Profiles

Named permission profiles for agent YAML frontmatter. These define the tool access boundaries for each agent role.

> **Note**: Profile references in agent YAML frontmatter are not yet supported by OpenCode. These profiles serve as documentation. The explicit `permission:` blocks in each agent file remain the source of truth.

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

### `plan_file_writer`

Tools: read, glob, grep, list, edit, write, bash — allow. external_directory — deny. task — deny.

Used by: plan-file-writer.

### `router`

Tools: read, glob, grep, list, bash — allow. edit, write — deny. task — allow specific downstream agents.

Used by: router.

