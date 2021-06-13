roman_to_arabic = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}


def is_smaller(d1, d2):
    return roman_to_arabic[d1] - roman_to_arabic[d2] < 0


def from_roman(number):
    if len(number) > 1 and is_smaller(number[0], number[1]):
        return roman_to_arabic[number[1]] - roman_to_arabic[number[0]]
    return sum(roman_to_arabic[digit] for digit in number)
