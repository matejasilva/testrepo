#!/usr/bin/env python3
"""Text utilities - text processing helpers."""

__all__ = ["lines", "bullet_list", "indent", "dedent", "width_wrap"]


def lines(text: str) -> list[str]:
    """Split text into lines, strip whitespace, skip empty."""
    return [ln.strip() for ln in text.splitlines() if ln.strip()]


def bullet_list(items: list[str], bullet: str = "-") -> str:
    """Format list as bullet points."""
    return "\n".join(f"{bullet} {item}" for item in items)


def indent(text: str, spaces: int = 2) -> str:
    """Indent each line by given spaces."""
    pad = " " * spaces
    return "\n".join(pad + ln for ln in text.splitlines())


def dedent(text: str) -> str:
    """Remove common leading whitespace from all lines."""
    lines_list = text.splitlines()
    if not lines_list:
        return ""
    min_indent = min(len(ln) - len(ln.lstrip()) for ln in lines_list if ln.strip())
    return "\n".join(ln[min_indent:] if len(ln) > min_indent else ln for ln in lines_list)


def width_wrap(text: str, width: int = 80) -> str:
    """Wrap text to width, breaking on word boundaries."""
    words = text.split()
    lines_list: list[str] = []
    current: list[str] = []
    current_len = 0
    for w in words:
        need = len(w) + (1 if current else 0)
        if current_len + need <= width:
            current.append(w)
            current_len += need
        else:
            if current:
                lines_list.append(" ".join(current))
            current = [w]
            current_len = len(w)
    if current:
        lines_list.append(" ".join(current))
    return "\n".join(lines_list)
