"""
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals,
and return an array of the non-overlapping intervals that cover all the intervals in the input.

Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.



"""

import numpy as np

__author__ = 'roeiherz'


def merge(intervals):
    """
    :type intervals: List[List[int]]
    :rtype: List[List[int]]
    """
    intervals = remove_dup(intervals)
    if len(intervals) == 1:
        return intervals

    pairs = {interval[0]: interval[1] for interval in intervals}
    sorted(intervals, key=lambda x: x[0])  # sort intervals based on start time
    stack = [interval[0] for interval in intervals][::-1]  # based on order times

    new_pairs = []
    cand_s = stack.pop()
    cand_e = pairs[cand_s]
    i = 0
    while i < len(intervals):
        interval = intervals[i]
        start, end = interval
        if start == cand_s and end == cand_e:
            i += 1
            continue

        if cand_e - start >= 0:
            new_pairs.append([cand_s, end])
            cand_s = stack.pop()
            cand_e = pairs[cand_s]
        else:
            new_pairs.append([start, end])
            cand_s = stack.pop()
            cand_e = pairs[cand_s]
        i += 1

    return new_pairs


def remove_dup(intervals):
    i = 0
    new_intervals = []
    while i < len(intervals):
        new_intervals.append(intervals[i])
        if i + 1 < len(intervals) and intervals[i][0] == intervals[i + 1][0] and intervals[i][1] == intervals[i + 1][1]:
            i += 2
            continue
        i += 1
    return new_intervals


if __name__ == '__main__':
    merge([[[1, 4], [1, 5]]])
    merge([[1, 4], [4, 5]])
    merge([[1, 3], [1, 3]])
    merge([[1, 3], [2, 6], [8, 10], [15, 18]])
