#TODO

import numpy as np

__author__ = 'roeiherz'

"""
Design an algorithm to figure out if someone has won a game of tic-tac-toe
"""


class TicTacTow:
    def __init__(self, N=3):
        self.n = N
        self.board = [[None for i in range(N)] for i in range(N)]

    def fill(self, x, y, item=0):
        if item != 0 or item != 1:
            return None
        self.board[x][y] = item

    def is_end(self):
        # Check rows
        for row in self.board:
            map = {0: 0, 1: 0}
            for col in row:
                if col is None:
                    return False
                map[col] += 1
            if self.n in map.values():
                return True

        # Check cols
        for i in range(self.n):
            map = {0: 0, 1: 0}
            for j in range(self.n):
                if self.board[j][i] is None:
                    return False
                map[self.board[j][i]] += 1
            if self.n in map.values():
                return True

        # Check diag
        map = {0: 0, 1: 0}
        for i in range(self.n):
            map[self.board[i][i]] += 1
        if self.n in map.values():
            return True

    def is_end_lst_move(self, i, j):
        """
        Get the last move that has been done in location (i,j)
        """
        # Check rows
        map = {0: 0, 1: 0}
        for col in self.board[i]:
            if col is None:
                return False
            map[col] += 1
        if self.n in map.values():
            return True

        # Check cols
        map = {0: 0, 1: 0}
        for col in range(self.n):
            if self.board[j][col] is None:
                return False
            map[self.board[j][col]] += 1
        if self.n in map.values():
            return True

        # Check diag
        map = {0: 0, 1: 0}
        for i in range(self.n):
            map[self.board[i][i]] += 1
        if self.n in map.values():
            return True


if __name__ == '__main__':
    game = TicTacTow()
    game.is_end()