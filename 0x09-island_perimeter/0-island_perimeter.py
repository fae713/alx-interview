#!/usr/bin/python3
"""
Island Perimeter.
"""


def island_perimeter(grid):
    """
    a function that returns the perimeter
    of the island described in grid.
    """
    if not grid:
        return 0

    rows = len(grid)
    cols = len(grid[0])
    perimeter = 0

    # Directions: left, right, up, down
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                for direction in directions:
                    ni, nj = i + direction[0], j + direction[1]
                    if (ni < 0 or ni >= rows or
                            nj < 0 or nj >= cols or
                            grid[ni][nj] == 0):
                        perimeter += 1
    return perimeter
