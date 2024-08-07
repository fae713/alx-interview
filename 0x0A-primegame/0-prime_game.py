#!/usr/bin/python3
"""
ALX interview prime game task.
"""


def isWinner(x, nums):
    """
    Determines the winner of a game.

    Params:
        x (int): The number of game rounds played.
        nums (list): An array holding winners of each rounds.

    Returns:
        str: Name of the player that won the most rounds.
    """
    def SieveOfEratosthenes(n):
        """
        Sieve of Eratosthenes algorithm
        to find all prime numbers up to n.
        """
        prime_num = [True] * (n + 1)
        prime_num[0] = prime_num[1] = False
        p = 2
        while p * p <= n:
            if prime_num[p]:
                for i in range(p * p, n + 1, p):
                    prime_num[i] = False
            p += 1
        return prime_num

    def get_prime_list(n, prime_num):
        """
        Returns a list of primes up to n.
        """
        return [i for i in range(2, n + 1) if prime_num[i]]

    max_num = max(nums)
    prime_num = SieveOfEratosthenes(max_num)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        primes = get_prime_list(n, prime_num)
        moves = 0
        while primes:
            prime_in_game = primes.pop(0)
            moves += 1
            primes = [p for p in primes if p % prime_in_game != 0]

        if moves % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
