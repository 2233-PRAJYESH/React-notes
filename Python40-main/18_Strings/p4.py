# upper(), lower(), title(), swap-case(), startswith(), endswith()
# isalnum(), isalpha(),  isdigit(), isspace(),

# name_list = []
# Account_number = []
# User_Ids = []
# Passwords = []
#
# def signup():
#
#     act_str = 1001001
#     name = input('Enter your name: ')
#     name_list.append(name)
#     Account_number.append(act_str)
#     act_str = Account_number[-1]+1
#     print(name_list[-1], Account_number[-1])
#
#
# def login():
#     username = input('User Id: ')
#     password = input('Password: ')
#
#
# def operation(i):
#     switcher = {
#         1: signup(),
#         2: login(),
#     }
#     return switcher.get(i, "try again")
#
#
# while True:
#
#     operation(input("1. Signup 2.Login"))

name_list = []
Account_number = []

your_no = input("Continue: ")
while your_no == "yes":

    name = input("Enter your name: ")
    name_list.append(name)
    ac_number = input('Enter account number')
    Account_number.append(ac_number)
    name_and_ac_number = name_list + Account_number
    print(name_and_ac_number)

# convert to dict





