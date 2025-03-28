# Types of Statements
# Selection Statements: if else elif match
# Iteration Statements: for, while
# Transfer Statements: break and continue
# Task 1: if condition with boolean value
# if True:
#     print("Condition Passed")
#     a = 10
#     print(a)
#
#
# # This code is unreachable
# if False:
#     print("Condition Passed")
#     b = 20
#     print(b)

# Task 2: if condition with operators
# a = 5
# b = 10
# if a > b:
#     print("if condition")
# else:
#     print("else block")

# Task 3: logical operators
# user_name = input('Enter your name: ')
# pass_word = input('Enter your password: ')
# if user_name == "admin" and pass_word == "admin":
#     print("Login Success")
# else:
#     print("Login Failure")

# Task 4: elif
# user_salary = float(input('Enter you salary: '))
# if user_salary <= 10000:
#     print('User Salary is 0 to 10000: ', user_salary)
# elif user_salary <= 20000:
#     print('User Salary is 10001 to 20000: ', user_salary)
# elif user_salary <= 30000:
#     print('User Salary is 20001 to 30000: ', user_salary)
# elif user_salary <= 40000:
#     print('User Salary is 30001 to 40000: ', user_salary)
# elif user_salary <= 50000:
#     print('User Salary is 40001 to 50000: ', user_salary)
# else:
#     print("Invalid Salary")

# Task 5: match case
# functions are used for re-use-ability

# status_code = int(input("Enter status code: "))
# match status_code:
#     case 200:
#         print("OK")
#     case 201:
#         print("CREATED")
#     case 202:
#         print("ACCEPTED")
#     case 204:
#         print("NO CONTENT")
#     case _:
#         print("No Matching Status Code")

# Task 6: for loop
# list
# l1 = [10, 20, 30, 40, 50, 60, 70, 80]
# for i in l1:
#     print(i)

# string
# s1 = "hello world"
# for i in s1:
#     print(i)

# int, float, complex
# a = 10
# for i in a:
#     print(i)  # TypeError: 'int' object is not iterable

# for i in range(0, 10, 1):
#     print(i)
#
# for i in range(10, 0, -1):
#     print(i)

# d1 = {1: 10, 2: 20, 3:30, 4: 40, 5: 50}
# for i in d1.items():
#     print(i)

# Task 7: while loop
# while True:
#
#     print("Condition Check")

# Un-reachable code
# while False:
#
#     print("Condition Check")

# Assignment Operator
# i = 1
# while i <= 10:
#
#     print(i)
#     i += 1


# j = 10
# while j >= 1:
#
#     print(j)
#     j -= 1

# while True:
#
#     user_salary = float(input('Enter you salary: '))
#     if user_salary <= 10000:
#         print('User Salary is 0 to 10000: ', user_salary)
#     elif user_salary <= 20000:
#         print('User Salary is 10001 to 20000: ', user_salary)
#     elif user_salary <= 30000:
#         print('User Salary is 20001 to 30000: ', user_salary)
#     elif user_salary <= 40000:
#         print('User Salary is 30001 to 40000: ', user_salary)
#     elif user_salary <= 50000:
#         print('User Salary is 40001 to 50000: ', user_salary)
#     else:
#         print("Invalid Salary")
#
#     repeat = input('Do you want to continue or stop, ? yes/no: ').lower()
#     if repeat != "yes":
#         break

# l1 = ["NameOne"]
#
# while True:
#
#     l1.append(input('Enter a value: '))
#
#     repeat = input('Do you want to continue or stop, ? yes/no: ').lower()
#     if repeat != "yes":
#         break
#
#
# print(l1)

# Task 8: break and continue
# for i in range(10):
#
#     if i == 5:
#
#         continue  # skips the iteration
#
#     print(i)

# for i in range(10):
#
#     if i == 5:
#
#         break  # stops the iteration
#
#     print(i)


# for i in range(10):
#     pass

