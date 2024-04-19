#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    mat = []
    for i in matrix:
        m = list(map(lambda x: x ** 2, i))
        mat.append(m)
    return mat
