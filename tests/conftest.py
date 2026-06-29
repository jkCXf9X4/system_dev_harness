from __future__ import annotations

import json
import os
import shutil
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parents[1]
FIXTURE_ROOT = Path(__file__).resolve().parent / "fixtures" / "simple_project"
AUTH_FILE = Path.home() / ".local" / "share" / "opencode" / "auth.json"


@pytest.fixture()
def simple_project(tmp_path: Path) -> Path:
    worktree = tmp_path / "simple_project"
    shutil.copytree(FIXTURE_ROOT, worktree)
    shutil.copy2(REPO_ROOT / "opencode.json", worktree / "opencode.json")
    shutil.copytree(REPO_ROOT / ".opencode", worktree / ".opencode")
    return worktree


@pytest.fixture()
def opencode_env(tmp_path: Path) -> dict[str, str]:
    home = tmp_path / "opencode-home"
    data = tmp_path / "opencode-data"
    state = tmp_path / "opencode-state"
    cache = tmp_path / "opencode-cache"

    for path in (home / ".config", data, state, cache):
        path.mkdir(parents=True, exist_ok=True)

    if AUTH_FILE.exists():
        auth_dir = data / "opencode"
        auth_dir.mkdir(parents=True, exist_ok=True)
        shutil.copy2(AUTH_FILE, auth_dir / "auth.json")

    env = os.environ.copy()
    env.update(
        {
            "HOME": str(home),
            "XDG_CONFIG_HOME": str(home / ".config"),
            "XDG_DATA_HOME": str(data),
            "XDG_STATE_HOME": str(state),
            "XDG_CACHE_HOME": str(cache),
        }
    )

    if AUTH_FILE.exists():
        auth = json.loads(AUTH_FILE.read_text(encoding="utf-8"))
        openrouter_key = auth.get("openrouter", {}).get("key")
        if openrouter_key:
            env["OPENROUTER_API_KEY"] = openrouter_key
    return env
