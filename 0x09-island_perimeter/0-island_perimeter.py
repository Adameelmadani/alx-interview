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
    for i in range(h):
        for j in range(w):
            up = 1
            down = 1
            left = 1
            right = 1
            if grid[i][j] == 0:
                continue
            if i != 0:
                if grid[i - 1][j] == 1:
                    up = 0
            if i != h - 1:
                if grid[i + 1][j] == 1:
                    down = 0
            if j != 0:
                if grid[i][j - 1] == 1:
                    left = 0
            if j != w - 1:
                if grid[i][j + 1] == 1:
                    right = 0
            p += up + down + left + right
    return p
