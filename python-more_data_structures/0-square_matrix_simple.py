#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    """
    Compute the square value of all integers in a matrix.

    Parameters:
    matrix (list of lists of int): A 2D list (matrix) of integers.

    Returns:
    list of lists of int: A new matrix with the square of each integer from the input matrix.
    """
    return [[x**2 for x in row] for row in matrix]
