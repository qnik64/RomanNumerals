import RomanNumerals


def test_RomanNumerals_can_convert_I():
    assert RomanNumerals.from_roman('I') == 1


def test_RomanNumerals_can_convert_V():
    assert RomanNumerals.from_roman('V') == 5
