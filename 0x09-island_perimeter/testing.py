#!/usr/bin/python3
"""
This is our python module
"""


def island_perimeter(grid):
    """
    This is island_perimeter function
    """
    if grid is None:
        return 0
    h = len(grid)
    if h == 0:
        return 0
    w = len(grid[0])
    if w == 0:
        return 0

    p = 0
    i = 0
    j = 0
    for i in range(h):
        for j in range(w):
            if grid[i][j] == 1:
                break;
        if grid[i][j] == 1:
            break;
    up = 1
    left = 1
    down = 0
    right = 0
    p += up + left + down + right
