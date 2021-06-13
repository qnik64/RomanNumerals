import pytest

import RomanNumerals


@pytest.mark.parametrize("comment, test_value, expected_value", [
    ("one digit", 'I', 1),
    ("one digit", 'V', 5),
    ("one digit", 'X', 10),
    ("one digit", 'L', 50),
    ("one digit", 'C', 100),
    ("one digit", 'D', 500),
    ("one digit", 'M', 1000),

    ("two digits", 'II', 2),
    ("two digits", 'XX', 20),
    ("three digits", 'XXX', 30),
    ("mixed two digits", 'XI', 11),
    ("mixed two digits", 'MMXXI', 2021),

    ("ascending order", 'IV', 4),
    ("ascending order", 'IX', 9),
    ("ascending order", 'CD', 400),
    ("mixed order", 'CXL', 140),
    ("mixed order", 'XLI', 41),

    ("combo", 'MMCMLXXXIV', 2984)

])
def test_from_roman(comment, test_value, expected_value):
    assert RomanNumerals.from_roman(test_value) == expected_value
