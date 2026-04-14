# Utils

Collection of utility modules: string, dict, json, color, duration, validation, roman, slugify, and more.

## Installation

From project root:

```bash
pip install -e .
```

## Usage

```python
from utils import truncate, parse_duration, is_valid_email, clamp
from utils.duration import parse_duration, format_duration
```

## CLI

After install:

```bash
utils --help
utils string truncate "hello world" 5
utils duration parse "1h 30m"
utils json pretty '{"a":1}'
utils validation email user@example.com
```

Or run as module:

```bash
python -m utils --help
```

## Documentation

See [docs/README.md](docs/README.md) for the full module index and links to individual docs.

## Tests

Quick run (no coverage report):

```bash
pip install -e ".[dev]"
python -m pytest
```

With coverage (same invocation as CI: threshold and missing lines come from `pyproject.toml`):

```bash
pip install -e ".[dev]"
python -m pytest --cov=utils --cov-report=term-missing --cov-report=xml --cov-report=html:htmlcov
```

The terminal summary lists missed lines (`term-missing`). HTML output is written under `htmlcov/` (ignored by git). `coverage.xml` is suitable for external tools.
