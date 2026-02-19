import pytest
from slugify import slugify, SlugifyError


@pytest.mark.parametrize("input_text, expected", [
    ("Hello World", "hello-world"),
    ("Python_is Great!", "python-is-great"),
    ("  Multiple   Spaces  ", "multiple-spaces"),
    ("Café del Mar", "cafe-del-mar"),
    ("123 Testing 456", "123-testing-456"),
])
def test_slugify_valid(input_text, expected):
    assert slugify(input_text) == expected


@pytest.mark.parametrize("invalid_input", [
    "",
    "   ",
    None,
])
def test_slugify_invalid(invalid_input):
    with pytest.raises(SlugifyError):
        slugify(invalid_input)


def test_slugify_only_symbols():
    with pytest.raises(SlugifyError):
        slugify("!!!@@@###")


def test_idempotency():
    text = "Hello World!"
    assert slugify(slugify(text)) == slugify(text)
