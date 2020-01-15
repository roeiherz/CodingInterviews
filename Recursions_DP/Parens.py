__author__ = 'roeiherz'

"""
Implement an algorithm to print all valid (e.g., properly opened and closed) combinations of n pairs of parentheses.
Example: 3 -> ((())), (()()), ()(()), ()()()
"""


def paren(n, prefix, cnt=0):
    # Stop case
    if n == 0 and cnt == 0:
        print(prefix)

    if n > cnt:
        paren(n, prefix + '(', cnt+1)
    if cnt > 0:
        paren(n-1, prefix + ')', cnt-1)


if __name__ == '__main__':
    paren(3, '')
