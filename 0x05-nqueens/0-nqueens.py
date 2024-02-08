#!/usr/bin/python3
"""
The N queens puzzle is the challenge of placing N non-attacking queens
on an NxN chessboard. Write a program that solves the N queens problem.
"""

import sys


def queen_down(N, i, queens, final_combo, col, pos, neg):
    """recursive function to put down non attacking queens"""
    if len(queens) == N:
        final_combo.append(queens)
        return final_combo
    for j in range(N):
        if not (j in col or i + j in pos or i - j in neg):
            queen_down(N, i + 1, queens + [[i, j]], final_combo,
                       col + [j], pos + [i + j], neg + [i - j])
    return final_combo


if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

try:
    N = int(sys.argv[1])
except ValueError:
    print("N must be a number")
    sys.exit(1)

if N < 4:
    print("N must be at least 4")
    sys.exit(1)
queens = []
col = pos = neg = []
queen_down(N, 0, [], queens, col, pos, neg)
for queen in queens:
    print(queen)
