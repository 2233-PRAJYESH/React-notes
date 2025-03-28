# Advanced Functions
# Create an Inner Function
# Create a Higher Order Function (Pre: Functions, Inner Function)
# Create a Closure
# Create a Decorator

# Create an Inner Function without arguments
# Task 1:
# def d1():
#
#     print("d1 function is outer function")
#
#     def d2():
#
#         print("d2 function is inner function")
#
#     d2()
#
#
# d1()

# Task 2:
# def d1(a, b):
#
#     def d2():
#
#         print(a + b, a-b, a*b, a/b)
#
#     d2()
#
#
# d1(10, 20)  # 30 -10 200 0.5

# Higher Order Function takes as an argument(1) or returns a function(1)
# Task 1: Function as argument
# def d1(a):
#
#     return a, a, a
#
#
# print(d1(10))

# def d1(para1):
#
#     return "d1 function", para1
#
#
# print(d1(10))  # ('d1 function', 10)

# sai ram
# sai ram you need to call sai kiran function
# def d1(para1, para2):
#
#     return "d1 function",  para1, para2
#
#
# # sai kiran
# def d2():
#
#     return "d2 function"
#
#
# # sai kumar
# def d3():
#
#     return "d3 function"
#
#
# # sa ram is calling sai kiran function as argument
# d = d1(d2(), d3())
# print(d)  # ('d1 function', 'd2 function', 'd3 function')

# Task 2: Function as argument
# def d1(a):
#
#     return a
#
#
# def d2(x, y):
#
#     return print(x + y)
#
#
# d1(d2(10, 20))

# Task 3: returns a function
# def parent():
#     print("parent need to give permission to child")
#
#     def child():
#         print("child is waiting to get permission")
#
#     return child


# to bring child() function outside I should get permission from parent()
# by pass a variable to parent() we access child() function
# that variable will point to child directly
# p = parent()
# p()
# print(p.__name__)

# Task 4: returns a function with arguments
# def d1(a, b):
#
#     def d2():
#
#         return a + b
#
#     return d2
#
#
# d = d1(10, 20)
# print(d())
# print(d.__name__)

# Task 5:
def d1(x):
    def d2(y):
        def d3(z):

            return x + y + z
        return d3
    return d2


d = d1(10)
dd = d(20)
ddd = dd(30)
print(ddd)

d = d1(10)(20)(30)
print(d)
