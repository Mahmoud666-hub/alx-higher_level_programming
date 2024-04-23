#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    try:
        if range(my_list[:x]):
            m = 0
            for f in my_list[:x]:
                if type(f) == int:
                    print("{:d}".format(f), end="")
                    m += 1
            print()
            return m
    except TypeError:
        return m
