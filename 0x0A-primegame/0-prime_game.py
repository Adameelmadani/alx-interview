#!/usr/bin/python3
"""
This is prime game module
"""





def isWinner(x, nums):
    """
    This function check for the winner in this prime game
    """
    maria = 0
    ben = 0
    for i in range(x):
        n = nums[i]
        p = check_prime(n)
        if p % 2 == 0:
            ben += 1
        else:
            maria += 1

    if maria > ben:
        return "Maria"
    elif ben > maria:
        return "Ben"
    else:
        return None
