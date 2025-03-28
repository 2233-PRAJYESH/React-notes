# task 6: update()
s1 = {10, 20, 30, 40, 50, 60, 70, 80}
print(s1)  # {70, 40, 10, 80, 50, 20, 60, 30}
s1.update({90, 100, 110, 120})
print(s1)  # {100, 70, 40, 10, 110, 80, 50, 20, 120, 90, 60, 30}

s2 = {"NameOne", "NameTwo", "NameThree", "NameFour"}
s3 = {10, 20, 30, 40, 50}
s2.update(s3)
print(s2)  # {'NameTwo', 40, 10, 50, 'NameOne', 20, 'NameThree', 'NameFour', 30}
