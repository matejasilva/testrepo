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


def reverse_words(s: str) -> str:
    """Return s with the order of words reversed."""
    return " ".join(reversed(s.split()))


def capitalize_words(s: str) -> str:
    """Return s with the first letter of each word capitalized."""
    return s.title()


def strip_extra_spaces(s: str) -> str:
    """Collapse runs of whitespace to a single space and strip leading/trailing whitespace."""
    return " ".join(s.split())
