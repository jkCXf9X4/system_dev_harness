# Deployment Process

## Package Deployment

The workflow package is deployed by copying `opencode.json` and `.opencode/` into a target development repository.

### Steps

1. Clone or open the target development repository.
2. Copy `opencode.json` into the repository root.
3. Copy the `.opencode/` directory into the repository root.
4. The `docs/` tree stays in the package repository — it is not copied.

### Versioning

The package is versioned by git commit in this repository. There is no separate package registry. Update the target repo's copy by re-copying the files from a newer commit.

### Update Process

1. Pull latest changes from this package repository.
2. Re-copy `opencode.json` and `.opencode/` into the target repository.
3. Review `git diff` in the target repo to verify only the intended changes were applied.