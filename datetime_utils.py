#!/usr/bin/env python3
"""DateTime utilities - date/time helper functions."""

from datetime import datetime, timedelta


def parse_iso(s: str) -> datetime:
    """Parse ISO 8601 datetime string."""
    return datetime.fromisoformat(s.replace("Z", "+00:00"))


def format_iso(dt: datetime) -> str:
    """Format datetime as ISO 8601 string."""
    return dt.isoformat()


def days_ago(dt: datetime) -> int:
    """Days between dt and now (negative if dt is in future)."""
    return (datetime.now(dt.tzinfo) - dt).days


def start_of_day(dt: datetime) -> datetime:
    """Return datetime at midnight of same day."""
    return dt.replace(hour=0, minute=0, second=0, microsecond=0)


def end_of_day(dt: datetime) -> datetime:
    """Return datetime at 23:59:59.999999 of same day."""
    return dt.replace(hour=23, minute=59, second=59, microsecond=999999)


def is_weekend(dt: datetime) -> bool:
    """Return True if date is Saturday or Sunday."""
    return dt.weekday() >= 5


def add_business_days(dt: datetime, n: int) -> datetime:
    """Add n business days (skip weekends)."""
    result = dt
    days_added = 0
    direction = 1 if n >= 0 else -1
    n = abs(n)
    while days_added < n:
        result += timedelta(days=direction)
        if not is_weekend(result):
            days_added += 1
    return result
