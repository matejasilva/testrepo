#!/usr/bin/env python3
"""List utilities - a collection of list helper functions."""


def flatten(nested: list) -> list:
    """Flatten a nested list one level deep."""
    result = []
    for item in nested:
        if isinstance(item, list):
            result.extend(item)
        else:
            result.append(item)
    return result


def chunk(lst: list, size: int) -> list:
    """Split a list into chunks of given size."""
    return [lst[i : i + size] for i in range(0, len(lst), size)]


def dedupe(lst: list) -> list:
    """Remove duplicates while preserving order."""
    seen = set()
    return [x for x in lst if not (x in seen or seen.add(x))]


def rotate(lst: list, n: int) -> list:
    """Rotate list by n positions (negative n rotates left)."""
    if not lst:
        return []
    n = n % len(lst)
    return lst[n:] + lst[:n]


def take(lst: list, n: int) -> list:
    """Take first n elements from a list."""
    return lst[:n]


if __name__ == "__main__":
    data = [1, 2, [3, 4], 5, [6, 7]]
    nums = [1, 2, 3, 4, 5, 6, 7, 8]
    dupes = [1, 2, 2, 3, 1, 4, 3, 5]
    print("Flatten:", flatten(data))
    print("Chunk:", chunk(nums, 3))
    print("Dedupe:", dedupe(dupes))
    print("Rotate:", rotate([1, 2, 3, 4, 5], 2))
    print("Take 3:", take(nums, 3))
