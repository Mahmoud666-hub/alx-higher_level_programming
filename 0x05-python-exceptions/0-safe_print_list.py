#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        for f in range(my_list[x - 1]):
            print("{:d}".format(my_list[f]), end="")
        print()
        return x
    except:
        m = 0
        for f in my_list:
            print("{:d}".format(f), end="")
            m += 1
        print()
        return m
