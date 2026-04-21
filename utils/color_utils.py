#!/usr/bin/env python3
"""Color utilities - color conversion and formatting helpers."""

__all__ = [
    "hex_to_rgb",
    "rgb_to_hex",
    "rgb_to_grayscale",
    "is_dark",
    "contrast_color",
]


def hex_to_rgb(hex_str: str) -> tuple[int, int, int]:
    """Convert #RRGGBB to (r, g, b)."""
    hex_str = hex_str.lstrip("#")
    return (
        int(hex_str[0:2], 16),
        int(hex_str[2:4], 16),
        int(hex_str[4:6], 16),
    )


def rgb_to_hex(r: int, g: int, b: int) -> str:
    """Convert (r, g, b) to #RRGGBB."""
    return f"#{r:02x}{g:02x}{b:02x}"


def rgb_to_grayscale(r: int, g: int, b: int) -> int:
    """Convert RGB to grayscale (0-255)."""
    return int(0.299 * r + 0.587 * g + 0.114 * b)


def is_dark(r: int, g: int, b: int, threshold: int = 128) -> bool:
    """Return True if color is dark (suitable for light text)."""
    return rgb_to_grayscale(r, g, b) < threshold


def contrast_color(hex_str: str) -> str:
    """Return #000000 or #ffffff for best contrast on given background."""
    r, g, b = hex_to_rgb(hex_str)
    return "#ffffff" if is_dark(r, g, b) else "#000000"
