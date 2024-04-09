#!/usr/bin/python3
def uppercase(str):
    for i in str:
        m = chr(ord(i) - 32)
        if i == ' ':
            m = i
        print(m, end="")
    print()
