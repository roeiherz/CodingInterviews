__author__ = 'roeiherz'

"""
A popular masseuse receives a sequence of back-to-back appointment requests and is debating which ones to accept. 
She needs a 15-minute break between appointments and therefore she can't accept any adjacent requests.
Given a sequence of back-to-back appointment requests (all multiple of 15 minutes, none overlap, and none can be moved),
find the optimal (highest total booked minutes) set the masseuse can honor. Return the number of minutes.
Example: [30,15,60,75,45,15,15,45]-> 180 minutes (30, 60, 45, 45)
"""


def masseuse(A, ind=0, summ=0):
    """
    Return the max
    :param A:
    :param ind:
    :param summ:
    :return:
    """

    # Stop if
    if ind > len(A)-1:
        return summ

    return max(masseuse(A,  ind+2, summ+A[ind]), masseuse(A, ind+1, summ))


def masseuse2(A, appointments, ind=0, summ=0):
    """
    Return the max and appointments
    :param A:
    :param appointments:
    :param ind:
    :param summ:
    :return:
    """

    # Stop if
    if ind > len(A)-1:
        return summ

    if masseuse2(A, appointments, ind + 2, summ + A[ind]) > masseuse2(A, appointments, ind + 1, summ):

        if len(appointments) == 0:
            appointments.append((ind, summ))
        else:
            item = appointments[-1]
            if summ+A[ind] == item[1] and ind < item[0]:
                appointments.append((ind, summ))

        return summ+A[ind]
    else:
        return summ


def masseuse_memo(A, memo, ind=0):
    """
    Return the max with memo
    :param A:
    :param memo:
    :param ind:
    :return:
    """

    # Stop if
    if ind > len(A)-1:
        return 0

    if ind not in memo:
        memo[ind] = max(masseuse_memo(A, memo, ind + 2) + A[ind], masseuse_memo(A, memo, ind + 1))

    return memo[ind]


def masseuse_dynamic(A):
    """
    Return the max with memo
    :param A:
    :return:
    """

    # Still O(N) space
    memo = [0 for i in range(len(A)+2)]
    for i in range(len(A)-1, -1, -1):
        step2 = A[i] + memo[i+2]
        step1 = memo[i+1]
        memo[i] = max(step1, step2)

    one = 0
    two = 0
    for i in range(len(A)):
        step2 = A[i] + two
        step1 = one
        tmp = max(step1, step2)
        two = one
        one = tmp

    return memo


if __name__ == '__main__':
    A = [30, 15, 60, 75, 45, 15, 15, 45]
    # Recursion: O(2^n)
    print(masseuse(A))

    # Memo: O(n) space and time
    memo = {}
    masseuse_memo(A, memo)
    print(memo)

    # Dynamic: O(n) time and space O(1)
    print(masseuse_dynamic(A))

    # Return also appointments
    appointments = []
    masseuse2(A, appointments)
    for i, v in appointments[::-1]:
        print("Appointments:{}, Sum: {}".format(A[i], v+A[i]))
