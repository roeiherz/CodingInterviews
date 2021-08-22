"""
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.


Example 1:

Input: s = "leetcode"
Output: 0

Example 2:

Input: s = "loveleetcode"
Output: 2

Example 3:

Input: s = "aabb"
Output: -1

"""

__author__ = 'roeiherz'


def firstUniqChar(s):
    """
    :type s: str
    :rtype: int
    """
    mapping = {}
    for x in s:
        if x not in mapping:
            mapping[x] = 1
        else:
            mapping[x] += 1

    for i in range(len(s)):
        x = s[i]
        if mapping[x] == 1:
            return i
    return -1


if __name__ == '__main__':
    firstUniqChar("loveleetcode")