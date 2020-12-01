__author__ = 'roeiherz'

"""
There are 3 types of edits that can be performed in strings: insert a char, remove a char, replace a char. 
Given two strings, write a function to check if they are one edit (or zero) away.
example: 'pale, ple' -> true; 'pales, bale' -> false
"""


def one_hand_hash(x, y):
    """
    Use hash; more space
    :param x: string
    :param y: string
    :return:
    """
    if x == y:
        return True

    # Fill dict of chars from the first string
    cnt = {}
    for ch in x:
        if ch not in cnt:
            cnt[ch] = 1
        else:
            cnt[ch] += 1

    # Remove existing chars from the second string
    for ch in y:
        if ch in cnt:
            cnt[ch] -= 1

    # Check everything is 0 except one key
    tmp = 0
    for k, v in cnt.items():
        if v != 0:
            tmp += 1
        if tmp > 1:
            return False

    return True


def one_hand_inplace(x, y):
    """
    Use inplace
    :param x: string
    :param y: string
    :return:
    """

    def one_difference(xx, yy):
        cnt = 0
        for i in range(len(xx)):
            if xx[i] != yy[i]:
                cnt += 1
            if cnt > 1:
                return False
        return True

    def one_replacement(xx, yy):
        ind1 = 0
        ind2 = 0
        cnt = 0
        while ind1 < len(xx) and ind2 < len(yy):
            if xx[ind1] != yy[ind2]:
                cnt += 1
                ind1 += 1
            else:
                ind1 += 1
                ind2 += 1

        return False if cnt > 1 else True

    if len(x) == len(y):
        return one_difference(x, y)
    if len(x) == len(y) + 1:
        return one_replacement(x, y)
    if len(x) + 1 == len(y):
        return one_replacement(y, x)

    return False


if __name__ == '__main__':
    print(one_hand_inplace("pale", "ple"))
    print(one_hand_inplace("ple", "pale"))
    print(one_hand_inplace("pales", "pale"))
    print(one_hand_inplace("pale", "bale"))
    print(one_hand_inplace("pale", "bake"))
