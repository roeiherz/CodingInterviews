__author__ = 'roeiherz'

"""
Write a function to swap a number in place (that is, without temporary variables).
"""


def number_swapper(x, y):
    print("X:{}, Y:{}".format(x, y))
    y = x+y  # 3+5
    x = y-x  # 8-3
    y = y-x  # 8-5
    print("X:{}, Y:{}".format(x, y))


if __name__ == '__main__':
    number_swapper(3, 5)
