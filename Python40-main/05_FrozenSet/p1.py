# task 1:
# list (mutable) and tuple (immutable)
# set (mutable) and frozenset (immutable)
# In set we can modify the data, and in frozenset we cannot modify the data
# In set we can add frozenset, but in frozenset you cannot add set
s1 = {10, 20, 30, 40, 50, 60, 70}

f1 = frozenset({100, 200, 300, 400, 500})

s1.add(f1)
print(s1)  # {frozenset({400, 100, 500, 200, 300}), 50, 20, 70, 40, 10, 60, 30}

s1.remove(f1)
print(s1)  # {50, 20, 70, 40, 10, 60, 30}

# immutable
f1.add(s1)  # AttributeError: 'frozenset' object has no attribute 'add'



