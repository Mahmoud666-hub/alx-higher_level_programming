#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new = a_dictionary.copy()
    for i in new:
        new[i] = (2 * new[i])
    return new
