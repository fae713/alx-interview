#!/usr/bin/python3
"""
Pascal's Triangle.
"""


def pascal_triangle(n):
    """
    A funtion that creates Pascal's Triangle up to n levels.

    Args:
        n (int): The levels to generate in the triangle.

    Returns:
        list: A list of lists representing Pascal's Triangle levels.

    Raises:
        ValueError: If n is less than or equal to zero.
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        row = [1]

        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])

        row.append(1)

        triangle.append(row)

    return triangle
