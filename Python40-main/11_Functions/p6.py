# closures are even higher oder functions
# closures rely on nested function
# The inner function uses variable that are defined in the outer function. These are called as free variables
# Even after the outer function has completed its execution, the inner function retains access to the free variables

# Task 1:
# def d1():
#     x = 10
#     print('d1 scope: ', x)
#
#     def d2():
#         y = 20
#         print('d2 scope: ', x)
#         print('d2 scope: ', y)
#
#     return d2
#
#
# d = d1()
# d()
# print("Before")
# d()
# del d1
# print('After')
# d()

# Task 2
# def d1():
#
#     a = 10
#     print(a)
#
#
# d = d1
# d()
# print(d.__closure__)

# Task 3:
def d1(a, b):
    c = 30
    d = 40
    print("Scope d1: ", d)

    def d2():

        print('Scope d2: ', a)
        print('Scope d2: ', b)
        print('Scope d2: ', c)
        print(hex(id(a)), hex(id(b)), hex(id(c)))  # 0x1066399c0 0x106639b00 0x106639c40

    return d2


d = d1(10, 20)
d()
print(d.__closure__)
print(d.__code__.co_freevars)  # ('a', 'b', 'c')
# (<cell at 0x104e42c80: int object at 0x1066259c0>, <cell at 0x104e42ce0: int object at 0x106625b00>, <cell at 0x104e42cb0: int object at 0x106625c40>)

# Task: Need to Log in and Logout, Use if else and input function based on Decorator






