# task 1
# range(start: end(-1) : step-over(1))

r1 = range(0)
print(r1)  # range(0, 0)

r2 = range(5)
print(r2)  # range(0, 5)

r3 = range(0, 5)

# objects: list, tuple, set, dict
print(list(r3))  # [0, 1, 2, 3, 4]
print(tuple(r3))  # (0, 1, 2, 3, 4)
print(set(r3))  # {0, 1, 2, 3, 4}
# print(dict(r3))  # TypeError: cannot convert dictionary update sequence element #0 to a sequence

r4 = range(10, 1, -1)
print(list(r4))  # [10, 9, 8, 7, 6, 5, 4, 3, 2]

r4 = range(1, 10, 1)
print(list(r4))  # [1, 2, 3, 4, 5, 6, 7, 8, 9]


l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#     0  1  2  3  4  5  6  7  8, 9  # positive index
#    -10 -9 -8 -7 -6 -5 -4 -3 -2 -1  # negative index
print(l1[::1])
print(l1[::-1])


