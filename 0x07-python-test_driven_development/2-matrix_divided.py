#!/usr/bin/python3
'''matrix divided'''


def matrix_divided(matrix, div):
    '''matrix division'''
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    q = []
    h = []
    b = len(matrix[0])
    for v in matrix:
        for i in v:
            if not isinstance(i, int) and not isinstance(i, float):
                raise TypeError("matrix must be a matrix (list of lists) of \
integers/floats")
            else:
                q.append(round((i / div), 2))
        h.append(q)
        if not b == len(q):
            raise TypeError("Each row of the matrix must have the same size")
        q = []
    return h


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/2-matrix_divided.txt")
