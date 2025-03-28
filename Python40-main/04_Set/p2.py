# task 1: Add the data in Set, But we may not expect the order
s1 = {10, 20, 30, 40, 50}
print(s1)  # {50, 20, 40, 10, 30}

s1.add(60)
print(s1)  # {50, 20, 40, 10, 60, 30}

s1.add(70)
print(s1)  # {50, 20, 70, 40, 10, 60, 30}

s2 = {100, 200, 300, 400, 500}
s2.add(s1)
print(s2)  # TypeError: unhashable type: 'set'




