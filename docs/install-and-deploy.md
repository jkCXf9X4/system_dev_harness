# Install and Deploy

## Package Deployment

The workflow package is deployed by copying `opencode.json` and `.opencode/` into a target development repository.

## Steps

1. Clone or open the target development repository.
2. Copy `opencode.json` into the repository root.
3. Copy the `.opencode/` directory into the repository root.
4. Leave `product-breakdown/` in this repository; it is source documentation, not runtime payload.

## Dependency Handling

The `.opencode/package.json` file declares the OpenCode plugin dependency, and `.opencode/.gitignore` excludes `node_modules`, `package.json`, `package-lock.json`, and `bun.lock` from the copied runtime tree. Treat the copied manifest as the source of truth for the runtime dependency set.

## Update Process

1. Pull the latest changes from this repository.
2. Re-copy `opencode.json` and `.opencode/` into the target repository.
3. Review `git diff` in the target repository to confirm only the intended changes were applied.
