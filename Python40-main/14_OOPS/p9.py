# constructor overloading
# one class with same methods but arguments must be different
# what is special method /constructor
# __int__():
# special method is executed at the time object creation
from multipledispatch import dispatch


class Product:

    # methods
    @dispatch(int, int)
    def __init__(self, a, b):

        print(a, b)

    @dispatch(int, int, int)
    def __init__(self, a, b, c):

        print(a, b, c)


# object (object name and class name must be same)
Product(10, 20)
Product(10, 20, 30)



