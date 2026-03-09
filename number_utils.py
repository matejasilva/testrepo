#!/usr/bin/env python3
"""Number utilities - a collection of numeric helper functions."""


def clamp(n: float, low: float, high: float) -> float:
    """Clamp n to the range [low, high]."""
    if low > high:
        raise ValueError("low must be less than or equal to high")
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


def digits(n: int) -> list[int]:
    """Return list of digits in n. Handles negatives via abs."""
    n = abs(n)
    return [int(d) for d in str(n)]


if __name__ == "__main__":
    print("Clamp:", clamp(15, 0, 10))
    print("Sign:", sign(-5), sign(0), sign(3))
    print("Even/Odd:", is_even(4), is_odd(7))
    print("Digits:", digits(12345))
