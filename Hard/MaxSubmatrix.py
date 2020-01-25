import numpy as np

__author__ = 'roeiherz'

"""
Given an NxN matrix of positive and negative integers, write a code to find the submatrix with the largest possible sum.
"""


def sub_matrix_brute_force(A):
    """
    O(N^4)
    :param A:
    :return:
    """
    sub_matrix = None
    max_sum = 0
    for i in range(len(A)):
        for j in range(len(A)):
            for k in range(len(A), -1, -1):
                for l in range(len(A), -1, -1):
                    summ = A[i:k, j:l].sum()
                    if max_sum < summ:
                        max_sum = summ
                        sub_matrix = A[i:k, j:l]

    print("Sum: {}".format(max_sum))
    print("Submatrix: \n {}".format(sub_matrix))
    return


def sub_matrix_dynamic(A):
    """
    O(N^4)
    :param A:
    :return:
    """

    def _compute_sum(A):
        zz = np.zeros(A.shape)
        for i in range(len(A)):
            for j in range(len(A)):
                left = zz[i][j - 1] if j > 0 else 0
                top = zz[i - 1][j] if i > 0 else 0
                overlap = zz[i - 1][j - 1] if i > 0 and j > 0 else 0
                zz[i, j] = left + top - overlap + A[i, j]
        return zz

    def _get_sum(sum_mat, i, j, k, l):
        full = sum_mat[k, l]
        left = sum_mat[k, j-1] if j > 0 else 0
        top = sum_mat[i-1, l] if i > 0 else 0
        top_left = sum_mat[i - 1, j - 1] if i > 0 and j > 0 else 0
        return full - left - top + top_left

    sum_mat = _compute_sum(A)
    sub_matrix = None
    max_sum = 0
    for i in range(len(A)):
        for j in range(len(A)):
            for k in range(len(A)-1, -1, -1):
                for l in range(len(A)-1, -1, -1):
                    summ = _get_sum(sum_mat, i, j, k, l)
                    if max_sum < summ:
                        max_sum = summ
                        sub_matrix = A[i:k+1, j:l+1]

    print("Sum: {}".format(max_sum))
    print("Submatrix: \n {}".format(sub_matrix))
    return


if __name__ == '__main__':
    #  3  4  5  6
    #  1 -2  0  3
    #  7  0  0 -2
    # -3 -4 -5 -6
    # A = np.array([[3, 4, 5, 6], [1, -2, 0, 3], [7, 0, 0, -2], [-3, -4, -5, -6]])
    # print(A)
    # sub_matrix_brute_force(A)

    # -3 -4 -5 -6
    # -3, 4, 5, 6
    # -7 15 22 -2
    # -3 -4 -5 -6
    A = np.array([[-3, -4, -5, -6], [-3, 4, 5, 6], [-7, 15, 22, -2], [-3, -4, -5, -6]])
    print(A)
    sub_matrix_dynamic(A)
