#!/usr/bin/python3
""" function """


def print_matrix_integer(matrix=[[]]):
    """ handle empty parameter """
    if len(matrix) == 1:
        print("{}".format("\n"))
    else:
        for i in matrix:
            for m in i:
                if i.index(m) != len(i) - 1:
                    print("{}".format(m), end=" ")
            print("{}".format(m))
