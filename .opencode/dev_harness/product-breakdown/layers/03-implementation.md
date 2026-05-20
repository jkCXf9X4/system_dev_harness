# 03 Implementation Layer

The implementation layer describes how the architecture is realized in code, configuration, tools, and environments.

## Typical Artifacts



```text
code-structure.md - describes the repository layout and code organization
modules/          - contains module-level implementation notes
interfaces/       - documents internal APIs and boundary contracts
configuration.md  - explains how settings and flags are provided
environments.md   - lists supported local, test, staging, and prod envs
decisions/        - stores implementation-level decisions and rationale
```

## Questions Answered

- How is the code organized?
- How are modules structured?
- What internal interfaces exist?
- How is configuration handled?
- What environments are supported?
- Which implementation patterns are used?

## Example Decisions

```text
IMD-001-use-feature-folders-in-the-frontend.md
IMD-002-validate-at-command-boundaries.md
IMD-003-use-explicit-mapping-between-layers.md
TD-001-use-postgresql-as-primary-database.md
TD-002-use-github-actions-for-ci.md
```

Implementation decisions should be concrete. They usually affect developers working inside the codebase more directly than they affect product behavior or architecture.
