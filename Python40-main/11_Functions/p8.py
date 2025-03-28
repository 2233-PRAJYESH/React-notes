# Task 1:
# Syntax: lambda arguments: expression
# Normal Function
# def d1(a):
#
#     print(a)
#
#
# d1(5)

# Lambda Function
# d1 = lambda a: print(a)
# d1(5)

# Task 2:
# Normal Function
# def d2(a, b):
#
#     return print(a*b, a+b, a-b, a/b)
#
#
# d2(10, 5)


# d2 = lambda a, b: print(a*b, a+b, a-b, a/b)
# d2(10, 5)

# Task 3: Assign lambda function to a variable
# l1 = lambda a, b: a + b
# l = l1(10, 20)
# print(type(l1))
# print(l)
# print(type(l))

# Task 4: arbitrary arguments *, **
# l1 = lambda *a: print(a)
# l1(10, 20, 30, 40, 50)

# l2 = lambda **a: print(a)
# l2(a=10, b=20, c=30, d=40, e=50)

# Task 5: HOF
# def d1(a=10):
#     def d2(b):
#         return a + b
#
#     return d2
#
#
# d = d1()
# print(d(20))
#
# l1 = lambda a = 10: lambda b: a+b
# l = l1()
# print(l(20))

# Task 6: lambada using if else
l1 = lambda a, b: a if a > b else b
print(l1(5, 10))
print(l1(10, 5))


def d1(a, b):
    if a > b:
        return a
    else:
        return b


d = d1(10, 5)
print(d)
