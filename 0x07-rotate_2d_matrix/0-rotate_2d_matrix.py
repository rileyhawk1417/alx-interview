#!/usr/bin/python3

"""
Module rotates a 2d matrix
"""


def rotate_2d_matrix_copy(matrix):
    """
    Transpose a 2d matrix & swap values
    """
    swapped = zip(matrix)
    rotated_matrix = [list(row[::-1]) for row in swapped]
    return rotated_matrix


def rotate_2d_matrix(matrix):
    """
    Transpose the matrix values and print reverse
    """
    size = len(matrix)
    for idx in range(size):
        for inner_idx in range(idx, size):
            matrix[idx][inner_idx], matrix[inner_idx][idx] = \
                matrix[inner_idx][idx], matrix[idx][inner_idx]
    for row in matrix:
        row.reverse()
    return matrix
