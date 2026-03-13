# Ticket 003: Validation Utilities Module

## Status
Open

## Description
Create a new `validation_utils.py` module with helper functions to validate common string formats (email, URL, phone). Keep it simple and focused — no external dependencies.

## Acceptance Criteria
- [ ] `is_valid_email(s: str) -> bool` — basic email format validation (local@domain.tld)
- [ ] `is_valid_url(s: str) -> bool` — basic URL validation (http/https schemes)
- [ ] `is_valid_phone(s: str) -> bool` — flexible phone number validation (digits, spaces, dashes, optional +prefix)
- [ ] Matching `test_validation_utils.py` with tests for valid and invalid inputs
- [ ] Docstrings and consistent style with existing utils

## Notes
- Use regex or manual parsing; no `email-validator` or similar packages
- Aim for practical validation, not RFC-perfect
