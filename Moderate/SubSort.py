__author__ = 'roeiherz'

"""
Given an array if integer, write a method to find indices m and n such that if you sorted elements m trough n,
the entire array would be sorted. Minimize n - m (that is, find the smallest such sequence).
Example: [1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19] -> (3, 9)
"""


def smallest_diff(A, q, p):
    """
    not efficient
    :param A:
    :param q:
    :param p:
    :return:
    """

    if q < 0 or p > len(A):
        return False

    if max(A[:q]) < min(A[q:p]):
        return smallest_diff(A, q+1, p)

    if max(A[q:p]) < min(A[p:]):
        return smallest_diff(A, q, p-1)

    return q-1, p


if __name__ == '__main__':
    A = [1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]
    # smallest_diff(A, q=len(A) / 2 - 1, p=len(A) / 2 + 1)
    print(smallest_diff(A, q=1, p=len(A)-1))
