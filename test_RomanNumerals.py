import pytest

import RomanNumerals

testing_values = [
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
]


@pytest.mark.parametrize("comment, test_value, expected_value", testing_values)
def test_from_roman(comment, test_value, expected_value):
    assert RomanNumerals.from_roman(test_value) == expected_value


@pytest.mark.parametrize("comment, expected_value, test_value", testing_values[:10])
def test_to_roman(comment, test_value, expected_value):
    assert RomanNumerals.to_roman(test_value) == expected_value
