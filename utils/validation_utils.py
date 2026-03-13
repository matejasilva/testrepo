#!/usr/bin/env python3
"""Validation utilities - helpers for validating email, URL, and phone formats."""

import re


def is_valid_email(s: str) -> bool:
    """
    Basic email format validation (local@domain.tld).
    Returns True if format is valid, False otherwise.
    """
    if not s or not isinstance(s, str):
        return False
    # local@domain.tld - simple pattern: chars, optional dots, @, domain with TLD
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return bool(re.match(pattern, s.strip()))


def is_valid_url(s: str) -> bool:
    """
    Basic URL validation for http/https schemes.
    Returns True if format is valid, False otherwise.
    """
    if not s or not isinstance(s, str):
        return False
    s = s.strip()
    if not (s.startswith("http://") or s.startswith("https://")):
        return False
    # Basic structure: scheme://host (host can have domain, port, path)
    pattern = r"^https?://[a-zA-Z0-9.-]+(\.[a-zA-Z]{2,})?(/.*)?$"
    return bool(re.match(pattern, s))


def is_valid_phone(s: str) -> bool:
    """
    Flexible phone number validation.
    Accepts digits, spaces, dashes; optional + prefix.
    Requires at least 7 digits.
    """
    if not s or not isinstance(s, str):
        return False
    # Strip and allow digits, spaces, dashes, parens; optional leading +
    cleaned = s.strip()
    if cleaned.startswith("+"):
        cleaned = cleaned[1:].strip()
    digits_only = "".join(c for c in cleaned if c.isdigit())
    allowed_chars = set("0123456789 -()")
    return len(digits_only) >= 7 and all(c in allowed_chars for c in cleaned)
