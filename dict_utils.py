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
