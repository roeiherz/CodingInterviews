__author__ = 'roeiherz'

"""
You are building a diving board by placing a bunch of planks of wood end-to-end.
There are two types of planks, one of length *shorter* and one of length *longer*. 
You must use exactly K planks of wood. Write a method to generate all possible lengths for the diving board. 
"""


def diving_board(k, mapp, short=0, long=0):

    if k > K:
        return 1

    if k not in mapp:
        mapp[k] = [(short, long)]
    elif (short, long) not in mapp[k]:
        mapp[k].append((short, long))
    return diving_board(k+1, mapp, short+1, long) + diving_board(k+1, mapp, short, long+1)


def diving_board_eff():
    lst = []
    for i in range(K):
        if (i, K-i) not in lst:
            lst.append((i, K-i))
        if (K-i, i) not in lst:
            lst.append((K-i, i))
    print lst


if __name__ == '__main__':
    K = 10
    mapp = {}
    diving_board_eff()
    diving_board(0, mapp)
    print(mapp[K])
