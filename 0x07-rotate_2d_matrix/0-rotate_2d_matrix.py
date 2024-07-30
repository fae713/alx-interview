#!/usr/bin/python3
"""
2D Matrix module
"""
from typing import List, Any


def rotate_2d_matrix(matrix: List[List[Any]]) -> None:
    """
    A function that rotates an n x n 2D matrix
    90 degrees clockwise.
    """
    if not isinstance(matrix, list) or len(matrix) == 0:
        return

    if not all(isinstance(row, list) for row in matrix):
        return

    rows = len(matrix)
    cols = len(matrix[0])

    if not all(len(row) == cols for row in matrix):
        return

    rotated = [[] for _ in range(cols)]

    for r in range(rows):
        for c in range(cols):
            rotated[c].insert(0, matrix[r][c])

    matrix[:] = rotated
