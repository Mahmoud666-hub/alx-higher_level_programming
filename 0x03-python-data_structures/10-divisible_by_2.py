#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    nlist = []
    i = 0
    while i < len(my_list):
        if my_list[i] % 2 == 0:
            nlist.append(True)
        else:
            nlist.append(False)
        i += 1
    return nlist
