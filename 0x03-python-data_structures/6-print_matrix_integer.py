#!/usr/bin/python3
""" function """


def print_matrix_integer(matrix=[[]]):
    """ handle empty parameter """
    for i in matrix:
        for m in i:
            if i.index(m) != len(i) - 1:
                print("{:d}".format(m), end=" ")
        print("{:d}".format(m), end ="")
        print()
