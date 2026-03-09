import pytest
from number_utils import clamp, sign, is_even, is_odd, digits


class TestClamp:
    def test_within_range(self):
        assert clamp(5, 0, 10) == 5
        assert clamp(0, -5, 5) == 0

    def test_below_low(self):
        assert clamp(-5, 0, 10) == 0
        assert clamp(-100, -10, 10) == -10

    def test_above_high(self):
        assert clamp(15, 0, 10) == 10
        assert clamp(100, -10, 10) == 10

    def test_at_boundaries(self):
        assert clamp(0, 0, 10) == 0
        assert clamp(10, 0, 10) == 10

    def test_floats(self):
        assert clamp(2.5, 0, 5) == 2.5
        assert clamp(-1.5, 0, 5) == 0
        assert clamp(6.5, 0, 5) == 5

    def test_invalid_range_raises(self):
        with pytest.raises(ValueError, match="low must be less than or equal to high"):
            clamp(5, 10, 0)
        with pytest.raises(ValueError, match="low must be less than or equal to high"):
            clamp(0, 1, -1)


class TestSign:
    def test_positive(self):
        assert sign(1) == 1
        assert sign(100) == 1
        assert sign(0.001) == 1

    def test_zero(self):
        assert sign(0) == 0

    def test_negative(self):
        assert sign(-1) == -1
        assert sign(-100) == -1
        assert sign(-0.001) == -1


class TestIsEven:
    def test_even_numbers(self):
        assert is_even(0)
        assert is_even(2)
        assert is_even(4)
        assert is_even(-2)
        assert is_even(-100)

    def test_odd_numbers(self):
        assert not is_even(1)
        assert not is_even(3)
        assert not is_even(-1)
        assert not is_even(-7)


class TestIsOdd:
    def test_odd_numbers(self):
        assert is_odd(1)
        assert is_odd(3)
        assert is_odd(7)
        assert is_odd(-1)
        assert is_odd(-5)

    def test_even_numbers(self):
        assert not is_odd(0)
        assert not is_odd(2)
        assert not is_odd(-2)


class TestDigits:
    def test_positive_numbers(self):
        assert digits(0) == [0]
        assert digits(1) == [1]
        assert digits(12345) == [1, 2, 3, 4, 5]
        assert digits(9) == [9]

    def test_negative_numbers(self):
        assert digits(-12345) == [1, 2, 3, 4, 5]
        assert digits(-1) == [1]

    def test_large_numbers(self):
        assert digits(123456789) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
