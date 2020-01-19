__author__ = 'roeiherz'

"""
Given a two-dimensional graph with points on it, find a line which passes the most number of points.
"""

EPS = 1e-5


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
        return (self.point2[1] - self.point1[1]) / float(self.point2[0] - self.point1[0])

    def get_n(self):
        if self.m is None:
            return None
        return self.point1[1] - self.m * self.point1[0]


def best_line(points):
    mapp = {}
    for i in range(len(points)):
        for j in range(len(points)):
            if i == j:
                continue
            line = Line(points[i], points[j])
            if (line.m, line.n) in mapp or (line.m + EPS, line.n + EPS) in mapp \
                    or (line.m - EPS, line.n - EPS) in mapp:
                mapp[(line.m, line.n)].add(points[i])
                mapp[(line.m, line.n)].add(points[j])
            else:
                ss = set()
                ss.add(points[i])
                ss.add(points[j])
                mapp[(line.m, line.n)] = ss

    for k, v in mapp.items():
        print("Key: {}; Value: {}".format(k, v))


if __name__ == '__main__':
    # N^2 lines comparison
    points = [(3, 3), (2, 2), (1, 1), (-1, 2)]
    points = [(3, 3), (2, 2), (-1, 2)]
    best_line(points)
