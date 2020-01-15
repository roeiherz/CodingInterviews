import numpy as np

__author__ = 'roeiherz'


"""
You have 3 towers and N disks of different sizes which can slide onto any tower. 
The puzzle start with disks sorted in ascending order of size from top to bottom. You have the following constraints:
1. Only one disk can be moved at a time.
2. A disk is slid off the top of one tower onto another tower.
3. A disk cannot be placed on top of a smaller disk.
Write a program to move the disks from the first tower to the last using stacks.
"""


def tower_hanoi(mat):
    # Stop case
    if row < 0 or col < 0 or not mat[row, col]:
        return False

    return False


if __name__ == '__main__':
    tower = [[]]
    tower_hanoi(mat)
