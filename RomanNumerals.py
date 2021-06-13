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
    if len(number) > 1 and number[0] == 'I' and number[1] != 'I':
        return roman_to_arabic[number[1]] - 1
    return sum(roman_to_arabic[digit] for digit in number)

