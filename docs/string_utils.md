# string_utils

Basic string helper functions.

## Functions

| Function | Description |
|----------|-------------|
| `truncate(s, max_len, suffix="...")` | Truncate s to max_len, appending suffix if truncated |
| `is_palindrome(s)` | Return True if s reads the same forwards and backwards (ignores case) |
| `word_count(s)` | Return the number of words in s (split on whitespace) |
| `reverse_words(s)` | Return s with the order of words reversed |
| `capitalize_words(s)` | Return s with the first letter of each word capitalized |
| `strip_extra_spaces(s)` | Collapse runs of whitespace to a single space and strip leading/trailing whitespace |

## Example

```python
from string_utils import strip_extra_spaces, word_count

strip_extra_spaces("  hello   world  ")  # -> "hello world"
word_count("one two three")              # -> 3
```
