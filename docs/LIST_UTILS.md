# List Utilities Module

A collection of list helper functions for common list manipulation tasks.

## Installation

The `list_utils` module is part of this project. Import as:

```python
from list_utils import flatten, deep_flatten, chunk, unique, pairwise, rotate, partition, interleave, sliding_window
```

## Functions

### `flatten(nested: list) -> list`

Flatten a nested list one level deep.

```python
flatten([[1, 2], [3, 4], 5])  # [1, 2, 3, 4, 5]
```

### `deep_flatten(nested: list) -> list`

Recursively flatten a nested list of any depth.

```python
deep_flatten([[1, [2, 3]], [4, [5, [6]]]])  # [1, 2, 3, 4, 5, 6]
```

### `chunk(lst: list[T], size: int) -> list[list[T]]`

Split list into chunks of given size.

```python
chunk([1, 2, 3, 4, 5], 2)  # [[1, 2], [3, 4], [5]]
```

### `unique(lst: list[T], key: Callable | None = None) -> list[T]`

Return list with duplicates removed, preserving order. Optional `key` for custom equality.

```python
unique([1, 2, 2, 3, 1, 4])  # [1, 2, 3, 4]
unique(["a", "A", "b"], key=str.lower)  # ["a", "b"]
```

### `pairwise(lst: list[T]) -> list[tuple[T, T]]`

Return successive overlapping pairs from the list.

```python
pairwise([1, 2, 3, 4])  # [(1, 2), (2, 3), (3, 4)]
```

### `rotate(lst: list[T], n: int) -> list[T]`

Rotate list left by n positions (negative n rotates right).

```python
rotate([1, 2, 3, 4, 5], 2)   # [3, 4, 5, 1, 2]
rotate([1, 2, 3, 4, 5], -2)  # [4, 5, 1, 2, 3]
```

### `partition(lst: list[T], predicate: Callable[[T], bool]) -> tuple[list[T], list[T]]`

Split list into (matching, non-matching) based on predicate.

```python
partition([1, 2, 3, 4, 5], lambda x: x % 2 == 0)  # ([2, 4], [1, 3, 5])
```

### `interleave(*lists: list[T]) -> list[T]`

Interleave elements from multiple lists (stops at shortest).

```python
interleave([1, 2], ["a", "b"], [10, 20])  # [1, "a", 10, 2, "b", 20]
```

### `sliding_window(lst: list[T], size: int) -> list[tuple[T, ...]]`

Return sliding windows of given size.

```python
sliding_window([1, 2, 3, 4], 2)  # [(1, 2), (2, 3), (3, 4)]
```

## Running Tests

```bash
pytest test_list_utils.py -v
```
