import pytest

from utils.validation_utils import is_valid_email, is_valid_phone, is_valid_url


@pytest.mark.parametrize("email", [
    "user@example.com",
    "test.user@domain.co",
    "a+b@foo.bar",
    "name@sub.domain.org",
])
def test_is_valid_email_valid(email):
    assert is_valid_email(email) is True


@pytest.mark.parametrize("email", [
    "",
    "notanemail",
    "missing@domain",
    "@nodomain.com",
    "nodomain@.com",
    "spaces in@email.com",
])
def test_is_valid_email_invalid(email):
    assert is_valid_email(email) is False


@pytest.mark.parametrize("url", [
    "http://example.com",
    "https://example.com",
    "https://sub.domain.org/path",
])
def test_is_valid_url_valid(url):
    assert is_valid_url(url) is True


@pytest.mark.parametrize("url", [
    "",
    "example.com",
    "ftp://example.com",
    "http://",
])
def test_is_valid_url_invalid(url):
    assert is_valid_url(url) is False


@pytest.mark.parametrize("phone", [
    "1234567",
    "123-456-7890",
    "+1 234 567 8901",
    "555 123 4567",
])
def test_is_valid_phone_valid(phone):
    assert is_valid_phone(phone) is True


@pytest.mark.parametrize("phone", [
    "",
    "123",
    "123456",
])
def test_is_valid_phone_invalid(phone):
    assert is_valid_phone(phone) is False
