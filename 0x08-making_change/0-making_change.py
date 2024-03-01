#!/usr/bin/python3
"""This is our python module"""


def makeChange(coins, total):
    """makechange function for algo"""
    if total <= 0:
        return 0
    listed_coins = sorted(coins)
    n = len(listed_coins)
    if n == 0:
        return -1
    number = 0
    for i in range(n - 1, -1, -1):
        if total == 0:
            break
        if total < listed_coins[i]:
            continue
        number += int(total / listed_coins[i])
        total = total % listed_coins[i]
    if total == 0:
        return number
    return -1
