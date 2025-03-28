# list
# we can create list using square bracket [], and object list()
# it will maintain order, and also it allows duplicates
# in list we can store any data types
# in list all the items/elements we store them in index based position (index starts from 0)

# task 1: insertion order, duplicates
l1 = [10, 20, 30, 40, 10, 50, 60, 20, 70, 80]
print(l1)  # [10, 20, 30, 40, 10, 50, 60, 20, 70, 80]

l1 = list([10, 20, 30, 40, 10, 50, 60, 20, 70, 80])
print(l1)  # [10, 20, 30, 40, 10, 50, 60, 20, 70, 80]

# task 2: in list we store any data type
l2 = [10, 10.0, True, 10j, 'NameOne']
print(l2)

# task 3: find the element using index position
l3 = [10, 20, 30, 40, 10, 50, 60, 20, 70, 80]
#      0   1   2   3   4   5   6   7   8   9
print(l3[6], l3[3])  # 60 40

# task 4: find the length of the list
l4 = [10, 20, 30, 40, 10, 50, 60, 20, 70, 80]
#      0   1   2   3   4   5   6   7   8   9  : index
#      1   2   3   4   5   6   7   8   9   10 : length
print(len(l4))  # 10

# task 5: best practices
# when we pass data type it will return the class name
# when we pass object it will return default value
l5 = [int, float, bool, complex, str, list, tuple, set, frozenset, dict, bytes, bytes, range]
print(l5)  # [<class 'int'>, <class 'float'>, <class 'bool'>, <class 'complex'>, <class 'str'>, <class 'list'>, <class 'tuple'>, <class 'set'>, <class 'frozenset'>, <class 'dict'>, <class 'bytes'>, <class 'bytes'>, <class 'range'>]

l6 = [int(), float(), complex(), str(), list(), tuple(), set(), frozenset(), dict()]
print(l6)  # [0, 0.0, 0j, '', [], (), set(), frozenset(), {}]

# task 6: can you multiply both list given
l1 = [10, 20, 30, 40, 50]
l2 = [10, 20, 30, 40, 50]
# print(l1 * l2)  # TypeError: can't multiply sequence by non-int of type 'list'

# task 7: can you multiply the given list by any value
# repetition
l7 = [10, 20, 30, 40, 50]
print(l7 * 1)  # [10, 20, 30, 40, 50]
print(l7 * 2)  # [10, 20, 30, 40, 50, 10, 20, 30, 40, 50]
print(l7 * 3)  # [10, 20, 30, 40, 50, 10, 20, 30, 40, 50, 10, 20, 30, 40, 50]

# task 8: can you add both list given
# concatenation
l8 = [10, 20, 30, 40, 50]
l9 = [10, 20, 30, 40, 50]
print(l8 + l9)  # [10, 20, 30, 40, 50, 10, 20, 30, 40, 50]

# task 9 : how to get the half portion of the data from list
# slicing
# variable[start(0): end(-1) : step-over(1)]
l9 = [10, 20, 30, 40, 50, 10, 20, 60, 70, 80, 90]
#      0   1   2   3   4   5   6   7   8   9  10  11  12...
print(l9[0: 5: 1])  # [10, 20, 30, 40, 50]
print(l9[0: 5])  # [10, 20, 30, 40, 50]

print(l9[4: 8: 1])  # [50, 10, 20, 60]

l9 = [10, 20, 30, 40, 50, 10, 20, 60, 70, 80, 90]
print(l9[::2])  # [10, 30, 50, 20, 70, 90]
print(l9[::3])  # [10, 40, 20, 80]

print(l9[4:])  # [50, 10, 20, 60, 70, 80, 90]

# same copy
print(l9)
print(l9[::1])

# Task 10: perform slicing on negative numbers

# Diff b/w list and tuple
# Task 11: list is mutable/ unsafe
l11 = [10, 20, 30, 40, 50]
l11[0] = 100
l11[1] = 200
print(l11)  # [100, 200, 30, 40, 50]

# Task 12: tuple is immutable/ safe
l12 = (10, 20, 30, 40, 50)
l12[0] = 100
print(l12)  # TypeError: 'tuple' object does not support item assignment





















