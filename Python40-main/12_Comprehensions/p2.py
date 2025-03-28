# Set Comprehension
# syntax: {expression for i in iterable}

squares = {i ** 2 for i in set(range(1, 10))}
print(squares)  # {64, 1, 4, 36, 9, 16, 49, 81, 25}

squares = {i**2 for i in set(range(1, 10)) if i % 2 == 0}
print(squares)  # {16, 64, 4, 36}

