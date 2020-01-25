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
        self.center = self.get_center()

    def get_center(self):
        center_x = self.buttom[0] + (self.buttom[0] - self.top[0]) / 2.
        center_y = self.buttom[1] + (self.buttom[1] - self.top[1]) / 2.
        return (center_x, center_y)


def bisect_squares(A, B):
    # Sort arrays
    center_a = A.center
    center_b = B.center

    if float(center_b[0] - center_a[0]) != 0:
        m = (center_b[1] - center_a[1]) / float(center_b[0] - center_a[0])
        n = center_b[1] - m * center_b[0]
        return (m, n)

    # No m and n since x=5
    return None


if __name__ == '__main__':
    A = Square(top=(4, 3), buttom=(5, 2))
    B = Square(top=(5, 3), buttom=(4, 2))
    bisect_squares(A, B)
