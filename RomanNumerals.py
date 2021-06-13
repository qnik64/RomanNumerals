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
    ret_val = 0
    for i in range(len(number)-1):
        if is_smaller(number[i], number[i+1]):
            ret_val -= roman_to_arabic[number[i]]
        else:
            ret_val += roman_to_arabic[number[i]]
    ret_val += roman_to_arabic[number[len(number)-1]]

    return ret_val
