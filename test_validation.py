from validation import (
    is_email,
    is_url,
    is_positive_int,
    is_non_empty_str,
    in_range,
    one_of,
    has_required_keys,
)


def test_is_email():
    assert is_email("user@example.com")
    assert not is_email("invalid")
    assert not is_email("")


def test_is_url():
    assert is_url("https://example.com")
    assert not is_url("ftp://x.com")


def test_is_positive_int():
    assert is_positive_int(1)
    assert not is_positive_int(0)
    assert not is_positive_int(-1)


def test_is_non_empty_str():
    assert is_non_empty_str("x")
    assert not is_non_empty_str("   ")
    assert not is_non_empty_str(123)


def test_in_range():
    assert in_range(5, 0, 10)
    assert not in_range(15, 0, 10)


def test_one_of():
    assert one_of("a", ["a", "b", "c"])
    assert not one_of("z", ["a", "b"])


def test_has_required_keys():
    assert has_required_keys({"a": 1, "b": 2}, ["a", "b"])
    assert not has_required_keys({"a": 1}, ["a", "b"])
