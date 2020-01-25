__author__ = 'roeiherz'

"""
Merge Sort
"""


def merge(A, B):
    merged = []
    ind_a = 0
    ind_b = 0
    while ind_a < len(A) and ind_b < len(B):
        if A[ind_a] < B[ind_b]:
            merged.append(A[ind_a])
            ind_a += 1
        else:
            merged.append(B[ind_b])
            ind_b += 1

    # Append the reminding indices from the remain list
    while ind_a < len(A):
        merged.append(A[ind_a])
        ind_a += 1
    while ind_b < len(B):
        merged.append(B[ind_b])
        ind_b += 1

    return merged


def merge_sort(A):
    if len(A) == 1:
        return A

    pivot = len(A) // 2
    A_1 = merge_sort(A[:pivot])
    A_2 = merge_sort(A[pivot:])
    merged = merge(A_1, A_2)

    return merged


if __name__ == '__main__':
    # A = [10, 5, 7, 8, 1, 2, 4]
    A = [10, 5, 7, 8, 1, 2, 4,3]
    new_A = merge_sort(A)
    print(new_A)

