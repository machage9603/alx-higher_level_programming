#!/usr/bin/python3


def roman_to_int(roman_string):
    if not roman_string or not isinstance(roman_string, str):
        return 0

    rom_n = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    last_rom = 0
    total = 0

    for ch in reversed(roman_string):
        if ch not in rom_n:
            return 0  # Invalid Roman numeral

        current_value = rom_n[ch]

        if current_value < last_rom:
            total -= current_value
        else:
            total += current_value

        last_rom = current_value

    return total
