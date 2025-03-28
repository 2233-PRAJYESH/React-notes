# hierarchical
# son, father, grandfather, grandfather ...
# icici bank, axis bank, sbi bank, rbi
class grandparent:

    def d1(self):

        print("d1 method")


class parent(grandparent):

    def d2(self):

        print("d2 method")


class child_one(grandparent):

    def d3(self):

        print("d3 function")


class child_two(grandparent):

    def d4(self):
        print("d3 function")


g = grandparent()
g.d1()

p = parent()
p.d1()  # grandparent
p.d2()  # owned by them,self

c1 = child_one()
c1.d1()  # grandparent
c1.d3()  # owned by them,self

c2 = child_two()
c2.d1()  # grandparent
c2.d4()  # owned by them,self



