import pytest
from roman import to_roman, from_roman, RomanNumeralError


@pytest.mark.parametrize("number, roman", [
    (1, "I"),
    (4, "IV"),
    (9, "IX"),
    (58, "LVIII"),
    (1994, "MCMXCIV"),
    (3999, "MMMCMXCIX"),
])
def test_to_roman_valid(number, roman):
    assert to_roman(number) == roman


@pytest.mark.parametrize("number", [0, -1, 4000])
def test_to_roman_invalid(number):
    with pytest.raises(RomanNumeralError):
        to_roman(number)


@pytest.mark.parametrize("roman, number", [
    ("I", 1),
    ("IV", 4),
    ("IX", 9),
    ("LVIII", 58),
    ("MCMXCIV", 1994),
])
def test_from_roman_valid(roman, number):
    assert from_roman(roman) == number


@pytest.mark.parametrize("roman", ["", "IIII", "VX", "ABC"])
def test_from_roman_invalid(roman):
    with pytest.raises(RomanNumeralError):
        from_roman(roman)


def test_round_trip():
    for i in range(1, 1000):
        assert from_roman(to_roman(i)) == i
