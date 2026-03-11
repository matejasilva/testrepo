#!/usr/bin/env python3
"""String utilities - a collection of string helper functions."""

import re


def strip_extra_spaces(s: str) -> str:
    """Collapse runs of whitespace to a single space and strip leading/trailing whitespace."""
    return " ".join(s.split())


def capitalize_words(s: str) -> str:
    """Capitalize the first letter of each word in the string."""
    return " ".join(word.capitalize() for word in strip_extra_spaces(s).split())


def word_count(s: str) -> int:
    """Return the number of words in the string."""
    return len(strip_extra_spaces(s).split()) if s.strip() else 0


def truncate(s: str, max_length: int, suffix: str = "...") -> str:
    """Truncate string to max_length, appending suffix if truncated."""
    if len(s) <= max_length:
        return s
    if max_length <= len(suffix):
        return suffix[:max_length]
    return s[: max_length - len(suffix)] + suffix


def reverse_words(s: str) -> str:
    """Reverse the order of words in the string."""
    words = strip_extra_spaces(s).split()
    return " ".join(reversed(words))


def is_palindrome(s: str, ignore_case: bool = True, ignore_spaces: bool = True) -> bool:
    """Return True if the string is a palindrome."""
    cleaned = s
    if ignore_spaces:
        cleaned = "".join(s.split())
    if ignore_case:
        cleaned = cleaned.lower()
    return cleaned == cleaned[::-1]


def wrap_text(text: str, width: int = 80) -> list[str]:
    """Wrap text into lines of at most width characters."""
    if width <= 0:
        raise ValueError("width must be positive")
    words = strip_extra_spaces(text).split()
    if not words:
        return [""]
    lines = []
    current_line = []
    current_length = 0

    for word in words:
        need_space = len(current_line) > 0
        word_len = len(word) + (1 if need_space else 0)

        if current_length + word_len <= width:
            current_line.append(word)
            current_length += word_len
        else:
            if current_line:
                lines.append(" ".join(current_line))
            current_line = [word]
            current_length = len(word)

    if current_line:
        lines.append(" ".join(current_line))

    return lines


def normalize_whitespace(s: str, replace_with: str = " ") -> str:
    """Replace all whitespace sequences (spaces, tabs, newlines) with replace_with."""
    return re.sub(r"\s+", replace_with, s).strip()


if __name__ == "__main__":
    print("strip_extra_spaces:", repr(strip_extra_spaces("  hello   world  ")))
    print("capitalize_words:", capitalize_words("hello world"))
    print("word_count:", word_count("hello world from string utils"))
    print("truncate:", truncate("hello world", 8))
    print("reverse_words:", reverse_words("hello world"))
    print("is_palindrome:", is_palindrome("A man a plan a canal Panama"))
    print("wrap_text:", wrap_text("Hello world from string utils", 12))
