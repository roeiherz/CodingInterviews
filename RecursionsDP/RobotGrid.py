import numpy as np

__author__ = 'roeiherz'

R, D = 5, 5

"""
Imagine a robot sitting on the upper left corner of grid with r rows and c columns. 
The robot can only move in two directions, right and down, but certain cells are "off limits" such that 
the robot cannot step on them. Design an algorithm to find a path for the robot from the top left to the bottom right.
"""


def robot_grid(mat, path, row=0, col=0):
    # Stop case
    if row < 0 or col < 0 or not mat[row, col]:
        return False

    if robot_grid(mat, path, row - 1, col) or robot_grid(mat, path, row, col - 1) or (row == 0 and col == 0):
        path[row, col] = 1
        return True

    return False


def robot_grid_memo(mat, path, mem, row=0, col=0):
    # Stop case
    if row < 0 or col < 0 or not mat[row, col]:
        return False

    if (row, col) in mem:
        return mem[(row, col)]

    if robot_grid(mat, path, row - 1, col) or robot_grid(mat, path, row, col - 1) or (row == 0 and col == 0):
        path[row, col] = 1
        if (row, col) not in mem:
            mem[(row, col)] = True
        return True

    return False


if __name__ == '__main__':
    path = np.zeros((R, D))
    mat = np.random.rand(R, D)
    mat[mat < 0.05] = 0
    mat[mat > 0.] = 1
    print("Mat: {}".format(mat))
    robot_grid(mat, path, R - 1, D - 1)
    # mem = {}
    # robot_grid_memo(mat, path, mem, R - 1, D - 1)
    print("Path: {}".format(path))
