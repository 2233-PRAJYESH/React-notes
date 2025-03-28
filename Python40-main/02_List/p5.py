# task 4: create a copy of list copy()
import copy

l1 = [10, 20, 30, 40, 50]
print(l1)  # [10, 20, 30, 40, 50]
print(l1.copy())  # [10, 20, 30, 40, 50]
print(l1[:])  # [10, 20, 30, 40, 50]

# task 5: diff b/w deep copy and shallow copy
# deep copy: the original list will not change
# shallow copy: the original list will change

print(copy.copy(l1))  # [10, 20, 30, 40, 50]
# deepcopy
list1 = [[1, 2], [3, 4]]
list2 = copy.deepcopy(list1)
# modify
list2[0][0] = 10
print(list2)  # [[10, 2], [3, 4]]
print(list1)  # [[1, 2], [3, 4]]   # the original list will not change

# shallow-copy
list3 = [[1, 2], [3, 4]]
list4 = copy.copy(list3)
# modify
list4[0][0] = 10
print(list4)  # [[10, 2], [3, 4]]
print(list3)  # [[10, 2], [3, 4]]  # the original list will change

l1 = [[10, 20, 30, 40], [100, 200, 300, 400]]
#      0   1   2   3       0   1    2    3
#            0                      1
print(l1[0][3])
print(l1[1][2])
