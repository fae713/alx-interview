#!/usr/bin/python3
"""
Lockboxes interview puzzle.
"""


def canUnlockAll(boxes):
    if not boxes:
        return True

    n = len(boxes)
    opened = [False] * n
    opened[0] = True
    stack = [0]

    while stack:
        current_box = stack.pop()
        for key in boxes[current_box]:
            if key < n and not opened[key]:
                opened[key] = True
                stack.append(key)

    return all(opened)
