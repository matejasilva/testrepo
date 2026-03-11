#!/usr/bin/env python3
"""Validation utilities - input validation helpers."""


def is_email(s: str) -> bool:
    """Basic email format check."""
    if not s or "@" not in s or "." not in s:
        return False
    local, domain = s.split("@", 1)
    return len(local) > 0 and len(domain) > 3 and "." in domain


def is_url(s: str) -> bool:
    """Basic URL format check."""
    return s.startswith(("http://", "https://")) and len(s) > 10


def is_positive_int(value) -> bool:
    """Return True if value is a positive integer."""
    return isinstance(value, int) and value > 0


def is_non_empty_str(s) -> bool:
    """Return True if s is non-empty string."""
    return isinstance(s, str) and len(s.strip()) > 0


def in_range(value: int | float, low: int | float, high: int | float) -> bool:
    """Return True if low <= value <= high."""
    return low <= value <= high


def one_of(value, allowed: set | list) -> bool:
    """Return True if value is in allowed."""
    return value in allowed


def has_required_keys(d: dict, keys: list) -> bool:
    """Return True if dict has all required keys."""
    return all(k in d for k in keys)
