#!/usr/bin/python3
"""
This module calculates the minimum number of operations
to reach nH characters.
"""


def minOperations(n):
    operations = 0
    while n > 1:
        n //= 2
        operations += 1
    operations += 1  # Account for the final Paste operation
    return operations
