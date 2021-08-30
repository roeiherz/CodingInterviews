"""
The Stock Span Problem
https://www.geeksforgeeks.org/the-stock-span-problem/

For example, if an array of 7 days prices is given as {100, 80, 60, 70, 60, 75, 85},
then the span values for corresponding 7 days are {1, 1, 1, 2, 1, 4, 6}

"""


__author__ = 'roeiherz'


def calculateSpan(price):
    S = [0] * len(price)
    S[0] = 1
    for i in range(1, len(price)):
        counter = 1
        while i-counter >= 0 and price[i] > price[i-counter]:
            counter += S[i - counter]
        S[i] = counter


if __name__ == '__main__':
    # Driver program to test above function
    price = [100, 80, 60, 70, 60, 75, 85]
    calculateSpan(price)
    price = [10, 4, 5, 90, 120, 80]
    calculateSpan(price)