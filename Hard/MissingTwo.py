import math

__author__ = 'roeiherz'

"""
You are given an array with all the numbers from 1 to N appearing exactly once, except for one number that is missing.
How can you find the missing number in O(N) time and O(1) space?. What if there were two numbers missing?.
"""


def shortest_seq_one_missing(A):
    n = len(A) + 1
    sn = n * (1 + n) / 2
    x = sn - sum(A)

    print("The missing number is x={}".format(x))
    return


def shortest_seq_two_missing(B):
    n = len(B) + 2
    sn = n * (1 + n) / 2
    arithmetic = sn - sum(B)

    m = 1
    for zz in B:
        m *= zz
    geometry = math.factorial(n) / m

    delta = (arithmetic ** 2 - 4 * geometry) ** 0.5
    x = (arithmetic + delta) / 2
    y = arithmetic - x
    print("The missing number is x={} and y={}".format(int(x), int(y)))
    return


if __name__ == '__main__':
    A = [1, 2, 3, 4, 6, 7]
    shortest_seq_one_missing(A)
    B = [1, 3, 4, 6, 7]
    shortest_seq_two_missing(B)
