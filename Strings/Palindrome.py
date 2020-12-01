import numpy as np
from copy import deepcopy

__author__ = 'roeiherz'


def palindrome_perm(x):
    """
    This method outputs the all palindromes
    :param x: string
    :return: all permuted palindromes
    """
    def _get_perms(xx, lst, step=0):
        if len(xx) == step:
            # Check palindromes
            if _is_palindrome(xx):
                return lst.add(xx)

        for i in range(step, len(xx)):
            s = deepcopy(xx)
            arr = [c for c in s]
            arr[i], arr[step] = arr[step], arr[i]
            s = ''.join(arr)
            _get_perms(s, lst, step + 1)
        return lst

    def _is_palindrome(xx):
        xx = xx.replace(' ', '').lower()
        n = len(xx)
        for i in range(n / 2):
            if xx[i] != xx[n - i - 1]:
                return False
        return True

    # Get all permutations
    lst = set()
    palindromes = _get_perms(x, lst)

    return palindromes


def palindrome_perm_hash(x):
    """
    This function returns True whether there is a permuted palindrome or not
    :param x: string
    :return: True or False
    """

    # Use mapping - count occurrences; only one char should be odd; all others even
    map = {}
    x_space_out = x.replace(" ", "").lower()
    for c in x_space_out:
        if c in map:
            map[c] += 1
            map[c] %= 2
        else:
            map[c] = 1

    # Only one char should be 1; all other 0
    if np.array(map.values()).sum() == 1:
        return True
    return False


if __name__ == '__main__':
    "Given a string write a method to check its perm is a palindrome"
    # palindrome_perm("Tact Coa")
    palindrome_perm_hash("Tact Coa")
