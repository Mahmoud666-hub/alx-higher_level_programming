#!/usr/bin/python3
for n in range(0, 10):
    for i in range((n + 1), 10):
        if n != i and not (n == 8 and i == 9):
            print("{}{}, ".format(n, i), end="")
print("{}{}".format(n - 1, i))
