__author__ = 'roeiherz'

"""
Selection Sort
"""


def partition(A, p, q):
    pivot = A[q]
    curr = int(p)
    while curr < q:
        if pivot < A[curr]:
            curr += 1
        else:
            A[p], A[curr] = A[curr], A[p]
            p += 1
            curr += 1
    A[p], A[q] = A[q], A[p]
    return p


def selection_sort(A, p, q, k):
    if p >= q:
        return

    pivot = partition(A, p, q)
    if pivot == k or pivot == k+1:
        print(A[k])
        return

    if pivot > k:
        selection_sort(A, p=p, q=pivot - 1, k=k)
    else:
        selection_sort(A, p=pivot + 1, q=q, k=k)

    return


if __name__ == '__main__':
    A = [10, 5, 7, 8, 1, 2, 4]
    selection_sort(A, p=0, q=len(A)-1, k=3)
    print(A)

    A = [10, 5, 7, 8, 1, 3, 4, -4, 2]
    selection_sort(A, p=0, q=len(A)-1, k=3)
    print(A)
