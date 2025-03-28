# Task 2: In abc class can we create object / no
from abc import ABC, abstractmethod


class Test(ABC):

    @abstractmethod
    def d1(self):

        pass

    def d2(self):

        print("d2 method")


# Test().d1()  # TypeError: Can't instantiate abstract class Test without an implementation for abstract method 'd1'
# Test().d2()
# Test()  # TypeError: Can't instantiate abstract class Test without an implementation for abstract method 'd1'

