"""Tests for iterator and sequence helpers."""

import pytest

from utils.iter_utils import (
    batched,
    chunk,
    concat,
    cons,
    drop,
    drop_while,
    duplicates,
    duplicates_all,
    enumerate_from,
    first,
    flatten,
    flatten_depth,
    group_consecutive,
    interleave,
    last,
    nth,
    pad_none,
    pairwise,
    partition,
    run_length_encode,
    scan,
    sliding_window,
    spy,
    take,
    take_while,
    unique_ordered,
)


def test_chunk_basic_and_tail():
    assert list(chunk(range(5), 2)) == [[0, 1], [2, 3], [4]]
    assert list(chunk([1], 3)) == [[1]]
    assert list(chunk([], 2)) == []


def test_chunk_size_invalid():
    with pytest.raises(ValueError):
        list(chunk([1, 2], 0))


def test_batched_strict():
    assert list(batched(range(4), 2)) == [(0, 1), (2, 3)]
    assert list(batched(range(5), 2)) == [(0, 1), (2, 3)]
    assert list(batched([], 3)) == []


def test_batched_invalid():
    with pytest.raises(ValueError):
        list(batched([1], 0))


def test_flatten():
    assert list(flatten([[1, 2], [3], []])) == [1, 2, 3]


def test_flatten_depth_strings_atomic():
    nested = ["ab", ["cd", "ef"]]
    assert list(flatten_depth(nested, depth=2)) == ["ab", "cd", "ef"]


def test_flatten_depth_zero():
    assert list(flatten_depth([1, [2, 3]], depth=0)) == [1, [2, 3]]


def test_flatten_depth_non_iterable_leaf():
    assert list(flatten_depth([1, None, 3], depth=2)) == [1, None, 3]


def test_flatten_depth_negative():
    with pytest.raises(ValueError):
        list(flatten_depth([1], depth=-1))


def test_unique_ordered():
    assert list(unique_ordered([3, 1, 3, 2, 1])) == [3, 1, 2]


def test_pairwise():
    assert list(pairwise([1, 2, 3])) == [(1, 2), (2, 3)]
    assert list(pairwise([])) == []


def test_sliding_window():
    assert list(sliding_window([1, 2, 3, 4], 2)) == [(1, 2), (2, 3), (3, 4)]
    assert list(sliding_window([1], 2)) == []


def test_sliding_window_invalid():
    with pytest.raises(ValueError):
        list(sliding_window([1, 2], 0))


def test_partition():
    yes, no = partition(lambda x: x % 2 == 0, range(6))
    assert yes == [0, 2, 4]
    assert no == [1, 3, 5]


def test_take():
    assert take(3, range(10)) == [0, 1, 2]
    assert take(5, [1, 2]) == [1, 2]


def test_take_negative():
    with pytest.raises(ValueError):
        take(-1, [])


def test_drop():
    assert list(drop(2, range(5))) == [2, 3, 4]
    assert list(drop(10, [1])) == []


def test_drop_negative():
    with pytest.raises(ValueError):
        list(drop(-1, []))


def test_take_while():
    assert list(take_while(lambda x: x < 3, [1, 2, 3, 1])) == [1, 2]


def test_drop_while():
    assert list(drop_while(lambda x: x < 3, [1, 2, 3, 1, 0])) == [3, 1, 0]


def test_interleave_two():
    assert list(interleave([1, 2, 3], [10, 20])) == [1, 10, 2, 20, 3]


def test_interleave_empty():
    assert list(interleave([], [1, 2])) == [1, 2]


def test_nth():
    assert nth(range(5), 2) == 2
    assert nth(range(2), 5, default=-1) == -1


def test_nth_negative_index():
    with pytest.raises(ValueError):
        nth([], -1)


def test_first_last():
    assert first([7, 8]) == 7
    assert first([], default=0) == 0
    assert last([7, 8]) == 8
    assert last([], default="x") == "x"


def test_group_consecutive():
    assert list(group_consecutive([1, 1, 2, 2, 2, 1])) == [
        (1, [1, 1]),
        (2, [2, 2, 2]),
        (1, [1]),
    ]


def test_group_consecutive_key():
    items = ["aa", "b", "cc", "d"]
    assert list(group_consecutive(items, key=len)) == [
        (2, ["aa"]),
        (1, ["b"]),
        (2, ["cc"]),
        (1, ["d"]),
    ]


def test_run_length_encode():
    assert list(run_length_encode("aaabbc")) == [("a", 3), ("b", 2), ("c", 1)]


def test_duplicates_stream():
    assert list(duplicates([1, 2, 1, 3, 2, 2])) == [1, 2, 2]


def test_duplicates_all():
    assert duplicates_all([1, 2, 1, 3, 2]) == {1, 2}


def test_scan():
    assert list(scan(lambda a, b: a + b, [1, 2, 3], 0)) == [0, 1, 3, 6]


def test_enumerate_from():
    assert list(enumerate_from("ab", start=5)) == [(5, "a"), (6, "b")]


def test_pad_none_finite_prefix():
    from itertools import takewhile

    out = list(takewhile(lambda x: x is not None, pad_none([1, 2])))
    assert out == [1, 2]


def test_spy_replays_head():
    head, rest = spy([10, 20, 30], n=2)
    assert head == (10, 20)
    assert list(rest) == [10, 20, 30]


def test_spy_short_iterable():
    head, rest = spy([1], n=5)
    assert head == (1,)
    assert list(rest) == [1]


def test_spy_negative():
    with pytest.raises(ValueError):
        spy([], n=-1)


def test_cons():
    assert list(cons(0, [1, 2])) == [0, 1, 2]


def test_concat():
    assert list(concat([1, 2], [], [3])) == [1, 2, 3]


@pytest.mark.parametrize(
    "size, expected_rows",
    [
        (1, [[0], [1], [2]]),
        (3, [[0, 1, 2]]),
    ],
)
def test_chunk_parametrized(size, expected_rows):
    assert list(chunk(range(3), size)) == expected_rows


@pytest.mark.parametrize(
    "depth, expected",
    [
        (1, [1, 2, 3]),
        (2, [1, 2, 3]),
    ],
)
def test_flatten_depth_list(depth, expected):
    assert list(flatten_depth([[1], [2], [3]], depth=depth)) == expected


def test_partition_all_true():
    yes, no = partition(lambda _: True, [1, 2])
    assert yes == [1, 2] and no == []


def test_partition_all_false():
    yes, no = partition(lambda _: False, [1, 2])
    assert yes == [] and no == [1, 2]


def test_unique_ordered_empty():
    assert list(unique_ordered([])) == []


def test_pairwise_single():
    assert list(pairwise([1])) == []


def test_interleave_three_streams():
    assert list(interleave([1], [2], [3])) == [1, 2, 3]


def test_drop_while_all_match():
    assert list(drop_while(lambda x: x < 10, [1, 2, 3])) == []


def test_take_while_empty():
    assert list(take_while(lambda _: True, [])) == []


def test_run_length_encode_single():
    assert list(run_length_encode([42])) == [(42, 1)]


def test_group_consecutive_empty():
    assert list(group_consecutive([])) == []


def test_scan_empty():
    assert list(scan(lambda a, b: a + b, [], 100)) == [100]


def test_last_single():
    assert last([99]) == 99


def test_first_single():
    assert first([99]) == 99


def test_nth_first():
    assert nth("abc", 0) == "a"


def test_batched_single_full():
    assert list(batched([7, 8], 2)) == [(7, 8)]


def test_batched_insufficient_for_one_batch():
    assert list(batched([7], 2)) == []


def test_flatten_empty_inners():
    assert list(flatten([[], [1], []])) == [1]


def test_duplicates_no_dupes():
    assert list(duplicates([1, 2, 3])) == []


def test_duplicates_all_none():
    assert duplicates_all([1, 2, 3]) == set()


def test_enumerate_from_default_start():
    assert list(enumerate_from(["x"])) == [(0, "x")]


def test_chunk_single_element_chunks():
    assert list(chunk("abc", 1)) == [["a"], ["b"], ["c"]]


def test_sliding_window_full_length():
    assert list(sliding_window([1, 2, 3], 3)) == [(1, 2, 3)]


def test_drop_zero_is_identity():
    assert list(drop(0, [1, 2])) == [1, 2]


def test_take_zero():
    assert take(0, [1, 2, 3]) == []


def test_concat_no_args():
    assert list(concat()) == []


def test_interleave_all_empty():
    assert list(interleave([], [])) == []


def test_flatten_depth_mixed_with_string():
    assert list(flatten_depth(["hi", ["yo"]], depth=2)) == ["hi", "yo"]


def test_scan_mul():
    assert list(scan(lambda a, b: a * b, [2, 3, 4], 1)) == [1, 2, 6, 24]


def test_partition_types():
    yes, no = partition(str.isupper, ["a", "B", "c", "D"])
    assert yes == ["B", "D"]
    assert no == ["a", "c"]


def test_run_length_encode_empty():
    assert list(run_length_encode([])) == []


def test_unique_ordered_one():
    assert list(unique_ordered([5])) == [5]


def test_pairwise_long():
    xs = list(range(100))
    pairs = list(pairwise(xs))
    assert len(pairs) == 99
    assert pairs[0] == (0, 1)
    assert pairs[-1] == (98, 99)


def test_chunk_large_range():
    rows = list(chunk(range(1000), 100))
    assert len(rows) == 10
    assert rows[0][0] == 0
    assert rows[-1][-1] == 999


def test_sliding_window_runs():
    wins = list(sliding_window(range(50), 10))
    assert len(wins) == 41
    assert wins[0] == tuple(range(10))


def test_interleave_uneven_stress():
    a = list(range(0, 30, 3))
    b = list(range(1, 40, 2))
    out = list(interleave(a, b))
    assert out[0] == 0
    assert len(out) == len(a) + len(b)


def test_duplicates_all_many():
    xs = list(range(20)) + list(range(10, 15))
    dups = duplicates_all(xs)
    assert 10 in dups and 11 in dups and 0 not in dups


def test_group_consecutive_long_run():
    xs = [1] * 50 + [2] * 30
    groups = list(group_consecutive(xs))
    assert groups[0] == (1, [1] * 50)
    assert groups[1] == (2, [2] * 30)


def test_scan_string_lengths():
    lengths = list(scan(lambda acc, s: acc + len(s), ["aa", "bbb", ""], 0))
    assert lengths == [0, 2, 5, 5]


def test_nested_flatten_depth_three():
    nested = [[[1]], [[2, 3]]]
    flat = list(flatten_depth(nested, depth=3))
    assert flat == [1, 2, 3]


def test_partition_preserves_relative_order():
    items = list(range(50))
    evens, odds = partition(lambda x: x % 2 == 0, items)
    assert evens == list(range(0, 50, 2))
    assert odds == list(range(1, 50, 2))


def test_take_while_stops_at_boundary():
    data = [2, 4, 6, 5, 8]
    assert list(take_while(lambda x: x % 2 == 0, data)) == [2, 4, 6]


def test_drop_while_then_take():
    data = [0, 0, 1, 2, 3]
    trimmed = list(take(3, drop_while(lambda x: x == 0, data)))
    assert trimmed == [1, 2, 3]


def test_cons_concat_chain():
    assert list(concat(cons(1, [2]), [3])) == [1, 2, 3]


def test_spy_zero_head():
    head, rest = spy([1, 2], n=0)
    assert head == ()
    assert list(rest) == [1, 2]
