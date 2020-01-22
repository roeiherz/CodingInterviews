#TODO

__author__ = 'roeiherz'


"""
An array A contains all the integers from 0 to n, except for one number which is missing.
In this problem, we cannot access an entire integer in A with a single operation. 
The elements of A are represented in binary, and the only operation we can use to access them is 
"fetch the jth bit of A[i]", which takes constant time. Write code to find the missing integer. 
Can you do it in O(n) time?
"""


def missing_number(A, q, p):
    pass

if __name__ == '__main__':
    A = [1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]
    print(missing_number(A, q=1, p=len(A)-1))
