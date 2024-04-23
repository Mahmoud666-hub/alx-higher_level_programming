#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        if range(my_list[x]):
            for f in my_list[:2]:
                print("{:d}".format(f), end="")
            print()
            # print("1")
            return x
    except IndexError:
        m = 0
        for f in my_list:
            print("{:d}".format(f), end="")
            m += 1
        print()
        # print("2")
        return m
