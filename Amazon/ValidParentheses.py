"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.


Example 1:

Input: s = "()"
Output: true

Example 2:

Input: s = "()[]{}"
Output: true

Example 3:

Input: s = "(]"
Output: false

Example 4:

Input: s = "([)]"
Output: false

Example 5:

Input: s = "{[]}"
Output: true



"""

__author__ = 'roeiherz'


def isValid_wrong(s):
    """
    :type s: str
    :rtype: bool
    """
    mapp = {}
    for x in s:

        if x in ['(', '[', '{']:
            if x not in mapp:
                mapp[x] = 1
            else:
                mapp[x] += 1
        else:
            if x == ')':
                if '(' in mapp and mapp['('] > 0:
                    mapp['('] -= 1
                else:
                    return False
            elif x == ']':
                if '[' in mapp and mapp['['] > 0:
                    mapp['['] -= 1
                else:
                    return False
            elif x == '}':
                if '{' in mapp and mapp['{'] > 0:
                    mapp['{'] -= 1
                else:
                    return False

    if mapp.get('(', 0) == 0 and mapp.get('[', 0) == 0 and mapp.get('{', 0) == 0:
        return True
    else:
        return False


def isValid(s):
    """
    :type s: str
    :rtype: bool
    """
    if len(s) == 1:
        return False

    stack = []
    for x in s:

        if x in ['(', '[', '{']:
            stack.append(x)
        else:
            if len(stack) == 0:
                return False

            if x == ')' and stack[-1] != '(':
                return False
            if x == ']' and stack[-1] != '[':
                return False
            if x == '}' and stack[-1] != '{':
                return False
            stack.pop()

    if len(stack) != 0:
        return False
    return True


if __name__ == '__main__':
    print(isValid("){"))
    print(isValid("(("))
    print(isValid("()[]{}"))
    print(isValid("{[]}"))
    print(isValid("(]"))
    print(isValid("([)]"))
    print(isValid("{[]}"))
