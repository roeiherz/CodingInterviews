import numpy as np

__author__ = 'roeiherz'

"""
Write an algorithm to print all ways of arranging 8 queens on 8x8 chess board so that none of them share the same
row, column or diagonal. In this case, "diagonal" means all diagonals, not just the two that bisect the board.
"""

N = 5


def is_legal(mat, i, j):

    if i >= N or j >= N:
        return False

    # Row or column are not allowed
    if mat[i, :].sum() >= 1 or mat[:, j].sum() >= 1:
        return False

    # Diagonal is not allowed
    for ii in range(N):
        if i - ii >= 0 and j - ii >= 0 and mat[i - ii, j - ii] == 1:
            return False
        if i + ii < N and j + ii < N and mat[i + ii, j + ii] == 1:
            return False
        if i - ii >= 0 and j + ii < N and mat[i - ii, j + ii] == 1:
            return False
        if i + ii < N and j - ii >= 0 and mat[i + ii, j - ii] == 1:
            return False

    return True


def chess(mat, col=0):
    # Stop case
    if col >= N:
        return True

    for row in range(N):
        if is_legal(mat, row, col):
            mat[row, col] = 1
            if chess(mat, col + 1):
                return True
            # If placing queen in mat doesn't lead to a solution then remove queen
            mat[row, col] = 0

    return False


if __name__ == '__main__':
    mat = np.zeros((N, N))
    chess(mat, col=0)
    print(mat)
