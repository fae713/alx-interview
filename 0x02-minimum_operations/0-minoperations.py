#!/usr/bin/python3
"""
This module calculates the minimum number of operations
to reach nH characters.
"""


def minOperations(n):
    operations = 0

    # While n > 1, divide by 2 (equivalent to Copy)
    while n > 1:
        n //= 2
        operations += 1

    # If n is > 1 after dividing, add an operation(Paste)
    if n == 1:
        operations += 1

    return operations
