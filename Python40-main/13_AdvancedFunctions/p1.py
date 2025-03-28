# Iterables
# a = 10
# for i in a:
#     print(a)  # TypeError: 'int' object is not iterable

# b = 10.5
# for i in b:
#     print(i)  # TypeError: 'float' object is not iterable

# string is an iterable
# c = "hello python"
# for i in c:
#     print(i)

# list is an iterable
# l1 = [10, 20, 30, 40, 50]
# for i in l1:
#     print(i)

# what is iterable / iterator /
# iterator is an object contains two methods iter() and next() method
# l1 = [10, 30, 30, 40, 50]
# print(l1.__iter__())  # <list_iterator object at 0x10469eb30>
# print(dir(l1))

# ['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__',
#  '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__',
#  '__getstate__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__',
#  '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__',
#  '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__',
#  '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend',
#  'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

l = [10, 30, 30, 40, 50]
print(l.__iter__())  # <list_iterator object at 0x10469eb30>
l1 = l.__iter__()
print(l1.__next__())
print(l1.__next__())
print(l1.__next__())
print(l1.__next__())
print(l1.__next__())
# print(l1.__next__())  # StopIteration

# 10
# 30
# 30
# 40
# 50

l = [10, 20, 30, 40, 50]
l1 = iter(l)
print(next(l1))
print(next(l1))
print(next(l1))
print(next(l1))
print(next(l1))
# print(next(l1))  # StopIteration
# 10
# 20
# 30
# 40
# 50

for i in l:
    print(i)

# 10
# 30
# 30
# 40
# 50

l1 = [10, 20, 30, 40, 50]
result = iter(l1)
while True:

    try:
        element = next(result)
        print(element)
    except StopIteration:
        break

# 10
# 20
# 30
# 40
# 50
