#!/usr/bin/env python3
"""String utilities - basic string helper functions."""


def truncate(s: str, max_len: int, suffix: str = "...") -> str:
    """Truncate s to max_len, appending suffix if truncated."""
    if len(s) <= max_len:
        return s
    return s[: max_len - len(suffix)] + suffix


def is_palindrome(s: str) -> bool:
    """Return True if s reads the same forwards and backwards (ignores case)."""
    cleaned = "".join(c.lower() for c in s if c.isalnum())
    return cleaned == cleaned[::-1]


def word_count(s: str) -> int:
    """Return the number of words in s (split on whitespace)."""
    return len(s.split())
