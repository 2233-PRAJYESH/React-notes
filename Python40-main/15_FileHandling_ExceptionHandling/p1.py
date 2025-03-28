# file handling
# task 1: create a file and insert data
# exception handling
# exception: an unwanted exception that disturbs the normal flow of program is called eh
# try is a block used for writing the business logic
# except is used for handling the exceptions
# finally block is used for closing the connections
# f = None
# try:
#     f = open('one.txt', 'w')  # open(filename, mode)
#     s = input('Enter some text: ')
#     f.write(s)
#     print('file created and data inserted')
# except FileNotFoundError as e:
#     print('Exception is: ', e)
# finally:
#     f.close()

# task 2: read the data form file
# f = None
# try:
#     f = open('one.txt', 'r')
#     s = f.read()
#     print(s)  # Hello Hi How are you
#
# except FileNotFoundError as e:
#     print('Exception is: ', e)
#
# finally:
#     f.close()

# task 3: write and read the data using writelines method
# f = None
# try:
#     f = open('list.txt', 'w')
#     l1 = ["NameOne", "NameTwo", "NameThree", "NameFour"]
#     f.writelines(l1)
#     print("Data Inserted")
#
#     f = open('list.txt', 'r')
#     for i in f:
#         print(i)
#
# except FileNotFoundError as e:
#     print('Exception is: ', e)
#
# finally:
#     f.close()

# task 4: write and read the data using writelines method, but don't use finally block
# try:
#     with open('list.txt', 'w') as f:
#         l1 = ['NameOne', 'NameTwo', 'NameThree', 'NameFour']
#         f.writelines('\n'.join(l1))
#         print('Data Inserted')
#
#     with open('list.txt', 'r') as f:
#         for i in f:
#             print(i.strip())
#
# except FileNotFoundError as e:
#
#     print('Exception is: ', e)

# task 5: tell() this method returns the current position of the file
# try:
#
#     f = None
#     try:
#         f = open('two.txt', 'w')
#         s = input('Enter a text: ')
#         f.write(s)
#     except FileNotFoundError as e:
#         print('Exception is: ', e)
#     finally:
#         f.close()
#
#     try:
#         f = open('two.txt', 'r')
#         print(f.tell())
#         print(f.read(7))
#         print(f.tell())
#     except FileNotFoundError as e:
#         print('Exception is: ', e)
#     finally:
#         f.close()
# except FileNotFoundError as e:
#     print('Exception is: ', e)


# s1 ="Hello HI How are you"
# print(len(s1))

# task 6: how to transfer data from one to other file
# try:
#     f = open('list.txt', 'r')
#     data = f.read()
#     f1 = open('list_new.txt', 'w')
#     f1.write(data)
#     print('file created')
#     f.close()
#     f1.close()
# except FileNotFoundError as e:
#     print('Exception: ', e)

# task 7: converting python object into byte stream
import pickle

# l1 = ['NameOne', 'NameTwo', 'NameThree', 'NameFour']
# print(l1)  # ['NameOne', 'NameTwo', 'NameThree', 'NameFour']
#
# # wb : write binary
# f1 = open('three.dat', 'wb')
# pickle.dump(l1, f1)
# f1.close()

# task 7: converting byte stream into python object
# f1 = open('three.dat', 'rb')
# p = pickle.load(f1)
# print(p)
# f1.close()

# task 8: store excel data
# from openpyxl import Workbook
#
# data = [
#     ['Name', 'Age', 'City'],
#     ['NameOne', 25, 'CityOne'],
#     ['NameTwo', 26, 'CityTwo'],
#     ['NameThree', 27, 'CityThree'],
#     ['NameFour', 28, 'CityFour']
#
# ]
#
# wb = Workbook()
# ws = wb.active
#
# for row in data:
#     ws.append(row)
#
# excel_file_path = 'one.xlsx'
#
# wb.save(excel_file_path)
#
# print("Data has written to ", excel_file_path)

# task 9: read the excel data
# from openpyxl import load_workbook
#
# excel_file_path = 'one.xlsx'
#
# # load the workbook
# wb = load_workbook(excel_file_path)
#
# # get the activate sheet
# ws = wb.active
#
# for rows in ws.iter_rows(values_only=True):
#
#     print(rows)
#
# wb.close()

# task 10: a+ appending
# readline_before = open('one.txt', 'r')
# before = readline_before.read()
# print('Before, ', before)  # Before,  Hello Hi How are you
# readline_before.close()
#
# file = open('one.txt', mode='a+')
# file.write("Welcome to JavaScript")
# file.close()
#
# readline_after = open('one.txt', 'r')
# after = readline_after.read()
# print('Before, ', after)  # Before,  Hello Hi How are youWelcome to JavaScript
# readline_after.close()





