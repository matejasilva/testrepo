# Ticket 002: Add consistent logging across all utils modules

**Priority:** Medium  
**Effort:** Medium  
**Component:** All utils

## Description

Add structured logging to all utility modules so callers can optionally enable debug/info output. Each module should use a shared logger namespace (e.g. `utils.string_utils`, `utils.json_utils`) and log at appropriate levels for key operations.

## File changes (12 files)

1. **`logging_config.py`** (new) – Shared logging setup, formatters, and logger factory
2. **`string_utils.py`** – Add logger, log inputs/outputs for `capitalize_words`, `strip_extra_spaces`, etc.
3. **`text_utils.py`** – Add logger, log for `truncate`, `word_wrap`, etc.
4. **`json_utils.py`** – Add logger, log parse/serialize ops and path lookups
5. **`color_utils.py`** – Add logger, log color conversions
6. **`number_utils.py`** – Add logger, log clamping/formatting
7. **`retry.py`** – Add logger, log retry attempts and backoff
8. **`docs/EXTRA_UTILS_README.md`** – Document logging usage and env vars
9. **`test_string_utils.py`** – Add tests for logging output (optional capture)
10. **`test_json_utils.py`** – Add tests for logging output
11. **`test_color_utils.py`** – Add tests for logging output
12. **`test_number_utils.py`** – Add tests for logging output

## Acceptance criteria

- [ ] `logging_config.py` defines shared setup and `get_logger(module_name)`
- [ ] All 6 utils modules use the shared logger with correct namespaces
- [ ] Log level controllable via `LOG_LEVEL` env var or explicit config
- [ ] No performance impact when logging disabled (use `logger.isEnabledFor()` or lazy args)
- [ ] README documents how to enable and configure logging
- [ ] At least 4 test files verify logging behavior (no regressions when disabled)

## Notes

Use `logging.getLogger(__name__)` pattern. Consider `structlog` or stdlib `logging` only to avoid new deps. Ensure tests can assert log calls without polluting test output.
