#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    """
    Print a matrix of integers.

    Parameters:
    matrix (list of lists of int): The matrix to print,
    where each sublist represents a row.

    Returns:
    None
    """
    for row in matrix:
        print(" ".join("{:d}".format(element) for element in row))
