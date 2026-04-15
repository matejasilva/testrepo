#!/usr/bin/env python3
"""Iterator and sequence helpers built on lazy evaluation where possible."""

from __future__ import annotations

from collections import deque
from collections.abc import Callable, Iterable, Iterator
from typing import Any, TypeVar

T = TypeVar("T")
U = TypeVar("U")


def chunk(iterable: Iterable[T], size: int) -> Iterator[list[T]]:
    """Yield lists of up to ``size`` items from *iterable*.

    The final chunk may be shorter than ``size``. ``size`` must be positive.
    """
    if size < 1:
        raise ValueError("size must be at least 1")
    it = iter(iterable)
    while True:
        batch: list[T] = []
        try:
            for _ in range(size):
                batch.append(next(it))
        except StopIteration:
            if batch:
                yield batch
            break
        yield batch


def batched(iterable: Iterable[T], n: int) -> Iterator[tuple[T, ...]]:
    """Like :func:`chunk`, but each batch is an immutable tuple of length *n*.

    The last batch is dropped if *iterable* length is not divisible by *n*
    (strict sizing). For variable-length tail behaviour, use :func:`chunk`.
    """
    if n < 1:
        raise ValueError("n must be at least 1")
    it = iter(iterable)
    while True:
        batch: list[T] = []
        try:
            for _ in range(n):
                batch.append(next(it))
        except StopIteration:
            break
        yield tuple(batch)


def flatten(iterable: Iterable[Iterable[T]]) -> Iterator[T]:
    """Flatten one level of nesting."""
    for inner in iterable:
        yield from inner


def flatten_depth(iterable: Iterable[Any], depth: int = 1) -> Iterator[Any]:
    """Flatten nested iterables up to *depth* levels.

    Strings and bytes are treated as atomic values (not iterated).
    """
    if depth < 0:
        raise ValueError("depth must be non-negative")
    if depth == 0:
        for item in iterable:
            yield item
        return

    for item in iterable:
        if isinstance(item, (str, bytes)):
            yield item
        else:
            try:
                it = iter(item)
            except TypeError:
                yield item
            else:
                yield from flatten_depth(it, depth - 1)


def unique_ordered(iterable: Iterable[T]) -> Iterator[T]:
    """Yield unique items preserving first-seen order (hashable items)."""
    seen: set[T] = set()
    for item in iterable:
        if item not in seen:
            seen.add(item)
            yield item


def pairwise(iterable: Iterable[T]) -> Iterator[tuple[T, T]]:
    """Yield overlapping pairs ``(x0, x1), (x1, x2), ...``."""
    it = iter(iterable)
    try:
        prev = next(it)
    except StopIteration:
        return
    for cur in it:
        yield (prev, cur)
        prev = cur


def sliding_window(iterable: Iterable[T], n: int) -> Iterator[tuple[T, ...]]:
    """Yield tuples of *n* consecutive items; requires *n* >= 1."""
    if n < 1:
        raise ValueError("n must be at least 1")
    it = iter(iterable)
    window: deque[T] = deque(maxlen=n)
    for _ in range(n):
        try:
            window.append(next(it))
        except StopIteration:
            return
    yield tuple(window)
    for item in it:
        window.append(item)
        yield tuple(window)


def partition(
    pred: Callable[[T], bool],
    iterable: Iterable[T],
) -> tuple[list[T], list[T]]:
    """Split *iterable* into ``(trues, falses)`` according to *pred*.

    This consumes the iterable into two lists.
    """
    yes: list[T] = []
    no: list[T] = []
    for item in iterable:
        if pred(item):
            yes.append(item)
        else:
            no.append(item)
    return yes, no


def take(n: int, iterable: Iterable[T]) -> list[T]:
    """Return the first *n* items of *iterable* as a list."""
    if n < 0:
        raise ValueError("n must be non-negative")
    out: list[T] = []
    it = iter(iterable)
    for _ in range(n):
        try:
            out.append(next(it))
        except StopIteration:
            break
    return out


def drop(n: int, iterable: Iterable[T]) -> Iterator[T]:
    """Skip the first *n* items, then yield the rest."""
    if n < 0:
        raise ValueError("n must be non-negative")
    it = iter(iterable)
    for _ in range(n):
        try:
            next(it)
        except StopIteration:
            return
    yield from it


def take_while(pred: Callable[[T], bool], iterable: Iterable[T]) -> Iterator[T]:
    """Yield items from *iterable* while *pred* is true; stops at first false."""
    for item in iterable:
        if not pred(item):
            break
        yield item


def drop_while(pred: Callable[[T], bool], iterable: Iterable[T]) -> Iterator[T]:
    """Skip leading items satisfying *pred*, then yield the remainder."""
    it = iter(iterable)
    for item in it:
        if not pred(item):
            yield item
            break
    yield from it


def interleave(*iterables: Iterable[T]) -> Iterator[T]:
    """Round-robin elements from each iterable until all are exhausted.

    Shorter iterables are skipped once empty; continues with the rest.
    """
    iterators = [iter(it) for it in iterables]
    while iterators:
        next_round: list[Iterator[T]] = []
        for it in iterators:
            try:
                yield next(it)
                next_round.append(it)
            except StopIteration:
                pass
        iterators = next_round


def nth(iterable: Iterable[T], n: int, default: U | None = None) -> T | U | None:
    """Return the *n*-th element (0-based) or *default* if index out of range."""
    if n < 0:
        raise ValueError("n must be non-negative")
    it = iter(iterable)
    for _ in range(n):
        try:
            next(it)
        except StopIteration:
            return default
    try:
        return next(it)
    except StopIteration:
        return default


def first(iterable: Iterable[T], default: U | None = None) -> T | U | None:
    """Return the first item or *default* if empty."""
    it = iter(iterable)
    try:
        return next(it)
    except StopIteration:
        return default


def last(iterable: Iterable[T], default: U | None = None) -> T | U | None:
    """Return the last item or *default* if empty."""
    it = iter(iterable)
    try:
        prev = next(it)
    except StopIteration:
        return default
    for item in it:
        prev = item
    return prev


def group_consecutive(
    iterable: Iterable[T],
    key: Callable[[T], Any] | None = None,
) -> Iterator[tuple[Any, list[T]]]:
    """Group adjacent equal items; *key* defaults to identity."""
    it = iter(iterable)
    try:
        current = next(it)
    except StopIteration:
        return
    k = key(current) if key is not None else current
    group: list[T] = [current]
    for item in it:
        item_key = key(item) if key is not None else item
        if item_key == k:
            group.append(item)
        else:
            yield (k, group)
            k = item_key
            group = [item]
    yield (k, group)


def run_length_encode(iterable: Iterable[T]) -> Iterator[tuple[T, int]]:
    """Yield ``(value, count)`` for consecutive runs of equal values."""
    for _key, group in group_consecutive(iterable):
        yield (group[0], len(group))


def duplicates(iterable: Iterable[T]) -> Iterator[T]:
    """Yield items that appear more than once (second and later occurrences).

    First occurrence is suppressed; order follows *iterable*.
    """
    seen: set[T] = set()
    for item in iterable:
        if item in seen:
            yield item
        else:
            seen.add(item)


def duplicates_all(iterable: Iterable[T]) -> set[T]:
    """Return the set of values that occur more than once."""
    seen: set[T] = set()
    dup: set[T] = set()
    for item in iterable:
        if item in seen:
            dup.add(item)
        else:
            seen.add(item)
    return dup


def scan(
    func: Callable[[U, T], U],
    iterable: Iterable[T],
    initial: U,
) -> Iterator[U]:
    """Cumulative fold: yield *initial*, then ``func(acc, x)`` for each *x*."""
    acc = initial
    yield acc
    for item in iterable:
        acc = func(acc, item)
        yield acc


def enumerate_from(iterable: Iterable[T], start: int = 0) -> Iterator[tuple[int, T]]:
    """Like built-in ``enumerate`` with an explicit name for the start index."""
    i = start
    for item in iterable:
        yield (i, item)
        i += 1


def pad_none(iterable: Iterable[T]) -> Iterator[T | None]:
    """Yield items from *iterable*, then infinite ``None`` values.

    Useful with ``takewhile`` from itertools; callers usually slice externally.
    """
    yield from iterable
    while True:
        yield None


def spy(
    iterable: Iterable[T],
    n: int = 1,
) -> tuple[tuple[T, ...], Iterator[T]]:
    """Peek at the first *n* elements without consuming the full iterable.

    Returns ``(head_tuple, iterator)`` where the iterator replays *head* then
    continues the original stream.
    """
    if n < 0:
        raise ValueError("n must be non-negative")
    it = iter(iterable)
    head_list: list[T] = []
    for _ in range(n):
        try:
            head_list.append(next(it))
        except StopIteration:
            break
    head = tuple(head_list)

    def replay() -> Iterator[T]:
        yield from head
        yield from it

    return head, replay()


def cons(head: T, tail: Iterable[T]) -> Iterator[T]:
    """Yield *head* then all of *tail*."""
    yield head
    yield from tail


def concat(*iterables: Iterable[T]) -> Iterator[T]:
    """Chain iterables sequentially (shallow)."""
    for it in iterables:
        yield from it
