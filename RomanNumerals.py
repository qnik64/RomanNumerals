roman_to_arabic = {
    'I': 1,
    'IV': 4,
    'V': 5,
    'IX': 9,
    'X': 10,
    'XL': 40,
    'L': 50,
    'XC': 90,
    'C': 100,
    'CD': 400,
    'D': 500,
    'CM': 900,
    'M': 1000
}


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
    def find_max_roman_digit_smaller_than(num):
        for r, a in reversed(roman_to_arabic.items()):
            if a <= num:
                return r

    ret_val = []
    while number > 0:
        f = find_max_roman_digit_smaller_than(number)
        ret_val.append(f)
        number -= roman_to_arabic[f]
    return "".join(ret_val)
