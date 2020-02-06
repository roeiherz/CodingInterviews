__author__ = 'roeiherz'


def test(A, new_A, max_set, max_sum=-20000000):
    if len(A) == 0:
        max_set.add(max_sum)
        return

    for i in range(len(A)):
        sub_arr = A[:i] + A[i+1:]
        newA = new_A + [A[i]]
        if max_sum < sum(newA):
            max_sum = sum(newA)
        test(sub_arr, newA, max_set, max_sum)


def split_word(A, sett):

    if A in sett:
        return True

    for i in range(len(A)):
        left = A[:i]
        right = A[i:]
        if split_word(left, sett) and split_word(right, sett):
            return True

    return False


if __name__ == '__main__':
    sett = set()
    x = "dogwalker"
    split_word(x, sett)

    A = [2, -8, 3, -2, 4, -10]
    new_arr = []
    max_set = set()
    test(A, new_arr, max_set)
    print max(max_set)
