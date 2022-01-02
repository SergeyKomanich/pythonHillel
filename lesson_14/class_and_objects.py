"""
class ClassName(ParentName1, ParentName2 ...):
    body_class

class ClassName:
    body_class
"""


class Point:
    A = 10
    B = 11
    name = 'Point'

    def __init__(self, x=0, y=0):
        if 5 <= x <= 10:
            self.x = x
        else:
            self.x = x % 10
        self.y = y

    def setX(self, x):
        if 5 <= x <= 10:
            self.x = x

    def getX(self):
        return self.x

    def __gt__(self, other):
        if self.x > other.x and self.y > other.y:
            return True
        else:
            return False

    def __add__(self, other):
        return Point(self.x+other.x, self.y+other.y)

    def __str__(self):
        return f'x = {self.x}, y = {self.y}'

    def show(self):
        print(f'Point({self.x}, {self.y})')

    @staticmethod
    def mult(i, j):
        return i + j



pt = Point(6, 5)
print(pt.x)
pt.x = 4
print(pt.A)
Point.A = 23
print(Point.A)
print(pt.x)
pt1 = Point()
pt2 = Point()
print(pt1.A)
print(pt2.A)
print(type(pt1), type(pt2))
print(id(pt1), id(pt2))

print(pt.A)
print(pt1.A)
print(pt2.A)
pt.A = 45
print(pt.A)
print(pt1.A)
print(pt2.A)
print(Point.A)

pt.B = 88
print(dir(Point))
print(dir(pt))
print(dir(pt1))


class T:
    """
    Instance of class T
    """

    def func(self):
        self.d = 9


t = T()
print(dir(T))
print(dir(t))
print(T.__dict__)
print("t", t.__dict__)

pt1.x = 3
pt1.y = 2
print(pt1.x, pt1.y)
print(pt2.x, pt2.y)
print(pt1 > pt2)

pt3 = pt1 + pt2
print(pt3.x, pt3.y)
print(pt3)

pt4 = Point(pt1.x+pt2.x, pt1.y+pt2.y)
print(pt4)
pt4.show()
print(pt4.mult(4, 5))
print(Point.mult(6, 7))
