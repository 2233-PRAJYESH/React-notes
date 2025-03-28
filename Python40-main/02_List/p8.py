# count(), : finding the same occurrences
# clear(), sort()
l1 = [10, 20, 30, 40, 50, 10, 20, 30, 10, 20]
print(l1.count(10))

print(l1.count(50))

print(l1.count(100))

l1.clear()  # clear the entire list
print(l1)

# sort()
l1 = ['b', 'e', 'a', 'c', 'd']
# insertion order
print(l1)  # ['b', 'e', 'a', 'c', 'd']
l1.sort(reverse=False)
print(l1)  # ['a', 'b', 'c', 'd', 'e']
l1.sort(reverse=True)
print(l1)

