# task 1: diff b/w append() and extend()
l1 = [10, 20, 30, 40, 50]
print(l1)  # [10, 20, 30, 40, 50]

l1.append("NameOne")
print(l1)  # [10, 20, 30, 40, 50, 'NameOne']

l1.append("NameTwo")
l1.append("NameThree")
l1.append("NameFour")
print(l1)  # [10, 20, 30, 40, 50, 'NameOne', 'NameTwo', 'NameThree', 'NameFour']


l2 = [10, 20, 30, 40, 50]
print(l2)  # [10, 20, 30, 40, 50]
l2.extend(["NameOne", "NameTwo", "NameThree", "NameFour"])
print(l2)
