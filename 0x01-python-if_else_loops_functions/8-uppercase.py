#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if ord(i) in range(97, 122):
            m = chr(ord(i) - 32)
        else:
            m = i
        print("{0}".format(m), end="")
    print()
