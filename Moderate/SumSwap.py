__author__ = 'roeiherz'

"""
Given two arrays of integers, find a pair of values (one value from each array) that you can swap to give the
two arrays the same sum.
Example: [4,1,2,1,1,2], [3,6,3,3] -> [1,3]
"""


def sum_swap(A, B):
    """
    O(AlogA + BlogB + A + B)
    """

    sum_a = sum(A)
    sum_b = sum(B)
    if (sum_a - sum_b) % 2 == 0:
        diff = (sum_a - sum_b) / 2
    else:
        return False

    a = 0
    b = 0
    A = sorted(A)
    B = sorted(B)
    while a < len(A) and b < len(B):
        x = A[a]
        y = B[b]
        if x - y == diff:
            return [x, y]

        if x - y > diff:
            a += 1
        else:
            b += 1

    return False


if __name__ == '__main__':
    A = [4,1,2,1,1,2]
    B = [3,6,3,3]
    print(sum_swap(A, B))
