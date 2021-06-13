import pytest

import RomanNumerals


@pytest.mark.parametrize("test_value, expected_value", [
    ('I', 1),
    ('V', 5),
    ('X', 10)
])
def test_from_roman(test_value, expected_value):
    assert RomanNumerals.from_roman(test_value) == expected_value
