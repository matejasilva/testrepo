class RomanNumeralError(ValueError):
    pass


_ROMAN_MAP = [
    (1000, "M"),
    (900, "CM"),
    (500, "D"),
    (400, "CD"),
    (100, "C"),
    (90, "XC"),
    (50, "L"),
    (40, "XL"),
    (10, "X"),
    (9, "IX"),
    (5, "V"),
    (4, "IV"),
    (1, "I"),
]


def to_roman(n: int) -> str:
    """
    Convert integer to Roman numeral.
    Supports 1–3999.
    """
    if not 1 <= n <= 3999:
        raise RomanNumeralError("Number must be between 1 and 3999")

    result = ""
    for value, symbol in _ROMAN_MAP:
        while n >= value:
            result += symbol
            n -= value
    return result


def from_roman(s: str) -> int:
    """
    Convert Roman numeral to integer.
    """
    if not s or not isinstance(s, str):
        raise RomanNumeralError("Invalid Roman numeral")

    s = s.upper()
    index = 0
    result = 0

    for value, symbol in _ROMAN_MAP:
        while s[index:index + len(symbol)] == symbol:
            result += value
            index += len(symbol)
            if index >= len(s):
                break

    # Validate round-trip correctness
    if to_roman(result) != s:
        raise RomanNumeralError("Invalid Roman numeral format")

    return result
