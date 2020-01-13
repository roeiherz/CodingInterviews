import re

__author__ = 'roeiherz'

"""
Assume you have a method isSubstring which checks if one word is a substring of another. 
Given two strings, s1 and s2, write a code to check if s2 is a rotation of s1 using one call to IsSubstring
example: 'waterbottle', 'erbottlewat' -> True
"""


def string_rotation_ineffcient(x, y):
    """
    :param x: string
    :param y: string
    :return:
    """
    def find_start_ind(string1, string2):
        chr = string1[0]
        matches = re.finditer(chr, string2)
        indices = [match.start() for match in matches]

        if len(indices) == 1:
            return indices[0]

        for ind in indices:
            if string2[ind:] in string1:
                return ind
        return -1

    if len(x) != len(y):
        return False

    ind1 = 0
    ind2 = find_start_ind(x, y)
    while ind1 < len(x):
        if x[ind1] != y[ind2]:
            return False

        ind2 = (ind2 + 1) % len(x)
        ind1 += 1

    return True


def string_rotation(x, y):
    """
    :param x: string
    :param y: string
    :return:
    """
    if len(x) != len(y):
        return False

    new_str = x + x
    if y in new_str:
        return True
    return False


if __name__ == '__main__':
    # print(string_rotation_ineffcient('waterbottle', 'erbottlewat'))
    print(string_rotation('waterbottle', 'erbottlewat'))
