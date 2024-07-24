#!/usr/bin/python3
"""
Change comes from within.
"""


def makeChange(coins, total):
    """
    Determines the fewest number of coins needed to meet a given
    amount total when given a pile of coins of different values.
    """
    if total <= 0:
        return 0

    # Initialize remaining amount and coin count
    rem = total
    coins_count = 0
    coin_idx = 0

    # Sort coins in descending order
    sorted_coins = sorted(coins, reverse=True)
    n = len(sorted_coins)

    while rem > 0:
        if coin_idx >= n:
            return -1
        if rem - sorted_coins[coin_idx] >= 0:
            rem -= sorted_coins[coin_idx]
            coins_count += 1
        else:
            coin_idx += 1

    return coins_count
