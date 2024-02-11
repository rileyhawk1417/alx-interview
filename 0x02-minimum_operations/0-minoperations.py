#!/usr/bin/python3

"""
Get the most amount of work done,
with little effort.
"""


def minOperations(n):
    """
    Calculate the least number of ops
    to get the result
    """
    if not isinstance(n, int):
        return 0
    op_count = 0
    tmp = 0
    complete = 1
    while complete < n:
        if tmp == 0:
            tmp = complete
            complete += tmp
            op_count += 2
        elif n - complete > 0 and (n - complete) % complete == 0:
            tmp = complete
            complete += tmp
            op_count += 2
        elif tmp > 0:
            complete += tmp
            op_count += 1
    return op_count
