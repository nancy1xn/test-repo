from abc import ABC, abstractmethod


class Shape(ABC):
    def area(self):
        pass

    # implement abstract class here


class Square(Shape):
    def __init__(self, l):
        self.l = l

    def area(self):
        return self.l**2

    # area = l^2


class Rectangle(Shape):
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def area(self):
        return self.w * self.h

    # area = w * h


# TODO
# 1. Fix naming convention according following PEPs.
#    https://peps.python.org/pep-0008/#naming-conventions
# 2. What is exception? What is the common error handling in Python?
# 3. Can Shape class still be instanciated? If so, how to make it raise exception when the user try to instanciate?


def division_20_by(x) -> float:
    # TODO - 2
    # hint: what is try-except block
    return 20 / x


if __name__ == "__main__":
    # TODO - 1
    Object1 = Square(3)
    Answer1 = Object1.area()
    print(Answer1)

    Object2 = Rectangle(3, 4)
    Answer2 = Object2.area()
    print(Answer2)

    # TODO - 3
    # Try to make following expression raise exception
    s = Shape()
