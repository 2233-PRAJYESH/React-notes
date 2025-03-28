# task 4: diff b/w remove() and discard()
# remove() will throw the error if the element doesn't exist
s1 = {10, 20, 30, 40, 50}
s1.remove(20)
print(s1)  # {50, 40, 10, 30}

# s1.remove(60)  # KeyError: 60

# discard() will not throw any error if the element doesn't exist
s2 = {10, 20, 30, 40, 50}
s2.discard(20)
print(s2)  # {50, 40, 10, 30}

s2.discard(60)
print(s2)




