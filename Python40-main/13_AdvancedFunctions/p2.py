# generators
# By using generators we can create our own iterations
# In generator we use yield keyword
# In generator we don't use return keyword, if we use return keyword it will terminate the function

# Task 1:
# def d1():
#     return 10
#     return 20   # This code is unreachable
#     return 30   # This code is unreachable
#
#
# d = d1()
# print(d)  # 10


# Task 2:
# def d2():
#     yield 10
#     yield 20
#     yield 30
#
#
# d = d2()
# print(d)  # <generator object d2 at 0x1007b4880>
# print(next(d))
# print(next(d))
# print(next(d))
# print(next(d))  # StopIteration

# def d3():
#     yield 10
#     return 20  # StopIteration: 20
#     yield 30
#
#
# d = d3()
# print(d)  # <generator object d2 at 0x1007b4880>
# print(next(d))
# print(next(d))
# print(next(d))

def d4(n):
    for i in range(n):
        yield i


d = d4(50)
print(next(d))
print(next(d))
print(next(d))
print(next(d))
print(next(d))




