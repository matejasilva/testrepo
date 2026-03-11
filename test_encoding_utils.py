from encoding_utils import (
    base64_encode,
    base64_decode,
    hex_encode,
    hex_decode,
    sha256_hex,
    md5_hex,
)


def test_base64_roundtrip():
    s = "hello"
    enc = base64_encode(s)
    assert base64_decode(enc) == s


def test_hex_roundtrip():
    data = b"hello"
    enc = hex_encode(data)
    assert hex_decode(enc) == data


def test_sha256_hex():
    h = sha256_hex("test")
    assert len(h) == 64
    assert all(c in "0123456789abcdef" for c in h)


def test_md5_hex():
    h = md5_hex("test")
    assert len(h) == 32
