#!/usr/bin/env python3
"""Regex utilities - common regex patterns and helpers."""

import re


def extract_first(pattern: str, text: str, group: int = 0) -> str | None:
    """Extract first match from text. Returns None if no match."""
    m = re.search(pattern, text)
    return m.group(group) if m else None


def extract_all(pattern: str, text: str, group: int = 0) -> list[str]:
    """Extract all non-overlapping matches."""
    if group == 0:
        return re.findall(pattern, text)
    return [m.group(group) for m in re.finditer(pattern, text)]


def replace_all(pattern: str, replacement: str, text: str) -> str:
    """Replace all matches of pattern with replacement."""
    return re.sub(pattern, replacement, text)


def split_regex(pattern: str, text: str, maxsplit: int = 0) -> list[str]:
    """Split text by regex pattern."""
    return re.split(pattern, text, maxsplit=maxsplit)


# Common patterns
EMAIL_PATTERN = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
URL_PATTERN = r"https?://[^\s]+"
IPV4_PATTERN = r"\b(?:\d{1,3}\.){3}\d{1,3}\b"
INTEGER_PATTERN = r"-?\d+"
FLOAT_PATTERN = r"-?\d+\.?\d*"
