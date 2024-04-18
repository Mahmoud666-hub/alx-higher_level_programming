#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == []:
        return None
    i = 0
    e = my_list[0]
    while i < len(my_list) - 1:
        if e < my_list[i]:
            e = my_list[i]
        i += 1
    return e
