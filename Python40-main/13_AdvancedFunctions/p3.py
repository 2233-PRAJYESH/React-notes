# map(function, iterables), filter(function, iterables)

# Task 1:
l1 = [10, 20, 30, 40, 50]


def d1(n):

    return n * 2


m = map(d1, l1)
print(m)  # <map object at 0x100cc2b90>
print(list(m))  # [20, 40, 60, 80, 100]

# Task 2:
l1 = [10, 20, 30, 40, 50]

l = lambda x: x * 2
m = map(l, l1)
print(m)  # <map object at 0x100a72f20>
print(list(m))

# Task 3:
print(list(map(lambda x: x*2, [10, 20, 30, 40, 50])))  # [20, 40, 60, 80, 100]

# Task 4:
print(list(map(lambda a, b: a*b, [1, 2, 3, 4], [1, 2, 3, 4])))  # [1, 4, 9, 16]

