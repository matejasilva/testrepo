# String Utilities Module

A collection of string helper functions for common text processing tasks.

## Installation

The `string_utils` module is part of this project. Import as:

```python
from string_utils import strip_extra_spaces, capitalize_words, word_count, truncate, reverse_words, is_palindrome, wrap_text, normalize_whitespace
```

## Functions

### `strip_extra_spaces(s: str) -> str`

Collapses runs of whitespace to a single space and strips leading/trailing whitespace.

```python
strip_extra_spaces("  hello   world  ")  # "hello world"
```

### `capitalize_words(s: str) -> str`

Capitalize the first letter of each word in the string.

```python
capitalize_words("hello world")  # "Hello World"
```

### `word_count(s: str) -> int`

Return the number of words in the string.

```python
word_count("hello world from string utils")  # 5
```

### `truncate(s: str, max_length: int, suffix: str = "...") -> str`

Truncate string to max_length, appending suffix if truncated.

```python
truncate("hello world", 8)  # "hello..."
```

### `reverse_words(s: str) -> str`

Reverse the order of words in the string.

```python
reverse_words("hello world")  # "world hello"
```

### `is_palindrome(s: str, ignore_case: bool = True, ignore_spaces: bool = True) -> bool`

Return True if the string is a palindrome.

```python
is_palindrome("A man a plan a canal Panama")  # True
is_palindrome("racecar")  # True
```

### `wrap_text(text: str, width: int = 80) -> list[str]`

Wrap text into lines of at most width characters.

```python
wrap_text("Hello world from string utils", 12)  # ["Hello world", "from string", "utils"]
```

### `normalize_whitespace(s: str, replace_with: str = " ") -> str`

Replace all whitespace sequences (spaces, tabs, newlines) with replace_with.

```python
normalize_whitespace("hello\t\nworld")  # "hello world"
```

## Running Tests

```bash
pytest test_string_utils.py -v
```
