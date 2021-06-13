roman_to_arabic = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}

arabic_to_roman = {a: r for r, a in roman_to_arabic.items()}

def from_roman(number):
    converted = [roman_to_arabic[d] for d in number]
    ret_val = converted[-1]
    for current_digit, next_digit in zip(converted[:-1], converted[1:]):
        if current_digit < next_digit:
            ret_val -= current_digit
        else:
            ret_val += current_digit

    return ret_val


def to_roman(number):
    for i in range(1,4):
        try:
            return i * arabic_to_roman[number/i]
        except KeyError:
            pass

