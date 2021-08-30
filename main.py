__author__ = 'roeiherz'

"""
Write a method to return all subsets of a set
"""


def power_set(A, set_of_sets):

    for i in range(len(A)):
        for j in range(len(A)):
            if i == j:
                continue

            new_set = frozenset(A[i:j+1])
            if new_set in set_of_sets:
                return set_of_sets
            set_of_sets.add(new_set)
            power_set(A, set_of_sets)


def power_set_memo(A, set_of_sets):

    if len(A) != 0:
        if A not in set_of_sets:
            set_of_sets.add(A)
            print(A)

    for i in range(len(A)):
        new_A = A[:i] + A[i+1:]
        power_set_memo(new_A, set_of_sets)


if __name__ == '__main__':
    sett = set([])
    print(power_set_memo((1, 2, 3, 4), sett))
    print(power_set([1, 2, 3, 4], sett))
