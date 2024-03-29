#!/usr/bin/python3
"""
matrix module
"""


def matrix_divided(matrix, div):
    """ matrix division function """
    for row in matrix:
        for value in row:
            if type(value) not in [float, int]:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    first_row_size = len(matrix[0])
    for row in matrix:
        if len(row) != first_row_size:
            raise TypeError("Each row of the matrix must have the same size")

    if type(div) not in [float, int]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[float(f"{value/div: .2f}") for value in row] for row in matrix]
