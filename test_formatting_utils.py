from formatting_utils import (
    pluralize,
    format_number,
    truncate_str,
    pad_left,
    pad_right,
    percent_str,
)


def test_pluralize():
    assert pluralize(1, "item") == "item"
    assert pluralize(2, "item") == "items"
    assert pluralize(2, "child", "children") == "children"


def test_format_number():
    assert "1,000" in format_number(1000) or "1000" in format_number(1000)


def test_truncate_str():
    assert truncate_str("hello world", 8) == "hello..."


def test_pad_left():
    assert pad_left("x", 5) == "    x"


def test_pad_right():
    assert pad_right("x", 5) == "x    "


def test_percent_str():
    assert "50" in percent_str(1, 2)
    assert percent_str(0, 0) == "0%"
