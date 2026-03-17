# Ticket 006: Add UtilsError Base Class and Unify Custom Exceptions

## Status
Open

## Description
Introduce a shared `UtilsError` base class in a new `utils/exceptions.py` module, then refactor all custom exceptions (`RomanNumeralError`, `SlugifyError`, `DurationFormatError`, `RetryError`) to inherit from it. This enables consumers to catch `UtilsError` for any utils-related failure.

## Scope (Estimated ~11 files changed)

### 1. New Module
- Create `utils/exceptions.py` with `UtilsError(Exception)` base class

### 2. Refactor Exception Definitions (~4 files)
- `utils/roman.py` — `RomanNumeralError(UtilsError)` instead of `RomanNumeralError(ValueError)`
- `utils/slugify.py` — `SlugifyError(UtilsError)` instead of `SlugifyError(ValueError)`
- `utils/duration.py` — `DurationFormatError(UtilsError)` instead of `DurationFormatError(ValueError)`
- `utils/retry.py` — `RetryError(UtilsError)` instead of `RetryError(Exception)`

### 3. Package Exports
- `utils/__init__.py` — add `UtilsError` import and export in `__all__`

### 4. Tests (~4 files)
- `test_roman.py` — optionally add test that `RomanNumeralError` is instance of `UtilsError`
- `test_slugify.py` — same for `SlugifyError`
- `test_duration.py` — same for `DurationFormatError`
- `test_retry.py` — same for `RetryError`

### 5. Documentation
- `docs/README.md` or new `docs/exceptions.md` — document `UtilsError` and exception hierarchy

## Acceptance Criteria
- [ ] `utils/exceptions.py` exists with `UtilsError` base class
- [ ] All four custom exceptions inherit from `UtilsError`
- [ ] `from utils import UtilsError` works; `UtilsError` in `__all__`
- [ ] `isinstance(RomanNumeralError("x"), UtilsError)` is `True` (and similarly for others)
- [ ] All existing tests pass
- [ ] Brief documentation of exception hierarchy

## Notes
- Keep existing exception names; only change the base class
- `UtilsError` should inherit from `Exception` for broad compatibility
- Consider adding `utils.exceptions` to `__init__.py` re-exports if needed
