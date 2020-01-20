__author__ = 'roeiherz'

"""
You are given an array of integers (both positive and negative). Find the contiguous sequence with the largest sum.
Return the sum.
Example: [2, -8, 3, -2, 4, -10] -> 5; {3, -2, 4}
"""


def contiguous_seq(A, seq, maxx=0):

    # Stop if
    if len(A) < 1:
        return False

    for i in range(len(A)):
        for j in range(i, len(A)):
            curr_seq = A[i:j]
            if sum(curr_seq) > maxx:
                maxx = sum(curr_seq)
                seq = set()
                [seq.add(n) for n in curr_seq]
            contiguous_seq(curr_seq, seq, maxx)

    print("Max: {} with Sequence: {}".format(maxx, seq))
    return True


def contiguous_seq_eff(A, maxx=0):
    """
    No need for any recursion
    """

    # Stop if
    if len(A) < 1:
        return False

    for i in range(len(A)):
        for j in range(i, len(A)):
            curr_seq = A[i:j]
            if sum(curr_seq) > maxx:
                maxx = sum(curr_seq)
                seq = set()
                [seq.add(n) for n in curr_seq]

    print("Max: {} with Sequence: {}".format(maxx, seq))
    return True


def contiguous_seq_eff2(A, maxx=0, max_seq=set()):
    """
    No need for any recursion and only one for loop
    """

    # Stop if
    if len(A) < 1:
        return False

    sum_ = 0
    seq = set()
    for n in A:
        sum_ += n
        seq.add(n)
        if sum_ > maxx:
            maxx = sum_
            max_seq = seq.copy()
        elif sum_ < 0:
            sum_ = 0
            seq = set()

    print("Max: {} with Sequence: {}".format(maxx, max_seq))
    return True


if __name__ == '__main__':
    A = [2, -8, 3, -2, 4, -10]
    seq = set()
    # contiguous_seq(A, seq)
    # contiguous_seq_eff(A)
    contiguous_seq_eff2(A)
