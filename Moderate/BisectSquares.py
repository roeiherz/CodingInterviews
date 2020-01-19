__author__ = 'roeiherz'

# todo

"""
Given two squares on a two-dimensional plane, find a line that would cut these two squares in half.
Assume that the top and the bottom sides of the square run parallel to the x-axis.
"""


class Square:
    def __init__(self, top, buttom):

        if not isinstance(top, tuple) or not isinstance(buttom, tuple):
            raise Exception

        self.top = top
        self.buttom = buttom


def bisect_squares(A, B):
    # Sort arrays
    print("Smallest Diff {}")


if __name__ == '__main__':
    A = Square(top=(4, 3), buttom=(5, 2))
    B = Square(top=(5, 3), buttom=(4, 2))
    bisect_squares(A, B)
