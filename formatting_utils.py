#!/usr/bin/env python3
"""Formatting utilities - number/string formatting helpers."""


def pluralize(n: int, singular: str, plural: str | None = None) -> str:
    """Return singular or plural form based on count."""
    if plural is None:
        plural = singular + "s"
    return singular if n == 1 else plural


def format_number(n: int | float, sep: str = ",") -> str:
    """Format number with thousand separators."""
    s = f"{n:,}"
    return s if sep == "," else s.replace(",", sep)


def truncate_str(s: str, max_len: int, suffix: str = "...") -> str:
    """Truncate string to max length."""
    if len(s) <= max_len:
        return s
    return s[: max_len - len(suffix)] + suffix


def pad_left(s: str, width: int, char: str = " ") -> str:
    """Pad string to width with char on left."""
    return s.rjust(width, char)


def pad_right(s: str, width: int, char: str = " ") -> str:
    """Pad string to width with char on right."""
    return s.ljust(width, char)


def percent_str(value: float, total: float, decimals: int = 1) -> str:
    """Format value/total as percentage string."""
    if total == 0:
        return "0%"
    pct = 100 * value / total
    return f"{pct:.{decimals}f}%"
