#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if idx < 0 or idx > (len(my_list) - 1):
        return my_list
    i = 0
    while i < idx:
        i += 1
    if i == idx:
        my_list[i] = element
        return my_list
