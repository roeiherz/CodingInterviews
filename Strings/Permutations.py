"""
This script counts all permutation in a string
"""

__author__ = 'roeiherz'


def permutation_v4(x, y):
    """
    x,y: strings.
    A method to decide if x is a permutation of y (for example 'aedcbc' is a perm of 'cabcde')
    """

    # option1: sort and check O(nlogn)
    x_tmp = ''.join(sorted(x))
    y_tmp = ''.join(sorted(y))
    if x_tmp in y_tmp:
        return True
    return False

    # option2: hashing
    def _occur(x):
        map = {}
        for s in x:
            if s not in map:
                map[s] = 1
            else:
                map[s] += 1
        return map
    map_x, map_y = _occur(x), _occur(y)
    for k, v in map_x.items():
        if k not in map_y and map_y[k] != v:
            return False
    return True


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
    Counts only sub permutation of the string
    :param string: abc
    :param prefix: ''
    :return: a, b, c, ab, ac, bc (not ba or cb or ca)
    """

    if len(string) != 0:
        print(prefix)

    for i in range(len(string)):
        new_string = string[0: i] + string[i + 1:]
        permutation_v2(new_string, prefix + string[i])


def permutation(string):
    """
    Counts every strings permutations
    :param string: abc
    :return: a, b, c, ab, bc, ac, ba, cb, ca
    """

    if string != '':
        print(string)

    for i in range(len(string)):
        new_string = string[0: i] + string[i + 1:]
        permutation(new_string)


def permutation_without_dups(string, prefix):
    """
    Write a method to compute all permutations of a string of unique chars
    :param string:
    :return:
    """

    # Stop if
    if prefix != '':
        print(prefix)

    for i in range(len(string)):
        new_str = string[:i] + string[i+1:]
        permutation_without_dups(new_str, prefix + string[i])


def permutation_with_dups(string, prefix, sett):
    """
    Write a method to compute all permutations of a string of unique chars
    :param string:
    :return:
    """

    # Stop if
    if prefix != '':
        print(prefix)

    for i in range(len(string)):
        new_str = string[:i] + string[i+1:]
        new_prefix = prefix + string[i]
        if new_prefix not in sett:
            sett.add(new_prefix)
        else:
            continue
        permutation_with_dups(new_str, new_prefix, sett)


if __name__ == '__main__':
    # permutation('abc')
    # print("new")
    # permutation_v2('abc', "")
    # permutation_v3('abc')
    # permutation_v4('aedcbc', 'cabcde')
    # permutation_without_dups("abcde", '')
    sett = set()
    permutation_with_dups("abcde", '', sett)
