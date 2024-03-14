#!/usr/bin/python3
"""
This is prime game module
"""

def SieveOfEratosthenes(n):
    prime = [True for i in range(n+1)]
    p = 2
    while (p * p <= n):
 
        # If prime[p] is not
        # changed, then it is a prime
        if (prime[p] == True):
 
            # Update all multiples of p
            for i in range(p * p, n+1, p):
                prime[i] = False
        p += 1
 
    # Print all prime numbers
    for p in range(2, n+1):
        if prime[p]:
            print(p)


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
