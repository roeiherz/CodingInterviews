__author__ = 'roeiherz'

"""
QuickSort
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


def quick_sort(A, p, q):
    if p >= q:
        return

    pivot = partition(A, p, q)
    quick_sort(A, p=p, q=pivot-1)
    quick_sort(A, p=pivot+1, q=q)

    return True


if __name__ == '__main__':
    A = [10, 5, 7, 8, 1, 2, 4]
    quick_sort(A, p=0, q=len(A)-1)
    print(A)
