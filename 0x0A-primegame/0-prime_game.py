#!/usr/bin/env python3

"""
Prime Game module
"""


def sieve_of_eratosthenes(n):
    """optimized prime number algo for big O.
        Algorithm used to generate all prime
        numbers up to a given limit `n`.
    Args:
        `n` (int): Generate prime numbers based on limit of `n`

    Returns:
        list [int]: return list of prime numbers
    """
    prime = [True] * (n + 1)
    prime[0], prime[1] = False, False
    p = 2
    while p * p <= n:
        if prime[p]:
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1
    return [i for i in range(n + 1) if prime[i]]


def isWinner(x, nums):
    """Checks if user is the winner

    Args:
        x (int): number of rounds played.
        nums (list[int]): list of numbers to validate winner.

    Returns:
        string: name of winner
    """
    def count_primes(n):
        """Simply count prime numbers for each game

        Args:
            n (int): prime number to check against.

        Returns:
            int: prime number count
        """
        primes = sieve_of_eratosthenes(n)
        return len(primes)

    maria_wins = 0
    ben_wins = 0

    for _ in range(x):
        for n in nums:
            prime_count = count_primes(n)
            # If the count of primes is odd, Maria wins since she starts first.
            if prime_count % 2 != 0:
                maria_wins += 1
            else:
                ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
