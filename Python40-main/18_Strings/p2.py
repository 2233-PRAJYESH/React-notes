# string methods
# task 1:
# split() : string to list of elements
s1 = "Hello World Hello Python"
print(s1.split())  # ['Hello', 'World', 'Hello', 'Python']

# task 2:
# s1 = "Hello Python"
# print(s1.split(''))  # ValueError: empty separator

s2 = "HelloPython"
print(s2.split(' '))  # ['HelloPython']

s2 = 'Hello Python'
print(s2.split(' '))  # ['Hello', 'Python']

# task 3:
mobiles = "Nokia:Samsung:Lg:Moto"
print(mobiles.split(":"))  # ['Nokia', 'Samsung', 'Lg', 'Moto']

colors = "red-black-blue-green-yellow-orange-pink"
print(colors.split('-'))  # ['red', 'black', 'blue', 'green', 'yellow', 'orange', 'pink']

programming = "javaandpythonandphpandruby"
print(programming.split('and'))  # ['java', 'python', 'php', 'ruby']

# task 4: max split
programming = "java and python and php and ruby"
print(programming.split(' ', 1))  # ['java', 'and python and php and ruby']

# task 5:
mobiles = ['Nokia', 'Samsung', 'Lg', 'Moto']
print(':'.join(mobiles))  # Nokia:Samsung:Lg:Moto

print(','.join(mobiles))  # Nokia,Samsung,Lg,Moto

print(''.join(mobiles))  # NokiaSamsungLgMoto

# task 6: pass numbers in join()
# lst = [1, 2, 3, 4, 5]
# print(','.join(lst))  # TypeError: sequence item 0: expected str instance, int found

# lst = ['1', '2', '3', '4', '5']
# print(','.join(lst))  # 1,2,3,4,5












