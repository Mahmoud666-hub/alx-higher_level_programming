#!/usr/bin/python3
'''start'''


def roman_to_int(roman_string):
    '''start'''
    if roman_string is None or type(roman_string) != str:
        return 0
    h = {"M": 1000, "D": 500, "C": 100, "L": 50,
         "X": 10, "V": 5, "I": 1}
    n = 0
    z = 0
    while z < len(roman_string):
        if roman_string[z:(z+2)] == "IX":
            n += 9
            z += 2
        elif roman_string[z:(z+2)] == "IV":
            n += 4
            z += 2
        elif roman_string[z:(z + 1)] in h:
            n += h[roman_string[z:(z + 1)]]
            z += 1
    return n
