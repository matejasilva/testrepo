# Dict Utilities Module

A collection of dictionary helper functions for common dict manipulation tasks.

## Installation

The `dict_utils` module is part of this project. Import as:

```python
from utils import deep_merge, flatten_keys, unflatten_keys, invert, filter_keys, omit_keys, map_values, map_keys, get_nested, set_nested
```

## CLI

Dict utils are used internally; use the Python API for dict operations.

## Functions

### `deep_merge(base: dict, override: dict) -> dict`

Recursively merge override into base. Override values take precedence.

```python
deep_merge({"a": 1, "b": {"x": 1}}, {"b": {"y": 2}})  # {"a": 1, "b": {"x": 1, "y": 2}}
```

### `flatten_keys(d: dict, parent_key: str = "", sep: str = ".") -> dict`

Flatten nested dict to single level with dotted keys.

```python
flatten_keys({"a": {"b": {"c": 1}}})  # {"a.b.c": 1}
```

### `unflatten_keys(d: dict, sep: str = ".") -> dict`

Convert flattened dict with dotted keys back to nested structure.

```python
unflatten_keys({"a.b.c": 1})  # {"a": {"b": {"c": 1}}}
```

### `invert(d: dict) -> dict`

Invert dict: values become keys, keys collected in lists (handles duplicates).

```python
invert({"a": 1, "b": 1, "c": 2})  # {1: ["a", "b"], 2: ["c"]}
```

### `filter_keys(d: dict, keys: set | list) -> dict`

Return dict containing only the specified keys.

```python
filter_keys({"a": 1, "b": 2, "c": 3}, ["a", "c"])  # {"a": 1, "c": 3}
```

### `omit_keys(d: dict, keys: set | list) -> dict`

Return dict excluding the specified keys.

```python
omit_keys({"a": 1, "b": 2, "c": 3}, ["b"])  # {"a": 1, "c": 3}
```

### `map_values(d: dict, fn: Callable) -> dict`

Apply function to each value, return new dict.

```python
map_values({"a": 1, "b": 2}, lambda x: x * 2)  # {"a": 2, "b": 4}
```

### `map_keys(d: dict, fn: Callable) -> dict`

Apply function to each key, return new dict.

```python
map_keys({"a": 1, "b": 2}, str.upper)  # {"A": 1, "B": 2}
```

### `get_nested(d: dict, path: str | list, default=None, sep=".") -> Any`

Get value at dotted path.

```python
get_nested({"a": {"b": {"c": 42}}}, "a.b.c")  # 42
get_nested({"a": 1}, "x.y", default=99)  # 99
```

### `set_nested(d: dict, path: str | list, value: Any, sep=".") -> None`

Set value at dotted path. Mutates d in place.

```python
d = {}
set_nested(d, "a.b.c", 42)  # d == {"a": {"b": {"c": 42}}}
```

## Running Tests

```bash
pytest test_dict_utils.py -v
```
