__author__ = 'roeiherz'

"""
Given two straight line segments (represents as a start point and end point), compute the point of intersection, if any.
"""


class Line:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2
        self.m = self.slope()
        self.n = self.get_n()

    def slope(self):

        # X=5
        if self.point1[0] == self.point2[0]:
            return None
        # Y=3
        if self.point1[1] == self.point2[1]:
            return 0
        # Y=mX+N
        return (self.point2[1] - self.point1[1]) / (self.point2[0] - self.point1[0])

    def get_n(self):
        if self.m is None:
            return None
        return self.point1[1] - self.m * self.point1[0]


def find_intersection(line1, line2):
    # both lines are x=5 and x=3; no intersection
    if line1.m is None and line2.m is None:
        return None

    # both lines are y=5 and y=3; no intersection
    if line1.n is None and line2.n is None:
        return None

    # Only one of the lines is x=5; and other y=mx+n
    if line1.m is None:
        x = line1.point1[0]
        y = line2.m * x + line2.n
        return (x, y)
    if line2.m is None:
        x = line2.point1[0]
        y = line1.m * x + line1.n
        return (x, y)

    # Find intersection point
    if line2.m != line1.m:
        x = (line1.n - line2.n) / (line2.m - line1.m)
        y = line2.m * x + line2.n
        return (x, y)
    else:
        return None


if __name__ == '__main__':
    line1 = Line((5, 3), (4, 2))
    line2 = Line((3, 5), (2, 4))
    inter = find_intersection(line1, line2)