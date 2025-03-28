# a = 10
# b = 0
# print('before')
# print(a / b)  # ZeroDivisionError: division by zero

# print('after')

# try, except, finally keywords
# try:
#     a = 10
#     b = 0
#     print('before')
#     print(a / b)
#
# except ZeroDivisionError as e:
#     print(e)
#
# print('after')

# try, except, finally, raise,
# raise exception
# print(10/0)  # ZeroDivisionError: division by zero
# print(10/2)  # 5.0
# class EmployeeSalary(Exception):
#
#     # instance method
#     def checkSalary(self, e_salary):
#
#         if e_salary <= 50000:
#
#             print("Employee Salary is 50,000")
#         else:
#
#             raise EmployeeSalary('EmployeeSalary out of the range')
#
#
# e = EmployeeSalary()
# e.checkSalary(60000)
# print('Employee Verified')

# l1 = [10, 20, 30, 40, 50]
# print(l1[10])  # IndexError: list index out of range

try:
    l1 = [10, 20, 30, 40, 50]
    print(l1[10])  # IndexError: list index out of range
except IndexError as e:
    print(e)

print("After")


try:
    l1 = [10, 20, 30, 40, 50]
    print(l1[10])  # IndexError: list index out of range

    s1 = {10, 20, 30, 40, 50}
    print(s1[1])  # TypeError: 'set' object is not subscriptable
except TypeError as e:
    print(e)
except IndexError as e:
    print(e)

print("After")

try:
    l1 = [10, 20, 30, 40, 50]
    print(l1[10])  # IndexError: list index out of range

    s1 = {10, 20, 30, 40, 50}
    print(s1[1])  # TypeError: 'set' object is not subscriptable

except Exception as e:
    print(e)


