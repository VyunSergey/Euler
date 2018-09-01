class Point2D(object):
    def __init__(self, dx, dy):
        self.x = dx
        self.y = dy

    def __str__(self):
        return '(' + str(self.x) + ', ' + str(self.y) + ')'

    def x_eq(self, other):
        return self.x == other.x

    def y_eq(self, other):
        return self.y == other.y

    def __eq__(self, other):
        return self.x_eq(other) and self.y_eq(other)

    def x_ne(self, other):
        return self.x != other.x

    def y_ne(self, other):
        return self.y != other.y

    def __ne__(self, other):
        return self.x != other.x or self.y != other.y

    def x_gt(self, other):
        return self.x > other.x

    def y_gt(self, other):
        return self.y > other.y

    def __gt__(self, other):
        return self.x_gt(other) and self.y_gt(other)

    def slight_gt(self, other):
        return self.x_gt(other) or self.y_gt(other)

    def x_lt(self, other):
        return self.x < other.x

    def y_lt(self, other):
        return self.y < other.y

    def __lt__(self, other):
        return self.x_lt(other) and self.y_lt(other)

    def slight_lt(self, other):
        return self.x_lt(other) or self.y_lt(other)

    def x_ge(self, other):
        return self.x >= other.x

    def y_ge(self, other):
        return self.y >= other.y

    def __ge__(self, other):
        return self.x_ge(other) and self.y_ge(other)

    def slight_ge(self, other):
        return self.x_ge(other) or self.y_ge(other)

    def x_le(self, other):
        return self.x <= other.x

    def y_le(self, other):
        return self.y <= other.y

    def __le__(self, other):
        return self.x_le(other) and self.y_le(other)

    def slight_le(self, other):
        return self.x_le(other) or self.y_le(other)

    def copy(self):
        return Point2D(self.x, self.y)

    def left(self):
        self.x += -1
        return self

    def right(self):
        self.x += 1
        return self

    def up(self):
        self.y += 1
        return self

    def down(self):
        self.y += -1
        return self


if __name__ == '__main__':
    pnt1 = Point2D(0, 0)
    pnt2 = Point2D(1, 0)
    pnt3 = Point2D(0, 1)
    pnt4 = Point2D(1, 1)

    print(pnt1, pnt2, pnt3, pnt4)

    print('pnt1 < pnt2:', pnt1 < pnt2)
    print('pnt1 <~ pnt2:', pnt1.slight_lt(pnt2))

    print('pnt2 < pnt3:', pnt2 < pnt3)
    print('pnt2 <~ pnt3:', pnt2.slight_lt(pnt3))

    print('pnt3 < pnt4:', pnt3 < pnt4)
    print('pnt3 <~ pnt4:', pnt3.slight_lt(pnt4))

    print('pnt1 < pnt4:', pnt1 < pnt4)
    print('pnt1 <~ pnt4:', pnt1.slight_lt(pnt4))
