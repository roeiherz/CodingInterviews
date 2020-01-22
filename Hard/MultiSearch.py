
__author__ = 'roeiherz'


"""
Given a string b and an array of smaller strings T, design a method to search b for each small string in T.
"""


def multi_search(b, T, prefix=''):

    if b == prefix:
        return True

    for i in range(len(T)):
        new_T = T[:i] + T[i+1:]
        new_prefix = prefix + T[i]
        if multi_search(b, new_T, new_prefix):
            return True

    return False


def multi_search_brute_force(b, T):

    for i in range(len(T)):
        sub_str = T[i]
        start_ind = b.find(sub_str)
        if start_ind == -1:
            return False
        end_ind = start_ind + len(sub_str)

        b = b[:start_ind] + b[end_ind:]
        if b == '' and len(T) == i:
            return True

    return False


if __name__ == '__main__':
    b = 'mississippi'
    # T = ['is', 'ppi', 'hi', 'sis', 'i', 'ssippi']
    T = ['mis', 'ppi', 'sis', 'si']
    # b = 'adam'
    # T = ['a', 'am', 'd']
    print(multi_search_brute_force(b, T))
    print(multi_search(b, T, ''))
