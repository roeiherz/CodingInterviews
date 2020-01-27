__author__ = 'roeiherz'

"""
Write a method to return all subsets of a set
"""


def triple_step(n=2):
    # Stop case
    if n < 0:
        return 0

    if n == 0:
        return 1

    return triple_step(n - 3) + triple_step(n - 2) + triple_step(n - 1)


def triple_step_memo(mem, n=2):
    # Stop case
    if n < 0:
        return 0

    if n in mem:
        return mem[n]
    else:
        mem[n] = triple_step_memo(mem, n - 3) + triple_step_memo(mem, n - 2) + triple_step_memo(mem, n - 1)
        return mem[n]


if __name__ == '__main__':
    # print(triple_step(4))
    mem = {0: 1}
    print(triple_step_memo(mem, 4))
    print(triple_step_memo(mem, 37))
