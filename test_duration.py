import pytest
from duration import parse_duration, format_duration, DurationFormatError


@pytest.mark.parametrize("input_str, expected", [
    ("1h", 3600),
    ("30m", 1800),
    ("45s", 45),
    ("1h 30m", 5400),
    ("2h 15m 10s", 8110),
])
def test_parse_duration_valid(input_str, expected):
    assert parse_duration(input_str) == expected


@pytest.mark.parametrize("invalid_input", [
    "",
    "1x",
    "h",
    "10",
    "1h 2h",
    "1h xm",
])
def test_parse_duration_invalid(invalid_input):
    with pytest.raises(DurationFormatError):
        parse_duration(invalid_input)


@pytest.mark.parametrize("seconds, expected", [
    (0, "0s"),
    (3600, "1h"),
    (1800, "30m"),
    (45, "45s"),
    (5400, "1h 30m"),
    (8110, "2h 15m 10s"),
])
def test_format_duration_valid(seconds, expected):
    assert format_duration(seconds) == expected


@pytest.mark.parametrize("invalid_seconds", [-1, 1.5, "100"])
def test_format_duration_invalid(invalid_seconds):
    with pytest.raises(DurationFormatError):
        format_duration(invalid_seconds)


def test_round_trip():
    for seconds in [0, 45, 60, 3600, 3661, 86399]:
        assert parse_duration(format_duration(seconds)) == seconds
