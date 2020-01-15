__author__ = 'roeiherz'

"""
A magic index in an array A[0...n-1] is defined to be an index such that A[i] = i.
Given a sorted array of distinct integers, write a method to find a magic index, if one exists, in array A.
"""


def magic_index(arr, start, end):
    # Stop case
    if start > end:
        return -1

    middle = (end - start) / 2 + start
    if arr[middle] == middle:
        return middle

    if arr[middle] < middle:
        return magic_index(arr, middle + 1, end)
    else:
        return magic_index(arr, start, middle - 1)


if __name__ == '__main__':
    arr = [-40, -20, -1, 1, 2, 3, 5, 7, 9, 12, 13]
    start = 0
    end = len(arr) - 1
    print(magic_index(arr, start, end))
