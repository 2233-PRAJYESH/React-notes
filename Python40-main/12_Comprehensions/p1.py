# Comprehension: Creating new data from the existing data
# List Comprehension
# Set Comprehension
# Dict Comprehension
# Generator Comprehension

# Task 1: Find the range using list()
l1 = list(range(1, 10))
print(l1)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Task 2: Find the square root without list comprehension
for i in list(range(1, 10)):

    print(i ** 2, end=" ")  # 1 4 9 16 25 36 49 64 81

print('')
# Task 3: Find the square root with list comprehension
# syntax: [expression for item in iterable]
l1 = [i**2 for i in list(range(1, 10))]
print(l1)  # [1, 4, 9, 16, 25, 36, 49, 64, 81]

# syntax: [expression for item in iterable]
l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
l1 = [i**2 for i in l]
print(l1)  # [1, 4, 9, 16, 25, 36, 49, 64, 81]

# syntax: [expression for item in iterable if condition]
squares = [i ** 2 for i in list(range(1, 20)) if i % 2 == 0]
print(squares)  # [4, 16, 36, 64, 100, 144, 196, 256, 324]

# syntax: [expression for item in iterable if condition if condition]
l1 = [i for i in range(50) if i % 2 == 0 if i % 5 == 0]
print(l1)  # [0, 10, 20, 30, 40]

# syntax: [expression if condition else condition for element in iterable]
names = ["admin", "admin", "admins", "admin"]
l1 = [i if i == "admin" else "not admin" for i in names]
print(l1)  # ['admin', 'admin', 'not admin', 'admin']

# syntax: [expression for element in iterable, for element in iterable]
l1 = [x+y for x in [10, 20, 30] for y in [100, 200, 300]]
print(l1)  # [110, 210, 310, 120, 220, 320, 130, 230, 330]

# without-compression
l1 = []
for x in [10, 20, 30]:
    for y in [100, 200, 300]:
        l1.append(x + y)

print(l1)  # [110, 210, 310, 120, 220, 320, 130, 230, 330]


