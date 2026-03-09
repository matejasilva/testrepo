#!/usr/bin/env python3
"""Number utilities - a collection of numeric helper functions."""


def clamp(n: float, low: float, high: float) -> float:
    """Clamp n to the range [low, high]."""
    return max(low, min(high, n))


def sign(n: float) -> int:
    """Return -1, 0, or 1 based on the sign of n."""
    return (n > 0) - (n < 0)


def is_even(n: int) -> bool:
    """Return True if n is even."""
    return n % 2 == 0


def is_odd(n: int) -> bool:
    """Return True if n is odd."""
    return n % 2 == 1
