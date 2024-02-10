#!/usr/bin/python3
"""
Pascal Triangle
variable `ix` is for ID
variable `ixin` is for the inner ID
"""


def pascal_triangle(n):
    """Pascal triangle function"""
    triangle = []

    if (n <= 0):
        return triangle

    for ix in range(n):
        row = []
        for ixin in range(ix+1):
            if ixin == 0 or ixin == ix:
                row.append(1)
            else:
                row.append(triangle[ix - 1][ixin - 1] + triangle[ix - 1][ixin])
        triangle.append(row)

    return triangle
