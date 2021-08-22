"""
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai).
n vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0).
Find two lines, which, together with the x-axis forms a container, such that the container contains the most water.

Notice that you may not slant the container.

Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7].
In this case, the max area of water (blue section) the container can contain is 49.

Example 2:

Input: height = [1,1]
Output: 1

Example 3:

Input: height = [4,3,2,1,4]
Output: 16

Example 4:

Input: height = [1,2,1]
Output: 2

https://leetcode.com/explore/interview/card/amazon/76/array-and-strings/2963/
"""

__author__ = 'roeiherz'


def maxArea(height):
    i = 0
    j = len(height) - 1
    maxx = 0
    while i < j:
        area = min(height[i], height[j]) * (j - i)
        if area > maxx:
            maxx = area

        if height[i] < height[j]:
            i += 1
        else:
            j -= 1

    print(maxx)


if __name__ == '__main__':
    maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7])
    maxArea([1,2])
    maxArea([1,2,4,3])
