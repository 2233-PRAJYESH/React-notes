from abc import ABC, abstractmethod


class test(ABC):

    @abstractmethod
    def d1(self):
        pass

    @abstractmethod
    def d2(self):
        pass

    @abstractmethod
    def d3(self):
        pass

    @abstractmethod
    def d4(self):
        pass


class test_impl(test):

    def d1(self):
        print("d1 method")

    def d2(self):
        print("d2 method")

    def d3(self):
        print("d3 method")

    def d4(self):
        print("d4 method")


test_impl().d1()
