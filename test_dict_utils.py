from __future__ import annotations

import pytest
from utils.dict_utils import (
    deep_merge,
    flatten_keys,
    unflatten_keys,
    invert,
    filter_keys,
    omit_keys,
    map_values,
    map_keys,
    get_nested,
    set_nested,
)


class TestDeepMerge:
    def test_shallow_override(self):
        result = deep_merge({"a": 1, "b": 2}, {"b": 3, "c": 4})
        assert result == {"a": 1, "b": 3, "c": 4}

    def test_nested_merge(self):
        result = deep_merge({"a": {"x": 1, "y": 2}}, {"a": {"y": 3, "z": 4}})
        assert result == {"a": {"x": 1, "y": 3, "z": 4}}

    def test_empty_override(self):
        assert deep_merge({"a": 1}, {}) == {"a": 1}

    def test_empty_base(self):
        assert deep_merge({}, {"a": 1}) == {"a": 1}


class TestFlattenKeys:
    def test_nested(self):
        assert flatten_keys({"a": {"b": {"c": 1}}}) == {"a.b.c": 1}

    def test_multiple_keys(self):
        d = {"a": {"x": 1}, "b": {"y": 2}}
        assert flatten_keys(d) == {"a.x": 1, "b.y": 2}

    def test_mixed(self):
        d = {"a": 1, "b": {"c": 2}}
        assert flatten_keys(d) == {"a": 1, "b.c": 2}

    def test_custom_sep(self):
        assert flatten_keys({"a": {"b": 1}}, sep="_") == {"a_b": 1}


class TestUnflattenKeys:
    def test_simple(self):
        assert unflatten_keys({"a.b.c": 1}) == {"a": {"b": {"c": 1}}}

    def test_roundtrip(self):
        d = {"a": {"b": 1}, "x": {"y": {"z": 2}}}
        flat = flatten_keys(d)
        assert unflatten_keys(flat) == d


class TestInvert:
    def test_unique_values(self):
        assert invert({"a": 1, "b": 2, "c": 3}) == {1: ["a"], 2: ["b"], 3: ["c"]}

    def test_duplicate_values(self):
        assert invert({"a": 1, "b": 1, "c": 2}) == {1: ["a", "b"], 2: ["c"]}


class TestFilterKeys:
    def test_basic(self):
        assert filter_keys({"a": 1, "b": 2, "c": 3}, ["a", "c"]) == {"a": 1, "c": 3}

    def test_with_set(self):
        assert filter_keys({"a": 1, "b": 2}, {"a"}) == {"a": 1}

    def test_missing_keys_ignored(self):
        assert filter_keys({"a": 1, "b": 2}, ["a", "z"]) == {"a": 1}


class TestOmitKeys:
    def test_basic(self):
        assert omit_keys({"a": 1, "b": 2, "c": 3}, ["b"]) == {"a": 1, "c": 3}

    def test_nonexistent_key(self):
        assert omit_keys({"a": 1}, ["z"]) == {"a": 1}


class TestMapValues:
    def test_double(self):
        assert map_values({"a": 1, "b": 2}, lambda x: x * 2) == {"a": 2, "b": 4}

    def test_str(self):
        assert map_values({"a": 1, "b": 2}, str) == {"a": "1", "b": "2"}


class TestMapKeys:
    def test_upper(self):
        assert map_keys({"a": 1, "b": 2}, str.upper) == {"A": 1, "B": 2}


class TestGetNested:
    def test_exists(self):
        d = {"a": {"b": {"c": 42}}}
        assert get_nested(d, "a.b.c") == 42

    def test_default_missing(self):
        assert get_nested({"a": 1}, "a.b.c", default=99) == 99

    def test_list_path(self):
        assert get_nested({"a": {"b": 1}}, ["a", "b"]) == 1


class TestSetNested:
    def test_create_path(self):
        d = {}
        set_nested(d, "a.b.c", 42)
        assert d == {"a": {"b": {"c": 42}}}

    def test_overwrite(self):
        d = {"a": {"b": 1}}
        set_nested(d, "a.b", 99)
        assert d == {"a": {"b": 99}}
