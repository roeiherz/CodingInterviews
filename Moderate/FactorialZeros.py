import math

__author__ = 'roeiherz'

"""
Write an algorithm which computes the number of trailing zeros in n factorial.
"""


def factorial(n, mem):
    if n == 0:
        return 1

    if n - 1 in mem:
        return mem[n - 1] * n

    mem[n] = factorial(n - 1, mem) * n
    return mem[n]


def factor5(n):
    """
    """

    if n == 0:
        return 0

    cnt = 0
    while n % 5 == 0:
        cnt += 1
        n /= 5
    return cnt


def trailing_zeros(n):
    """
    Each 5! add one trailing zero. Note that 25! add 2 trailing zeros because 5*5
    """
    cnt = 0
    for i in range(2, n + 1):
        cnt += factor5(i)
    return cnt


def trailing_zeros_eff(n):
    """
    Each 5! add one trailing zero. Note that 25! add 2 trailing zeros because 5*5
    """
    m = math.sqrt(n)
    return n // 5 + m -1


if __name__ == '__main__':
    mem = {}
    print(trailing_zeros(25))

    factorial(30, mem)
    for k, v in mem.items():
        print("N: {}, N!: {}".format(k, v))
