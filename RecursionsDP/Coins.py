__author__ = 'roeiherz'

"""
Given an infinite number of quarters (25 cent), dimes (10 cent), nickels (5 cent), and pennies (1 cent),
write code to calculate the number of ways of representing n cents.
"""


def coins(n, arr):
    """
    Counting all ways e.g.: (5,1) and (1,5)
    """

    # Stop case
    if n < 0:
        return 0
    if n == 0:
        return 1

    ways = 0
    for i in range(0, len(arr)):
        ways += coins(n - arr[i], arr)

    return ways


def coins_dynamic(n, arr):
    # Stop case
    if n < 0:
        return 0
    if n == 0:
        return 1

    table = [0 for k in range(n + 1)]
    # Base case (If given value is 0)
    table[0] = 1

    for i in range(0, len(arr)):
        for j in range(arr[i], n + 1):
            table[j] += table[j - arr[i]]

    return table[n]


if __name__ == '__main__':
    # print(coins(20, [20, 10, 5, 1]))
    print(coins(4, [1, 2, 3]))

    #
    # arr = [20, 10, 5, 1]
    # m = len(arr)
    # n = 20
    # x = count(arr, m, n)
    # print (x)
