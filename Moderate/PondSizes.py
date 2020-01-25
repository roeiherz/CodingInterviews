__author__ = 'roeiherz'

"""
You have an integer matrix representation a plot of land, where the value at that location represents the height above
see level. A value of zero indicates water. A pond is a region of water connected vertically, horizontally, 
or diagonally. The size of the pond is the total number of connected water cells. Write a method to compute
the sizes of all ponds in the matrix.

Example:

Input:
0 2 0 0
0 1 0 1
1 1 0 1
0 1 0 1

Output: 6, 3 (in any order)
"""


def compute_pond(A, i, j, locations):
    ind_i_min = max(i - 1, 0)
    ind_i_max = min(i + 1, len(A)-1)
    ind_j_min = max(j - 1, 0)
    ind_j_max = min(j + 1, len(A)-1)
    locations[i][j] = -1
    size = 0
    for k in range(ind_i_min, ind_i_max+1):
        for l in range(ind_j_min, ind_j_max+1):
            if locations[k][l] != -1 and A[k][l] > 0:
                locations[k][l] = -1
                size += A[k][l] + compute_pond(A, k, l, locations)
    return size


def pond(A):
    locations = [[0 for j in range(len(A))] for i in range(len(A))]
    sizes = set()
    for i in range(len(A)):
        for j in range(len(A)):
            if locations[i][j] != -1 and A[i][j] != 0:
                size = A[i][j] + compute_pond(A, i, j, locations)
                sizes.add(size)

    print("Sizes: {}".format(sizes))
    return


if __name__ == '__main__':
    # 0 2 1 0
    # 0 1 0 1
    # 1 1 0 1
    # 0 1 0 1
    # Output: {10}
    A = [[0, 0, 1, 0], [2, 1, 1, 1], [1, 0, 0, 0], [0, 1, 1, 1]]
    pond(A)
    # 0 2 0 0
    # 0 1 0 1
    # 1 1 0 1
    # 0 1 0 1
    # Output: {6, 3}
    A = [[0, 0, 1, 0], [2, 1, 1, 1], [0, 0, 0, 0], [0, 1, 1, 1]]
    pond(A)
