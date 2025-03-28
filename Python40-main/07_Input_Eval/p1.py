# input() build-in function
# The nature of input is string

# eval() build-in function
# The nature of eval is data type casting

# Task 1: Enter your name:
# user_name = input('Enter your name: ')
# print('Your Name is: ', user_name, type(user_name))

# Task 2: Login
# user_name = input("Enter your name: ")
# pass_word = input("Enter you password: ")

# control statements / flow controls
# if else condition
# if user_name == "Sai" and pass_word == "Kiran":
#     print("Login Success")
# else:
#     print("Login Failure")

# Task 3: Bank
# user_name = input('Enter your name: ')
# user_email = input('Enter your email: ')
#
# # Manually as developer we are performing casting
# user_account_no = int(input('Enter your account no: '))
# user_contact = int(input('Enter your contact no: '))
# user_balance = float(input('Enter your balance: '))

# print(user_name, user_email, user_account_no, user_contact, user_balance)

# Task 4: eval()
# user_name = input('Enter your name: ')
# user_email = input('Enter your email: ')
#
# user_account_no = input('Enter your account no: ')
# user_contact = input('Enter your contact no: ')
# user_balance = input('Enter your balance: ')
#
# u_account_no = eval(user_account_no)
# u_contact = eval(user_contact)
# u_balance = eval(user_balance)
#
# print(user_name, user_email, u_account_no, u_contact, u_balance)
# print(type(user_name), type(user_email), type(u_account_no), type(u_contact), type(u_balance))
# <class 'str'> <class 'str'> <class 'int'> <class 'int'> <class 'float'>

# Task 5: addition
# if we perform addition using input() it concat the data
# if we perform addition using eval() it add the data
# a = input('Enter a: ')
# b = input('Enter b: ')
# print(a + b)  # 1020

# aa = eval(a)
# bb = eval(b)
# print(aa + bb)

# Task 6: list
# i1 = input('Enter list: ')
# print(i1, type(i1))
#
# e1 = eval(i1)
# print(e1, type(e1))

# l1 = [input('O Index: '), input('1st Index: '), int(input('2nd Index:')), input('3rd Index: ')]
# print(l1, type(l1))

# d1 = {
#     'a': input('Enter the value of a: '),
#     'b': input('Enter the value of b: '),
# }
#
# print(d1)

