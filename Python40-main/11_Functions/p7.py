# Decorator
# Task 1: Normal Function
# def d1(func):
#
#     print(func)
#
#
# d1("Hello Python")
# d = d1
# print(d.__name__)  # d1
# d("Hello Java")

# Task 2
# def d1(func):
#
#     def d2():
#
#         return "Hello Java", func()
#
#     return d2
#
#
# @d1
# def d3():
#
#     return "Hello Python"
#
#
# # d = d1(d3)
# # print(d())
#
# print(d3())

# Task 3:
def d1(func):

    def d2(a, b):

        return func(a+b)

    return d2


@d1
def d3(c):

    return c


# c = a + b

d = d3
print(d(10, 20))


def d4(c):

    return c


d = d1(d4)
print(d(10, 20))

















