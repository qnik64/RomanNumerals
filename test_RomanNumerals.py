import pytest

import RomanNumerals


@pytest.mark.parametrize("test_value, expected_value", [
    ('I', 1),
    ('V', 5),
    ('X', 10),
    ('L', 50),
    ('C', 100),
    ('D', 500),
    ('M', 1000)
])
def test_from_roman(test_value, expected_value):
    assert RomanNumerals.from_roman(test_value) == expected_value
