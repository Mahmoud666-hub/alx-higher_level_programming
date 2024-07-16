#!/usr/bin/python3
"""module"""


def pascal_triangle(n):
    if n <= 0:
        return []
    r = []
    x = []
    t = 1
    while t <= n:
        q = 1
        r = []
        while q <= t:
            if q == t or q == 1:
                r.append(1)
            else:
                z = 0
                z = ((x[len(x) - 1][len(r) - 2]) + (x[len(x) - 1][len(r) - 1]))
                r.append(q)
                # print(q, "q")
                # print(len(x), "len x")
                # print(len(r), "len r")
                # print(x[len(x) - 1])
                # print(x[len(x) - 1][len(r) - 2])
                # print(x[len(x) - 1][len(r) - 1])
                z = ((x[len(x) - 1][len(r) - 2]) + (x[len(x) - 1][len(r) - 1]))
                r[len(r) - 1] = z
                # print(z, "z")
            q += 1
        x.append(r)
        t += 1

    return x
