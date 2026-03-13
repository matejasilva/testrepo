# Utils Documentation

Index of all module documentation.

## Modules

| Module | Description |
|--------|-------------|
| [COLOR_UTILS](COLOR_UTILS.md) | Color conversion (hex, RGB, contrast) |
| [DICT_UTILS](DICT_UTILS.md) | Dictionary helpers (merge, flatten, invert, etc.) |
| [JSON_UTILS](JSON_UTILS.md) | JSON parse/serialize helpers |
| [STRING_UTILS](string_utils.md) | String helpers (truncate, palindrome, word_count) |
| [TEXT_UTILS](TEXT_UTILS.md) | Text processing (lines, bullet_list, indent) |
| [duration](duration.md) | Duration parse/format (1h 30m) |
| [retry](retry.md) | Retry decorator |
| [validation_utils](validation_utils.md) | Email, URL, phone validation |
| [number_utils](number_utils.md) | clamp, sign, is_even, digits |
| [math_utils](math_utils.md) | is_prime |
| [roman](roman.md) | Roman numeral conversion |
| [slugify](slugify.md) | URL-friendly slug generation |

## Usage

```python
from utils import truncate, parse_duration, is_valid_email
# or
from utils.duration import parse_duration, format_duration
```

## CLI

```bash
utils --help
utils string truncate "hello world" 5
utils duration parse "1h 30m"
utils json pretty '{"a":1}'
utils validation email user@example.com
```
