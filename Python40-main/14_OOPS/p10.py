# method overriding
# two classes use inheritance and same methods and same arguments
class parent:

    def d1(self, a, b):
        print("parent: ", a, b)


class child(parent):

    def d1(self, a, b):
        print("child: ", a, b)


c = child()
c.d1(10, 20)

# implementation
# f/m
