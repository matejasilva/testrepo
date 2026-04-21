#!/usr/bin/env python3
"""JSON utilities - JSON parsing and serialization helpers."""

import json
from pathlib import Path

__all__ = ["loads_safe", "dumps_pretty", "load_file", "dump_file", "get_path"]


def loads_safe(s: str, default=None):
    """Parse JSON string, return default on error."""
    try:
        return json.loads(s)
    except (json.JSONDecodeError, TypeError):
        return default


def dumps_pretty(obj, indent: int = 2) -> str:
    """Serialize to JSON with pretty printing."""
    return json.dumps(obj, indent=indent)


def load_file(path: str | Path):
    """Load JSON from file."""
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def dump_file(obj, path: str | Path, indent: int = 2) -> None:
    """Write object to JSON file."""
    with open(path, "w", encoding="utf-8") as f:
        json.dump(obj, f, indent=indent)


def get_path(data: dict, path: str, default=None, sep: str = "."):
    """Get nested value by dotted path, e.g. 'a.b.c'."""
    keys = path.split(sep)
    current = data
    for k in keys:
        if isinstance(current, dict) and k in current:
            current = current[k]
        else:
            return default
    return current
