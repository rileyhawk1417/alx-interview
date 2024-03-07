#!/usr/bin/python3

"""
Module showcases on how to 
solve island perimeter in python.
"""


def island_perimeter_edges_1(grid):
    """
    island_perimeter - returns the perimeter of an island
    @grid: 2D list of integers
    Return: the perimeter of the island
    """
    island = 0

    size = len(grid)
    for outer, row in enumerate(grid):
        m = len(row)
        for inner, cell in enumerate(row):
            if cell == 0:
                continue
            edges = (
                outer == 0 or (len(grid[outer-1]) >
                               inner and grid[outer-1][inner] == 0),
                inner == m - 1 or (m > inner + 1 and row[inner+1] == 0),
                outer == size -
                1 or (len(grid[outer+1]) >
                      inner and grid[outer+1][inner] == 0),
                inner == 0 or row[inner-1] == 0,
            )
            island += sum(edges)
    return island


def island_perimeter_edges_2(grid):
    perimeter = 0
    rows, cols = len(grid), len(grid[0])

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                perimeter += 4  # Each land cell adds 4 to the perimeter

                # Check neighboring cells
                if i > 0 and grid[i - 1][j] == 1:  # Up
                    perimeter -= 1
                if i < rows - 1 and grid[i + 1][j] == 1:  # Down
                    perimeter -= 1
                if j > 0 and grid[i][j - 1] == 1:  # Left
                    perimeter -= 1
                if j < cols - 1 and grid[i][j + 1] == 1:  # Right
                    perimeter -= 1

    return perimeter
