import tempfile
from pathlib import Path

from utils.json_utils import dump_file, dumps_pretty, get_path, load_file, loads_safe


def test_loads_safe():
    assert loads_safe('{"a": 1}') == {"a": 1}
    assert loads_safe("invalid", default={}) == {}
    assert loads_safe("null") is None


def test_dumps_pretty():
    s = dumps_pretty({"a": 1})
    assert "a" in s and "1" in s


def test_load_dump_file():
    obj = {"x": 1, "y": [2, 3]}
    with tempfile.NamedTemporaryFile(suffix=".json", delete=False) as f:
        p = f.name
    try:
        dump_file(obj, p)
        loaded = load_file(p)
        assert loaded == obj
    finally:
        Path(p).unlink(missing_ok=True)


def test_get_path():
    d = {"a": {"b": {"c": 42}}}
    assert get_path(d, "a.b.c") == 42
    assert get_path(d, "a.x", default=99) == 99
