from regex_utils import extract_first, extract_all, replace_all, split_regex


def test_extract_first():
    assert extract_first(r"\d+", "abc123def") == "123"
    assert extract_first(r"x", "abc") is None


def test_extract_all():
    assert extract_all(r"\d+", "a1b2c3") == ["1", "2", "3"]


def test_replace_all():
    assert replace_all(r"\s+", "-", "a b  c") == "a-b-c"


def test_split_regex():
    assert split_regex(r"\s+", "a b  c") == ["a", "b", "c"]
