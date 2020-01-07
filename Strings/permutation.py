"""
This script counts all permutation in a string
"""

__author__ = 'roeiherz'


def permutation_v3(string, step=0):
    """
    Print every permutation of the string in the same length
    :param string: abc
    :return: abc, bac, cba, cab, acb, bca
    """

    n = len(string)
    if n == step:
        print ''.join(string)

    for i in range(step, n):
        copy_str = [c for c in string]
        copy_str[i], copy_str[step] = copy_str[step], copy_str[i]
        permutation_v3(copy_str, step + 1)


def permutation_v2(string, prefix):
    """
    Counts every permutation of the string
    :param string: abc
    :param prefix:
    :return: a, b, c, ab, ac, bc
    """

    if len(string) != 0:
        print(prefix)

    for i in range(len(string)):
        new_string = string[0: i] + string[i + 1:]
        permutation_v2(new_string, prefix + string[i])


def permutation(string):
    """
    Counts only sub strings permutations
    :param string: abc
    :return: a, b, c, ab, bc
    """

    if string != '':
        print(string)

    for i in range(len(string)):
        new_string = string[0: i] + string[i + 1:]
        permutation(new_string)


if __name__ == '__main__':
    # permutation('abc')
    # permutation_v2('abc', "")
    permutation_v3('abc')
