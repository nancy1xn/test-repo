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
# 1. (Done)Fix naming convention according following PEPs.
#    https://peps.python.org/pep-0008/#naming-conventions
# 2. What is exception? What is the common error handling in Python?
# 當執行時遇到error, 其檢測到的error就是例外 ex:Syntactical Error/Logical error/Run Time Error

# Common error handling-Except Handling:try to execute the statement, otherwise we'll print except block (only when we have an error)
a = 5
b = 0
try:
    print("Open")
    print(a/b)    
    k = int(input("Please enter a number"))
    print(k)

except ZeroDivisionError as e:
    print("You cannot divided zero")

except ValueError as e:
    print("You cannot enter value other than integer")

except Exception as e:
    print("Something went wrong")

finally:
    print("Bye")

# 3. Can Shape class still be instanciated? If so, how to make it raise exception when the user try to instanciate?

#Shape class cann't be instanciated b/c it is a abstract class. Regarding how to make it raise exception, please find as follows:


# 4.
def division_20_by(x) -> float:
    # TODO - 2
    # hint: what is try-except block
    try: 
        return 20 / x

    except ZeroDivisionError as e:
        print("You can't divide zero")

Object3 = division_20_by(0)
print(Object3)
#!Your indentation should be within the function. Correct answer would be following code. Please review and document all your unknowns.

if __name__ == "__main__":
    # TODO - 1
    object1 = Square(3)
    answer1 = object1.area()
    print(answer1)

    object2 = Rectangle(3, 4)
    answer2 = object2.area()
    print(answer2)

    # TODO - 3
    # Try to make following expression raise exception
    
    from abc import ABC, abstractmethod
    class Shape(ABC):
        def area(self):
            pass
        try:
            object4 = Shape(ABC)
            print(object4)

        except TypeError as e:
            print("Shape class cann't be instanciated")


