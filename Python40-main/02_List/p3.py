# task 2: diff b/w pop() and remove()
# pop()
l2 = [10, 20, 30, 40, 50]
print(l2.pop())  # 50
print(l2)  # [10, 20, 30, 40]
print(l2.pop())  # 40
print(l2)  # [10, 20, 30]
print(l2.pop())  # 30
print(l2)  # [10, 20]

# pop(index)
l3 = [10, 20, 30, 40, 50]
#      0   1   2   3   4
l3.pop(2)
print(l3)  # [10, 20, 40, 50]

# remove(element)
l4 = [10, 20, 30, 40, 50]
#     e1  e2  e3  e4  e5
#     i1  i2  i3  i4  i5
l4.remove(30)
print(l4)  # [10, 20, 40, 50]

# git s/w (bridge b/w local system and remote server(https://github.com/SajeedAI/Python40))
# github (store the code)
# push (username and passsword of github)