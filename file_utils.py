#!/usr/bin/env python3
"""File utilities - path and file helper functions."""

import os


def safe_filename(s: str, replacement: str = "_") -> str:
    """Replace unsafe filename characters with replacement."""
    unsafe = '<>:"/\\|?*'
    for c in unsafe:
        s = s.replace(c, replacement)
    return s.strip().rstrip(".")


def split_extension(path: str) -> tuple[str, str]:
    """Split path into (base, extension). Handles double extensions like .tar.gz."""
    basename = os.path.basename(path)
    if basename.startswith("."):
        return path, ""
    parts = basename.rsplit(".", 2)
    if len(parts) == 1:
        return path, ""
    if len(parts) == 2:
        return path.rsplit(".", 1)[0], "." + parts[1]
    # .tar.gz etc - keep last two
    base = path[: -len(parts[-1]) - len(parts[-2]) - 2]
    return base, "." + parts[-2] + "." + parts[-1]


def ensure_dir(path: str) -> str:
    """Create directory if it doesn't exist. Return path."""
    os.makedirs(path, exist_ok=True)
    return path


def file_size_human(size_bytes: int) -> str:
    """Format byte count as human-readable string."""
    for unit in ("B", "KB", "MB", "GB", "TB"):
        if size_bytes < 1024:
            return f"{size_bytes:.1f}{unit}"
        size_bytes /= 1024
    return f"{size_bytes:.1f}PB"


def path_parts(path: str) -> list[str]:
    """Split path into components, normalizing separators."""
    return [p for p in path.replace("\\", "/").split("/") if p]
