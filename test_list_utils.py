import pytest
from list_utils import (
    flatten,
    deep_flatten,
    chunk,
    unique,
    pairwise,
    rotate,
    partition,
    interleave,
    sliding_window,
)


class TestFlatten:
    def test_one_level(self):
        assert flatten([[1, 2], [3, 4]]) == [1, 2, 3, 4]

    def test_mixed_items(self):
        assert flatten([[1, 2], 3, [4]]) == [1, 2, 3, 4]

    def test_empty(self):
        assert flatten([]) == []

    def test_single_list(self):
        assert flatten([[1, 2, 3]]) == [1, 2, 3]


class TestDeepFlatten:
    def test_nested(self):
        assert deep_flatten([[1, [2, 3]], [4, [5, [6]]]]) == [1, 2, 3, 4, 5, 6]

    def test_one_level(self):
        assert deep_flatten([[1, 2], [3, 4]]) == [1, 2, 3, 4]

    def test_empty(self):
        assert deep_flatten([]) == []


class TestChunk:
    def test_even_split(self):
        assert chunk([1, 2, 3, 4], 2) == [[1, 2], [3, 4]]

    def test_uneven_split(self):
        assert chunk([1, 2, 3, 4, 5], 2) == [[1, 2], [3, 4], [5]]

    def test_size_one(self):
        assert chunk([1, 2, 3], 1) == [[1], [2], [3]]

    def test_size_larger_than_list(self):
        assert chunk([1, 2], 5) == [[1, 2]]

    def test_invalid_size_raises(self):
        with pytest.raises(ValueError, match="size must be positive"):
            chunk([1, 2, 3], 0)
        with pytest.raises(ValueError, match="size must be positive"):
            chunk([1, 2, 3], -1)


class TestUnique:
    def test_removes_duplicates(self):
        assert unique([1, 2, 2, 3, 1, 4]) == [1, 2, 3, 4]

    def test_preserves_order(self):
        assert unique([3, 1, 2, 1, 3]) == [3, 1, 2]

    def test_with_key(self):
        assert unique(["a", "A", "b", "B"], key=str.lower) == ["a", "b"]

    def test_empty(self):
        assert unique([]) == []


class TestPairwise:
    def test_basic(self):
        assert pairwise([1, 2, 3, 4]) == [(1, 2), (2, 3), (3, 4)]

    def test_two_elements(self):
        assert pairwise([1, 2]) == [(1, 2)]

    def test_single_element(self):
        assert pairwise([1]) == []

    def test_empty(self):
        assert pairwise([]) == []


class TestRotate:
    def test_rotate_left(self):
        assert rotate([1, 2, 3, 4, 5], 2) == [3, 4, 5, 1, 2]

    def test_rotate_right(self):
        assert rotate([1, 2, 3, 4, 5], -2) == [4, 5, 1, 2, 3]

    def test_full_rotation(self):
        assert rotate([1, 2, 3], 3) == [1, 2, 3]

    def test_empty(self):
        assert rotate([], 5) == []


class TestPartition:
    def test_even_odd(self):
        matching, non = partition([1, 2, 3, 4, 5], lambda x: x % 2 == 0)
        assert matching == [2, 4]
        assert non == [1, 3, 5]

    def test_all_match(self):
        matching, non = partition([2, 4, 6], lambda x: x % 2 == 0)
        assert matching == [2, 4, 6]
        assert non == []

    def test_none_match(self):
        matching, non = partition([1, 3, 5], lambda x: x % 2 == 0)
        assert matching == []
        assert non == [1, 3, 5]


class TestInterleave:
    def test_basic(self):
        assert interleave([1, 2], ["a", "b"], [10, 20]) == [1, "a", 10, 2, "b", 20]

    def test_two_lists(self):
        assert interleave([1, 3], [2, 4]) == [1, 2, 3, 4]

    def test_different_lengths_stops_at_shortest(self):
        assert interleave([1, 2, 3], ["a", "b"]) == [1, "a", 2, "b"]


class TestSlidingWindow:
    def test_size_two(self):
        assert sliding_window([1, 2, 3, 4], 2) == [(1, 2), (2, 3), (3, 4)]

    def test_size_three(self):
        assert sliding_window([1, 2, 3, 4], 3) == [(1, 2, 3), (2, 3, 4)]

    def test_size_equals_length(self):
        assert sliding_window([1, 2, 3], 3) == [(1, 2, 3)]

    def test_size_exceeds_length(self):
        assert sliding_window([1, 2], 3) == []

    def test_invalid_size_raises(self):
        with pytest.raises(ValueError, match="size must be positive"):
            sliding_window([1, 2, 3], 0)
