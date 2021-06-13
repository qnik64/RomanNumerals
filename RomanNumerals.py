roman_to_arabic = {
    'I': 1,
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}


def from_roman(number):
    return sum(roman_to_arabic[digit] for digit in number)

