# multi level
class grand_parent:

    # instance method
    def d1(self):
        print("d1 instance method")

    # static method
    @staticmethod
    def d2():
        print("d2 static method")

    # class method
    @classmethod
    def d3(cls):
        print("d3 class method")


class parent(grand_parent):

    def d4(self):
        print("d4 instance method")


class child(parent):

    def d5(self):

        print("d5 instance method")


c = child()
c.d5()
c.d4()
c.d3()
c.d2()
c.d1()


