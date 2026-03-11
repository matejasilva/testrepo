#!/usr/bin/env python3
"""Encoding utilities - encode/decode helpers."""

import base64
import hashlib


def base64_encode(s: str | bytes, encoding: str = "utf-8") -> str:
    """Base64 encode string or bytes."""
    if isinstance(s, str):
        s = s.encode(encoding)
    return base64.b64encode(s).decode("ascii")


def base64_decode(s: str, encoding: str = "utf-8") -> str:
    """Base64 decode to string."""
    return base64.b64decode(s).decode(encoding)


def hex_encode(data: bytes) -> str:
    """Encode bytes to hex string."""
    return data.hex()


def hex_decode(s: str) -> bytes:
    """Decode hex string to bytes."""
    return bytes.fromhex(s)


def sha256_hex(s: str | bytes, encoding: str = "utf-8") -> str:
    """Compute SHA256 hash as hex string."""
    if isinstance(s, str):
        s = s.encode(encoding)
    return hashlib.sha256(s).hexdigest()


def md5_hex(s: str | bytes, encoding: str = "utf-8") -> str:
    """Compute MD5 hash as hex string."""
    if isinstance(s, str):
        s = s.encode(encoding)
    return hashlib.md5(s).hexdigest()
