#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    n_matrix = []

    for numbers in matrix:
        n_matrix.append(list(map(lambda x: x**2, numbers)))
    return n_matrix
