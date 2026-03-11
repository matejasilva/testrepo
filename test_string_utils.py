import pytest
from string_utils import (
    strip_extra_spaces,
    capitalize_words,
    word_count,
    truncate,
    reverse_words,
    is_palindrome,
    wrap_text,
    normalize_whitespace,
)


class TestStripExtraSpaces:
    def test_collapses_multiple_spaces(self):
        assert strip_extra_spaces("  hello   world  ") == "hello world"

    def test_strips_leading_trailing(self):
        assert strip_extra_spaces("  hello  ") == "hello"

    def test_handles_tabs_and_newlines(self):
        assert strip_extra_spaces("hello\t\t\n\nworld") == "hello world"

    def test_empty_string(self):
        assert strip_extra_spaces("") == ""

    def test_single_word(self):
        assert strip_extra_spaces("  hello  ") == "hello"


class TestCapitalizeWords:
    def test_basic(self):
        assert capitalize_words("hello world") == "Hello World"

    def test_strips_extra_spaces_first(self):
        assert capitalize_words("  hello   world  ") == "Hello World"

    def test_single_word(self):
        assert capitalize_words("hello") == "Hello"

    def test_empty_string(self):
        assert capitalize_words("") == ""


class TestWordCount:
    def test_multiple_words(self):
        assert word_count("hello world from string utils") == 5

    def test_empty_string(self):
        assert word_count("") == 0

    def test_whitespace_only(self):
        assert word_count("   ") == 0

    def test_single_word(self):
        assert word_count("hello") == 1


class TestTruncate:
    def test_no_truncation_needed(self):
        assert truncate("hello", 10) == "hello"

    def test_truncates_with_ellipsis(self):
        assert truncate("hello world", 8) == "hello..."

    def test_exact_length(self):
        assert truncate("hello", 5) == "hello"

    def test_custom_suffix(self):
        assert truncate("hello world", 9, "…") == "hello wo…"

    def test_short_max_length_returns_suffix_only(self):
        assert truncate("hello", 3) == "..."


class TestReverseWords:
    def test_basic(self):
        assert reverse_words("hello world") == "world hello"

    def test_multiple_words(self):
        assert reverse_words("one two three four") == "four three two one"

    def test_single_word(self):
        assert reverse_words("hello") == "hello"

    def test_strips_extra_spaces(self):
        assert reverse_words("  hello   world  ") == "world hello"


class TestIsPalindrome:
    def test_true_classic(self):
        assert is_palindrome("racecar")

    def test_true_with_spaces(self):
        assert is_palindrome("A man a plan a canal Panama")

    def test_false(self):
        assert not is_palindrome("hello")

    def test_empty(self):
        assert is_palindrome("")

    def test_single_char(self):
        assert is_palindrome("a")


class TestWrapText:
    def test_wraps_at_width(self):
        result = wrap_text("Hello world from string utils", 12)
        assert result == ["Hello world", "from string", "utils"]

    def test_short_text(self):
        assert wrap_text("hi", 80) == ["hi"]

    def test_invalid_width_raises(self):
        with pytest.raises(ValueError, match="width must be positive"):
            wrap_text("hello", 0)


class TestNormalizeWhitespace:
    def test_replaces_multiple_spaces(self):
        assert normalize_whitespace("hello    world") == "hello world"

    def test_replaces_tabs_and_newlines(self):
        assert normalize_whitespace("hello\t\nworld") == "hello world"

    def test_custom_replacement(self):
        assert normalize_whitespace("hello  world", "_") == "hello_world"
