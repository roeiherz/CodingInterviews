__author__ = 'roeiherz'

"""
A child is running up a staircase with n steps and can hop either 1 step, 2 steps or 3 steps at a time.
Implement a method to count how many possible ways the child can run up the stairs.
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
