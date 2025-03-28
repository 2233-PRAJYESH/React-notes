# task 3: insert() the data in b/w
l1 = [10, 20, 30, 40, 50]
#      0   1   2   3   4
l1.insert(2, ["NameOne", "NameTwo"])
print(l1)  # [10, 20, ['NameOne', 'NameTwo'], 30, 40, 50]

l2 = [10, 20, 30, 40, 50]
l2.insert(3, 300)
print(l2)  # [10, 20, 30, 300, 40, 50]

l3 = [10, 20, 30, 40, 50, 60, 70]
l3.insert(4, [400, 500])
print(l3)

l4 = []
l4.insert(0, [l1, l2, l3])
print(l4)   # [[[10, 20, ['NameOne', 'NameTwo'], 30, 40, 50], [10, 20, 30, 300, 40, 50], [10, 20, 30, 40, [400, 500], 50, 60, 70]], ' ']
