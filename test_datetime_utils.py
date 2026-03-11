from datetime import datetime

from datetime_utils import parse_iso, format_iso, start_of_day, end_of_day, is_weekend, add_business_days


def test_parse_iso():
    dt = parse_iso("2025-03-10T12:00:00")
    assert dt.year == 2025 and dt.month == 3 and dt.day == 10


def test_format_iso():
    dt = datetime(2025, 3, 10, 12, 0, 0)
    assert "2025" in format_iso(dt)


def test_start_of_day():
    dt = datetime(2025, 3, 10, 14, 30, 0)
    assert start_of_day(dt) == datetime(2025, 3, 10, 0, 0, 0)


def test_end_of_day():
    dt = datetime(2025, 3, 10, 14, 30, 0)
    assert end_of_day(dt).hour == 23


def test_is_weekend():
    sat = datetime(2025, 3, 8)  # Saturday
    mon = datetime(2025, 3, 10)  # Monday
    assert is_weekend(sat)
    assert not is_weekend(mon)


def test_add_business_days():
    fri = datetime(2025, 3, 7)
    next_mon = add_business_days(fri, 1)
    assert next_mon.day == 10
