__author__ = 'roeiherz'

"""
Design an algorithm to find all pairs of integers within an array which sum to a specified value.
"""


def pair_sum(A, n=0):
    """
    O(n) but requires more memory (for the set)
    """
    sett = set()
    for x in A:
        if n-x not in sett:
            sett.add(n-x)

    lst = []
    for x in A:
        if n-x in sett and (x, n-x) not in lst:
            lst.append((x, n-x))
    return lst


def pair_sum_eff(A, n=0):
    """
    O(nlogn) but a memory efficient
    """

    A = sorted(A)
    lst = []
    first = 0
    last = len(A) - 1
    while first < last:
        if A[first] + A[last] == n:
            lst.append((A[first], A[last]))
            first += 1
            last -= 1
        elif A[first] + A[last] < n:
            first += 1
        else:
            last -= 1

    return lst


if __name__ == '__main__':
    A = [4, 1, 2, 1, 1, 2]
    A = [-2, -1, 0, 1, 2, 4, 7]
    n = 5
    # print(pair_sum(A, n))
    print(pair_sum_eff(A, n))
