#!/usr/bin/python3
"""
0x04. UTF-8 Validation” project.
"""


def validUTF8(data):
    """
    A method that determines if a given data set represents
    a valid UTF-8 encoding.

    Args:
        Data(list of INT) = A set can contain multiple characters.
        The data will be represented by a list of integers.
        Each integer represents 1 byte of data.

    Return:
        bool:
        True -> if data is a valid UTF-8 encoding,
        False -> if data isn't a valid UTF-8 encoding.
    """
    char = 0

    for byte in data:
        byte = byte & 0xFF
        if char == 0:
            if (byte >> 5) == 0b110:
                char = 1
            elif (byte >> 4) == 0b1110:
                char = 2
            elif (byte >> 3) == 0b11110:
                char = 3
            elif (byte >> 7) != 0:
                return False
        else:
            if (byte >> 6) != 0b10:
                return False
            char = 1

    return char == 0
