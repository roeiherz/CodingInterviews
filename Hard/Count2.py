import math

import numpy as np

__author__ = 'roeiherz'

"""
Write a method to count the number of 2s that appear in all the numbers between 0 and n (inclusive)
Example: 25 -> 9 (2, 12, 20, 21, 22, 23, 24, 25; 22 counts for two 2s)
"""


def count_two_eff(n):
    cnt = 0
    digits = [ch for ch in str(n)]
    for i in range(len(digits)):
        d = int(digits[i])
        if 1 < d < 2:
            cnt += math.pow(10, d + 1)
        elif d == 2:
            pass
        elif d > 2:
            # d > 2
            pass
    return cnt


def count_two(n):
    cnt = 0
    for i in range(2, n + 1):
        ins = np.array([1 if ch == '2' else 0 for ch in str(i)])
        cnt += ins.sum()
    return cnt


####### Not working #####
# Counts the number of '2' digits between 0 and n
def numberOf2sinRange(number):
    def count2sinRangeAtDigit(number, d):
        powerOf10 = int(pow(10, d))
        nextPowerOf10 = powerOf10 * 10
        right = number % powerOf10

        roundDown = number - number % nextPowerOf10
        roundup = roundDown + nextPowerOf10

        digit = (number // powerOf10) % 10

        # if the digit in spot digit is
        if (digit < 2):
            return roundDown // 10

        if (digit == 2):
            return roundDown // 10 + right + 1

        return roundup // 10

    # Convert integer to String to find its length
    s = str(number)
    len1 = len(s)

    # Traverse every digit and count for every digit
    count = 0
    for digit in range(len1):
        count += count2sinRangeAtDigit(number, digit)

    return count


def occurences(n, d):

    def find_digit(ln):
        if ln < 2:
            digit = int(math.pow(10, ln))
        elif ln >= 2:
            digit = int(math.pow(10, ln-1))
        return digit

    cnt = 1
    itr = d
    while itr <= n:
        digit = find_digit(len(str(itr)))
        if itr % 10 == d and not itr / 10 == d:
            cnt += 1
            itr += 10
            if itr / digit == d:
                itr -= d
        elif itr / 10 == d:
            cnt += 1
            itr += 1
        else:
            itr += d

    return cnt


if __name__ == '__main__':
    n = 220
    print(occurences(n, d=2))
    # print(numberOf2sinRange(22))
    print(count_two(n))
