#!/usr/bin/python3
from types import NoneType


def roman_to_int(roman_string):
    roman_numeral = {'I': 1, 'V': 5, 'X': 10,
                     'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    sum = 0
    if type(roman_string) != str or type(roman_string) is NoneType:
        return 0
    for roman in roman_string:
        sum += roman_numeral[roman]
    return sum
