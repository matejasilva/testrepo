# Ticket 004: Utils Package Restructure + Unified CLI + Documentation Overhaul

## Status
Open

## Description
Major refactor touching 30+ files: convert flat module layout into a proper `utils` package, add a unified CLI for all utilities, and overhaul documentation.

## Scope (Estimated ~35 files changed)

### 1. Package Restructure (~24 files)
- Create `utils/` package directory
- Move every util module into `utils/` (e.g. `color_utils.py` → `utils/color_utils.py`)
- Create `utils/__init__.py` exporting all public APIs from all modules
- Update every `test_*.py` import path (e.g. `from utils.color_utils import ...`)
- Add `py.typed` marker for PEP 561
- Update `.github/workflows/ci.yml` to run tests from new layout
- Update any scripts (e.g. `print_numbers.py`) that import utils

### 2. Unified CLI (~15+ files)
- Create `utils/cli.py` — main entry point with subcommands per module
- Add `__main__.py` so `python -m utils` runs the CLI
- Each util module gets a `cli(subparser)` or equivalent to register its commands
- Commands: `utils string truncate "hello world" 5`, `utils duration parse "1h 30m"`, `utils json pretty '{"a":1}'`, etc.
- Add `[project.scripts]` or `entry_points` in `pyproject.toml` / `setup.cfg` for `utils` CLI
- Ensure all 10+ util modules have at least one invocable CLI command

### 3. Documentation Overhaul (~15+ files)
- Create `docs/README.md` — master index linking to all module docs
- Add or expand `docs/*.md` for every module that lacks one: `duration`, `retry`, `validation_utils`, `number_utils`, `math_utils`, `roman`, `slugify`, `print_numbers`
- Add "Usage" section with `from utils import ...` examples to each doc
- Add "CLI" section showing command-line examples
- Create `docs/API.md` — auto-generated or hand-written API reference for all exports
- Update root `README.md` (create if missing) with install instructions and link to docs

### 4. Supporting Files
- `pyproject.toml` or update `setup.cfg` — package config, entry points
- `.cursorignore` / `.gitignore` — ignore `utils/__pycache__`, build artifacts if needed

## Acceptance Criteria
- [ ] All utils live under `utils/` package; root has no stray `*_utils.py` (except possibly backwards-compat shims)
- [ ] `from utils import truncate, parse_duration, is_valid_email` works
- [ ] `utils --help` and `utils <module> <command> --help` work
- [ ] At least one CLI command per util module (10+ modules)
- [ ] Every module has a corresponding doc in `docs/`
- [ ] `docs/README.md` indexes all module documentation
- [ ] All existing tests pass after restructure
- [ ] CI runs successfully against new layout

## Notes
- Consider backwards-compatibility shims (e.g. `color_utils.py` = `from utils.color_utils import *`) if external consumers exist
- CLI can use `argparse` subparsers; keep it dependency-free
- Break into subtasks if needed: (1) restructure, (2) CLI, (3) docs
