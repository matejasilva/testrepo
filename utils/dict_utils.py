#!/usr/bin/env python3
"""Dict utilities - a collection of dictionary helper functions."""

from typing import TypeVar, Any, Callable

__all__ = [
    "deep_merge",
    "flatten_keys",
    "unflatten_keys",
    "invert",
    "filter_keys",
    "omit_keys",
    "map_values",
    "map_keys",
    "get_nested",
    "set_nested",
]

K = TypeVar("K")
V = TypeVar("V")


def deep_merge(base: dict, override: dict) -> dict:
    """Recursively merge override into base. Override values take precedence."""
    result = dict(base)
    for key, value in override.items():
        if key in result and isinstance(result[key], dict) and isinstance(value, dict):
            result[key] = deep_merge(result[key], value)
        else:
            result[key] = value
    return result


def flatten_keys(d: dict, parent_key: str = "", sep: str = ".") -> dict[str, Any]:
    """Flatten nested dict to single level with dotted keys."""
    items: list[tuple[str, Any]] = []
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict) and v:
            items.extend(flatten_keys(v, new_key, sep).items())
        else:
            items.append((new_key, v))
    return dict(items)


def unflatten_keys(d: dict[str, Any], sep: str = ".") -> dict:
    """Convert flattened dict with dotted keys back to nested structure."""
    result: dict = {}
    for key, value in d.items():
        parts = key.split(sep)
        current = result
        for part in parts[:-1]:
            if part not in current:
                current[part] = {}
            current = current[part]
        current[parts[-1]] = value
    return result


def invert(d: dict[K, V]) -> dict[V, list[K]]:
    """Invert dict: values become keys, keys collected in lists (handles duplicates)."""
    result: dict[V, list[K]] = {}
    for k, v in d.items():
        if v not in result:
            result[v] = []
        result[v].append(k)
    return result


def filter_keys(d: dict[K, V], keys: set[K] | list[K]) -> dict[K, V]:
    """Return dict containing only the specified keys."""
    key_set = set(keys)
    return {k: v for k, v in d.items() if k in key_set}


def omit_keys(d: dict[K, V], keys: set[K] | list[K]) -> dict[K, V]:
    """Return dict excluding the specified keys."""
    key_set = set(keys)
    return {k: v for k, v in d.items() if k not in key_set}


def map_values(d: dict[K, V], fn: Callable[[V], Any]) -> dict[K, Any]:
    """Apply function to each value, return new dict."""
    return {k: fn(v) for k, v in d.items()}


def map_keys(d: dict[K, V], fn: Callable[[K], Any]) -> dict[Any, V]:
    """Apply function to each key, return new dict."""
    return {fn(k): v for k, v in d.items()}


def get_nested(d: dict, path: str | list, default: Any = None, sep: str = ".") -> Any:
    """Get value at dotted path, e.g. get_nested(d, 'a.b.c') or get_nested(d, ['a','b','c'])."""
    parts = path.split(sep) if isinstance(path, str) else path
    current = d
    for part in parts:
        if isinstance(current, dict) and part in current:
            current = current[part]
        else:
            return default
    return current


def set_nested(d: dict, path: str | list, value: Any, sep: str = ".") -> None:
    """Set value at dotted path. Mutates d in place."""
    parts = path.split(sep) if isinstance(path, str) else path
    current = d
    for part in parts[:-1]:
        if part not in current or not isinstance(current[part], dict):
            current[part] = {}
        current = current[part]
    current[parts[-1]] = value


if __name__ == "__main__":
    print("deep_merge:", deep_merge({"a": 1, "b": {"x": 1}}, {"b": {"y": 2}}))
    print("flatten_keys:", flatten_keys({"a": {"b": {"c": 1}}}))
    print("invert:", invert({"x": 1, "y": 1, "z": 2}))
    print("filter_keys:", filter_keys({"a": 1, "b": 2, "c": 3}, ["a", "c"]))
    print("get_nested:", get_nested({"a": {"b": {"c": 42}}}, "a.b.c"))
