__author__ = 'roeiherz'


"""
A majority element is an element that makes up more than half of the items in an array.
Given a positive integers array, find the majority element. If there is no majority element, return -1.
Do this in O(N) time and O(1) space.
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


def majority_element(A, p, q, k):
    if k > q - p + 1:
        return

    pivot = partition(A, p, q)

    if pivot == p + k:
        return A[pivot]
    elif pivot > p + k:
        return majority_element(A, p=p, q=pivot-1, k=k)
    else:
        return majority_element(A, p=pivot+1, q=q, k=k)


def majority_element_eff(A):

    def _get_candidate(A):
        majority = 0
        cnt = 0
        for n in A:
            if cnt == 0:
                majority = n
            if majority == n:
                cnt += 1
            else:
                cnt -= 1
        return majority

    candidate = _get_candidate(A)
    cnt = 0
    for n in A:
        if n == candidate:
            cnt += 1

    return candidate if cnt >= len(A) / 2 else -1


if __name__ == '__main__':
    A = [3, 5, 3, 4, 2, 2, 1, 8]
    candidate = majority_element_eff(A)
    # candidate = majority_element(A, p=0, q=len(A)-1, k=(len(A)-1)/2)
    # cnt = 0
    # for n in A:
    #     if n == candidate:
    #         cnt += 1
    #
    # print candidate if cnt >= len(A) / 2 else -1
