# inheritance: acquiring the properties from one class to other class
# types: single, multiple, multi-level, hybrid, hierarchical

# do python support all the inheritances : yes
# self: self is an object, which was present in constructor and instance method as argument
class parent:

    # instance method
    def get_id(self):  # self is an object in instance method

        print("get_id  instance method")


class child(parent):

    # instance method
    def update_id(self):  # self is an object in instance method

        print("update_id instance method")


# creating the object for child class,
# class name and object name must be same
# c is reference variable
c = child()  # object
c.get_id()
c.update_id()
