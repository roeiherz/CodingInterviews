"""
Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.



Example 1:

Input: nums = [3,2,1,5,6,4], k = 2
Output: 5

Example 2:

Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4

"""

__author__ = 'roeiherz'


def partition(A, p, q):
    curr = int(p)
    pivot = A[q]
    while curr < q:
        if pivot < A[curr]:
            curr += 1
        else:
            A[p], A[curr] = A[curr], A[p]
            p += 1
            curr += 1
    A[p], A[q] = A[q], A[p]
    return p


def selection(A, k, p, q):
    if p >= q:
        return

    pivot = partition(A, p, q)

    if pivot == k or pivot == k - 1:
        # print(A[pivot])
        return A[pivot]
    elif pivot > k:
        return selection(A, k, p, pivot - 1)
    else:
        return selection(A, k, pivot + 1, q)


def findKthLargest(A, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """

    return selection(A, len(A)-k, p=0, q=len(A) - 1)


if __name__ == '__main__':
    findKthLargest([2,1], 1)
    findKthLargest([3, 2, 1, 5, 6, 4], 2)
