#!/usr/bin/python3

"""
Module solving the NQueens problem in python
"""

import sys

moves = []
"""Possible list of moves to solve the problem"""

square_size = 0
"""Size of chessboard"""

piece_pos = None
"""Get the list of moves on the board"""


def get_board_size():
    """Get size of chessboard from user
    Returns:
        int: Size of chessboard
    """
    global square_size
    square_size = 0
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        square_size = int(sys.argv[1])
    except Exception:
        print("N must be a number")
        sys.exit(1)
    if square_size < 4:
        print("N must be at least 4")
        sys.exit(1)
    return square_size


def attack_mode(a, b):
    """Check if either queens positions are in attack mode
    Args:
        a (list or tuple): The first queens position
        b (list or tuple): The second queens position
    Returns:
        bool: True if either is in attack mode else False
    """
    if (a[0] == b[0]) or (a[1] == b[1]):
        return True
    return abs(a[0] - b[0]) == abs(a[1] - b[1])


def check_solution(solution):
    """Check if an existing solution is available
    Args:
        solution (List[int]): possible positions
    Returns:
        bool: True if present else False
    """
    global moves
    for move in moves:
        idx = 0
        for mv_pos in move:
            for sol_pos in solution:
                if mv_pos[0] == sol_pos[0] and mv_pos[1] == sol_pos[1]:
                    idx += 1
        if idx == square_size:
            return True
    return False


def build_move(pos, pos_list):
    """
    Build possible move list for n queens problem
    Args:
        pos (int): Get the current row position on the chessboard.
        pos_list (List[List[int]]): List of valid positions.

    """
    global moves
    global square_size
    if pos == square_size:
        tmp = pos_list.copy()
        if not check_solution(tmp):
            moves.append(tmp)
    else:
        for col in range(square_size):
            target = (pos * square_size) + col
            matched = zip(list([piece_pos[target]]) * len(pos_list), pos_list)
            used_pos = map(lambda x: attack_mode(x[0], x[1]), matched)
            pos_list.append(piece_pos[target].copy())
            if not any(used_pos):
                build_move(pos + 1, pos_list)
            pos_list.pop(len(pos_list) - 1)


def get_moves():
    """Get possible moves for given chessboard"""
    global piece_pos, square_size
    piece_pos = list(map(lambda x: [x // square_size, x % square_size],
                         range(square_size ** 2)))
    target = 0
    move_list = []
    build_move(target, move_list)


square_size = get_board_size()
get_moves()
for move in moves:
    print(move)
