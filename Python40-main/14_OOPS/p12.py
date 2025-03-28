# Task 1: abs class contains concrete methods and abs methods
from abc import ABC, abstractmethod


# inheritance, method overriding, abs
class Parent(ABC):

    # instance method (abs methods)
    @abstractmethod
    def display(self):
        pass

    # instance method (concrete method)
    def get_data(self):
        print("get method")


class Child(Parent):

    def display(self):
        print("display method")


c = Child()
c.display()
c.get_data()
