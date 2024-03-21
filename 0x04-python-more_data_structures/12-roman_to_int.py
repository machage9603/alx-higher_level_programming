#!/usr/bin/python3 


def roman_to_int(roman_string):
    if not  roman_string:
        return 0

    if not isinstance(roman_string, str):
        return 0

    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    return sum(roman_dict[c] * (1 if roman_dict[c] >= roman_dict.get(roman_string[i + 1], 0) else -1) for i, c in enumerate(roman_string))


