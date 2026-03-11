#!/usr/bin/env python3
"""List utilities - a collection of list helper functions."""

from typing import TypeVar, Callable

T = TypeVar("T")


def flatten(nested: list) -> list:
    """Flatten a nested list one level deep."""
    result = []
    for item in nested:
        if isinstance(item, list):
            result.extend(item)
        else:
            result.append(item)
    return result


def deep_flatten(nested: list) -> list:
    """Recursively flatten a nested list of any depth."""
    result = []
    for item in nested:
        if isinstance(item, list):
            result.extend(deep_flatten(item))
        else:
            result.append(item)
    return result


def chunk(lst: list[T], size: int) -> list[list[T]]:
    """Split list into chunks of given size."""
    if size <= 0:
        raise ValueError("size must be positive")
    return [lst[i : i + size] for i in range(0, len(lst), size)]


def unique(lst: list[T], key: Callable[[T], object] | None = None) -> list[T]:
    """Return list with duplicates removed, preserving order."""
    if key is None:
        seen = set()
        result = []
        for x in lst:
            if x not in seen:
                seen.add(x)
                result.append(x)
        return result
    seen = set()
    result = []
    for x in lst:
        k = key(x)
        if k not in seen:
            seen.add(k)
            result.append(x)
    return result


def pairwise(lst: list[T]) -> list[tuple[T, T]]:
    """Return successive overlapping pairs from the list."""
    return list(zip(lst[:-1], lst[1:]))


def rotate(lst: list[T], n: int) -> list[T]:
    """Rotate list left by n positions (negative n rotates right)."""
    if not lst:
        return []
    n = n % len(lst)
    return lst[n:] + lst[:n]


def partition(
    lst: list[T], predicate: Callable[[T], bool]
) -> tuple[list[T], list[T]]:
    """Split list into (matching, non-matching) based on predicate."""
    matching = []
    non_matching = []
    for x in lst:
        if predicate(x):
            matching.append(x)
        else:
            non_matching.append(x)
    return matching, non_matching


def interleave(*lists: list[T]) -> list[T]:
    """Interleave elements from multiple lists (stops at shortest)."""
    result = []
    for items in zip(*lists):
        result.extend(items)
    return result


def sliding_window(lst: list[T], size: int) -> list[tuple[T, ...]]:
    """Yield sliding windows of given size."""
    if size <= 0:
        raise ValueError("size must be positive")
    if size > len(lst):
        return []
    return [tuple(lst[i : i + size]) for i in range(len(lst) - size + 1)]


if __name__ == "__main__":
    print("flatten:", flatten([[1, 2], [3, 4], 5]))
    print("deep_flatten:", deep_flatten([[1, [2, 3]], [4, [5, [6]]]]))
    print("chunk:", chunk([1, 2, 3, 4, 5], 2))
    print("unique:", unique([1, 2, 2, 3, 1, 4]))
    print("pairwise:", pairwise([1, 2, 3, 4]))
    print("rotate:", rotate([1, 2, 3, 4, 5], 2))
    print("partition:", partition([1, 2, 3, 4, 5], lambda x: x % 2 == 0))
    print("interleave:", interleave([1, 2], ["a", "b"], [10, 20]))
    print("sliding_window:", sliding_window([1, 2, 3, 4], 2))
