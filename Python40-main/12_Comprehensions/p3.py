# Dict Comprehension
d = {i: i*i for i in range(1, 10)}
print(d)


d = dict((x, x*x) for x in range(1, 10))
print(d)

d = dict()
for i in range(1, 10):
    d[i] = i*i
print(d)
