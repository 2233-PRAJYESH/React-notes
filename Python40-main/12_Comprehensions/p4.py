# Generator Comprehension
squares = (i ** 2 for i in tuple(range(1, 10)))
print(squares)  # <generator object <genexpr> at 0x1008ec450>

print(tuple(squares))  # (1, 4, 9, 16, 25, 36, 49, 64, 81)

