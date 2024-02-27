#!/usr/bin/env python3
"""
Module to showcase minimum change problem.
"""


def makeChange(coins, total):
    """
    Find the minimum amount of coins for change.
    Args:
        coins: List[int] list of coin denominations.
        amount: [float] desired change
    Return:
        chnage: float
    """
    change = [float('inf')] * (total + 1)
    change[0] = 0
    for idx in range(1, total + 1):
        for coin in coins:
            if idx - coin >= 0:
                change[idx] = min(change[idx], change[idx - coin] + 1)
    if change[total] == float('inf'):
        return -1
    else:
        return change[total]
