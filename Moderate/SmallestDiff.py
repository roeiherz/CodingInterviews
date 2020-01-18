__author__ = 'roeiherz'

"""
Given two arrays of integers, compute the pair of values (one value in each array) with the smallest (non-negative) 
diff. Return the diff.
Example: [1,3,15,11,2], [23, 127, 235, 19, 8]
"""


def smallest_diff(A, B):
    """
    O(AlogA +BlogB + A+B)
    """
    # Sort arrays
    A = sorted(A)
    B = sorted(B)

    ind_a = 0
    ind_b = 0
    diff = 100000000000000000
    while ind_a < len(A) and ind_b < len(B):
        if diff > abs(A[ind_a] - B[ind_b]):
            diff = abs(A[ind_a] - B[ind_b])

        new_ind_a = min(ind_a + 1, len(A)-1)
        new_ind_b = min(ind_b + 1, len(B)-1)
        if abs(A[new_ind_a] - B[ind_b]) > abs(B[new_ind_b] - A[ind_a]):
            ind_b += 1
        else:
            ind_a += 1

    print("Smallest Diff {}".format(diff))


if __name__ == '__main__':
    A = [1, 2, 11, 15]
    B = [4, 12, 19, 23, 127, 235]
    smallest_diff(A, B)
