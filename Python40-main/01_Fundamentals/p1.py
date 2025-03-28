# data types in python
# number types: int, float, bool, complex
# string types: str
# sequence types: list, tuple, set, frozenset,
# looping : range
# mapping : dict
# binary type : bytes, bytearray
# null type : None

product_id = 23456   # class int
# product_name = 'eggs'  # class str
product_name = ['eggs', 'banana', 'dates', 'kiwi']
product_price = 100.00  # class float
product_quantity = 12  # class int

user_name = 'sai kiran'
user_contact = 9876543210
user_address = "hyd"
user_pincode = 50028

print(product_id, product_name, product_price, product_quantity)
print(user_name, user_contact, user_address, user_pincode)

# type()
print(type(product_id), type(product_name), type(product_quantity), type(product_price))
# <class 'int'> <class 'str'> <class 'int'> <class 'float'>

# variable : holds the value and stores the value

# when we pass data type in pythin it returns the class name
print(int, float, bool, complex)  # <class 'int'> <class 'float'> <class 'bool'> <class 'complex'>

# object: object is an instance of a class, class name and object name must be same
# when pass object we get default values
print(int(), float(), bool(), complex())  # 0 0.0 False 0j

print(str())

print(list(), tuple(), set(), frozenset())  # [] () set() frozenset()

print(dict())  # {}

print(range(0))  # range(0, 0)

print(bytes(), bytearray())  # b'' bytearray(b'')

# class : it is a blueprint or a template, in class we have properties and method



