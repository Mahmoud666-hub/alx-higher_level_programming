#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    try:
        m = 0
        for f in range(x):
            if isinstance(my_list[f], int):
                print("{:d}".format(my_list[f]), end="")
                m += 1
        print()
        return m
    except TypeError:
        return m
