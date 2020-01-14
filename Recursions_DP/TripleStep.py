__author__ = 'roeiherz'

"""
Write a method to return all subsets of a set
"""


def power_set(subset):
    n = len(subset)
    # Stop case
    if n != 0:
        print(subset)

    for i in range(n):
        new_lst = subset[:i] + subset[i + 1:]
        power_set(new_lst)


def power_set_memo(subset, mem):
    n = len(subset)
    # Stop case
    if n != 0:
        if subset not in mem:
            mem.add(subset)
            print(subset)

    for i in range(n):
        new_lst = subset[:i] + subset[i + 1:]
        power_set_memo(new_lst, mem)


if __name__ == '__main__':
    mem = set()
    # power_set((1, 2, 3, 4))
    power_set_memo((1, 2, 3, 4), mem)
