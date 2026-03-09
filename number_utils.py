#!/usr/bin/env python3
"""Number utilities - a collection of numeric helper functions."""


def clamp(n: float, low: float, high: float) -> float:
    """Clamp n to the range [low, high]."""
    return max(low, min(high, n))


def sign(n: float) -> int:
    """Return -1, 0, or 1 based on the sign of n."""
    return (n > 0) - (n < 0)
