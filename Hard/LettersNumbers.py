__author__ = 'roeiherz'

"""
Given an array filled with letters and numbers, find the longest subarray with an equal number of letters and numbers.
"""


def letters_numbers_equals(A):
    """
    Here, I'm trying to outputs the sub-array that its numbers and letters equals:
    [1, 1, 2, 's', 7, 's', 'b', 5, 'q'] -> 1,8 (4 int and 4 str)
    O(N^2)
    :param A:
    :return:
    """

    max_size = 0
    start = 0
    end = 0
    for i in range(len(A)):
        letters = 0
        nums = 0
        size = 0
        for j in range(len(A)):

            if i > j:
                continue

            if isinstance(A[j], int):
                nums += 1
            elif isinstance(A[j], str):
                letters += 1

            if nums == letters:
                size = nums
            if size > max_size:
                max_size = size
                start = i
                end = j

    print("Start index: {}, end index: {}, array: {}".format(start, end, A[start:end + 1]))
    return True


def letters_numbers_equals_eff(A):
    """
    Here, I'm trying to outputs the sub-array that its numbers and letters equals:
    [1, 1, 2, 's', 7, 's', 'b', 5, 'q'] -> 1,8 (4 int and 4 str)
    :param A:
    :return:
    """

    def _count(A):
        cnt_int = 0
        map_int = set()
        cnt_str = 0
        map_str = set()
        for i in range(len(A)):
            x = A[i]
            if isinstance(x, int):
                cnt_int += 1
                map_int.add(i)
            if isinstance(x, str):
                cnt_str += 1
                map_str.add(i)
        if cnt_int < cnt_str:
            return cnt_int, str, min(map_int), max(map_int)
        else:
            return cnt_str, int, min(map_str), max(map_str)

    cnt, type, i, j = _count(A)
    other_cnt = 0
    for q in range(i, j):
        if isinstance(A[q], type):
            other_cnt += 1

    start = i
    end = j
    while other_cnt < cnt:
        # Move left
        if start - 1 >= 0 and isinstance(A[start - 1], type):
            other_cnt += 1
            start -= 1
        # Move right
        if other_cnt < cnt and end + 1 < len(A) and isinstance(A[end + 1], type):
            other_cnt += 1
            end += 1

    print("Start index: {}, end index: {}, array: {}".format(start, end, A[start:end + 1]))
    return True


def equal_letters_numbers_brute_force(A):
    """
    Here, I'm trying to outputs the sub-array that its numbers and letters *content* are equal:
    Count(A, subarray) = Count(B, subarray) in [A,B,A,A,A,B,B,B,A,B,A,A,B,B,A,A,A,A,A,A]
    :param A:
    :return:
    """

    def has_equal(A, i, j):
        # Create mapping
        mapp = {}
        for q in range(i, j + 1):
            x = A[q]
            if x in mapp:
                mapp[x] += 1
            else:
                mapp[x] = 1

        # Empty
        if not mapp:
            return 0

        # Equal number of keys; return the max
        if max(mapp.values()) == min(mapp.values()):
            return max(mapp.values())

        # No equal
        return 0

    max_size = 0
    start = 0
    end = 0

    for i in range(len(A)):
        # both working
        # for j in range(len(A)-1, 1, -1):
        for j in range(i, len(A) - 1):
            cnt = has_equal(A, i, j)
            if cnt > 0 and cnt > max_size:
                max_size = cnt
                start = i
                end = j

    print("Start index: {}, end index: {}, array: {}".format(start, end, A[start:end + 1]))
    return True


if __name__ == '__main__':
    A = [1, 1, 2, 's', 7, 's', 'b', 5, 'q']
    letters_numbers_equals(A)
    A = ['A', 5, 'A', 'A', 'A', 2, 1, 0, 'A', -3, 'A', 'A', -5, 7, 'A', 'A', 'A', 'A', 'A', 'A']
    letters_numbers_equals_eff(A)
    A = ['A', 'B', 'A', 'A', 'A', 'B', 'B', 'B', 'A', 'B', 'A', 'A', 'B', 'B', 'A', 'A', 'A', 'A', 'A', 'A']
    equal_letters_numbers_brute_force(A)
