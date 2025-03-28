# insert the data without insert()
l1 = [10, 20, 30, 40, 50, 60, 70, 80, 90]
#      0   1   2   3   4   5   6   7   8

print(l1)

l1[3] = 300
l1[4] = 400
l1[5] = 500

print(l1)

l1[3: 6: 1] = 1000, 2000, 3000
print(l1)
