#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    square_matrix = []
    for s in matrix:
        square_matrix.append(list(map(lambda s: s**2, s)))
    return square_matrix
