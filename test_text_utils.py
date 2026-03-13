from utils.text_utils import lines, bullet_list, indent, dedent, width_wrap


def test_lines():
    assert lines("  a  \n  b  \n\n  c  ") == ["a", "b", "c"]


def test_bullet_list():
    result = bullet_list(["x", "y"], bullet="-")
    assert "- x" in result and "- y" in result


def test_indent():
    assert indent("a\nb", 2) == "  a\n  b"


def test_dedent():
    text = "  a\n  b\n    c"
    assert "a" in dedent(text) and "c" in dedent(text)


def test_width_wrap():
    result = width_wrap("hello world foo bar", width=10)
    assert len(result.splitlines()) >= 2
