#!/usr/bin/env python3
"""Dict utilities - a collection of dict helper functions."""


def invert(d: dict) -> dict:
    """Swap keys and values. Values must be hashable."""
    return {v: k for k, v in d.items()}


def get_nested(d: dict, path: str, sep: str = ".") -> object:
    """Get nested value by dot-separated path, e.g. 'a.b.c'."""
    for key in path.split(sep):
        d = d[key]
    return d


def merge(*dicts: dict) -> dict:
    """Merge multiple dicts. Later dicts override earlier ones."""
    result = {}
    for d in dicts:
        result.update(d)
    return result


def pick(d: dict, keys: list) -> dict:
    """Return dict with only the specified keys."""
    return {k: d[k] for k in keys if k in d}


if __name__ == "__main__":
    print("Invert:", invert({"a": 1, "b": 2}))
    print("Nested:", get_nested({"a": {"b": {"c": 42}}}, "a.b.c"))
    print("Merge:", merge({"x": 1}, {"y": 2}, {"x": 99}))
    print("Pick:", pick({"a": 1, "b": 2, "c": 3}, ["a", "c"]))
