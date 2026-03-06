#!/usr/bin/env python3
"""String utilities - a collection of string helper functions."""


def truncate(text: str, max_length: int = 50, suffix: str = "...") -> str:
    """Truncate a string to max_length, appending suffix if truncated."""
    if len(text) <= max_length:
        return text
    return text[: max_length - len(suffix)] + suffix


def word_count(text: str) -> int:
    """Count the number of words in a string."""
    return len(text.split())


def reverse_words(text: str) -> str:
    """Reverse the order of words in a string."""
    return " ".join(reversed(text.split()))


if __name__ == "__main__":
    sample = "The quick brown fox jumps over the lazy dog"
    print("Original:", sample)
    print("Truncated:", truncate(sample, 20))
    print("Word count:", word_count(sample))
    print("Reversed words:", reverse_words(sample))
