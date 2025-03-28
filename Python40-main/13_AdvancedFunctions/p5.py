# reduce(function, iterable)
from functools import reduce

# Task 1
lst = [12, 14, 16, 4, 18]

print(reduce(lambda x, y: x+y, lst))
# 12 + 14 = 26
# 26 + 16 = 42
# 42 + 4 = 46
# 46 + 18 = 64

# Task 2
print(reduce(lambda x, y: x if (x < y) else y, [12, 14, 16, 4, 2, 18]))

