# operators
# # arithmetic operators + - * / // ** %
# a = 10
# b = 20
# c = 15
# d = 3
# print(a + b)  # 30
# print(a - b)  # -10
# print(a * b)  # 200
# print(c / d)  # 5.0
# print(c // d)  # 5
# print(c % d)  # 0
# a = 5
# b = 2
# print(a ** b)  # 25

# assignment operators += -= *= /= //= **= %=
# a = 10
# b = 20
# c = 15
# d = 3
# a += 1  # a = a + 1 # a = 10 + 1 # a = 11
# print(a)
#
# b += a  # b = b + a # b = 20 + 11 # b = 31
# print(b)

# comparison operators < > <= >= == !=
# a = 10
# b = 5
# c = 10
# print(a < b)  # False # 10 < 5
# print(a > b)  # True # 10 > 5
# print(a <= c)  # True
# print(a >= c)  # True
# print(a == c)  # True
# print(a != c)  # False
# print(a != b)  # True
# print(a == b)  # False

# logical operators: and or not
# and: both conditions must satisfy
# print(True and True)  # True
# print(True and False)  # False
# print(False and True)   # False
# print(False and False)  # False
# print()
# print(True or True)  # True
# print(True or False)  # True
# print(False or True)   # True
# print(False or False)  # False
# print()
# print(not True)  # False
# print(not False)  # True

# Membership Operators: in, not in
# l1 = [10, 20, 30, 40, 50]
# print(10 in l1)  # True
# print(100 not in l1)  # True
# print(1000 in l1)  # False

# Identity Operators
# is and ==
# is checks reference comparison
# == checks content comparison
l1 = [10, 20, 30, 40, 50]
l2 = [10, 20, 30, 40, 50]
l3 = l1

print(l1 == l2)  # True
print(l3 == l1)  # True

print(l1 is l2)  # False
print(l3 is l1)  # True

print(id(l1), id(l2), id(l3))










