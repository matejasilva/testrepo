# Duration Utilities

Parse and format duration strings (e.g. `1h 30m 15s`).

## Usage

```python
from utils import parse_duration, format_duration, multiply_duration, add_durations, subtract_durations
```

## Functions

- `parse_duration(duration: str) -> int` — Parse string to total seconds
- `format_duration(seconds: int) -> str` — Convert seconds to duration string
- `multiply_duration(duration: str, factor: int | float) -> str` — Multiply duration by factor
- `add_durations(a: str, b: str) -> str` — Sum two duration strings (e.g. `"1h 30m"` + `"45m"` → `"2h 15m"`)
- `subtract_durations(a: str, b: str) -> str` — Subtract second from first; raises if the result would be negative

## CLI

```bash
utils duration parse "1h 30m"
utils duration format 5400
utils duration multiply "1h" 2.5
utils duration subtract "2h 15m" "45m"
```
