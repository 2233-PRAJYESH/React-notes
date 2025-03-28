# tuple vs list
# un safe data
l1 = [10, 20, 30, 40, 50, 60, 70]
l1[0] = 100
print(l1)

# safe data
t1 = (10, 20, 30, 40, 50, 60, 70)
t1[0] = 100
print(t1)  # TypeError: 'tuple' object does not support item assignment
