# task 5: find the index position of the list
# index(element)
l1 = [10, 20, 30, 40, 50]
#      0   1   2   3   4
print(l1.index(10))

# index(element, start, end)
l1 = [10, 20, 30, 40, 50, 60, 70, 10, 20, 80, 90, 10, 20]
#     0    1   2   3   4   5   6   7   8   9  10  11  12
print(l1.index(10, 5))
print(l1.index(10, 9))
