#!/usr/bin/python3
def uniq_add(my_list=[]):
    a = set(my_list)
    x = 0
    for i in a:
        x += i
    return x
