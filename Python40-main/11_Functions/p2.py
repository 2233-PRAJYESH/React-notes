# Basic Functions
# Create a function with zero arguments
# Create a function with arguments
# Create a function and pass default values
# Create a function and add arbitrary-arguments
# Create a function and add return keyword
# Create a function and pass global variable and local variable
# Create a function and use global keyword

# Create a function with zero arguments
# def d1():
#
#     print("Hello World")
#
#
# d1()
# d1()
# d1()

# Create a function with arguments
# def d1(a, b):
#
#     print(a, b)
#
#
# d1(10, 20)
# d1(100, 200)

# Create a function and pass default values
# def d3(username, pincode=500028):
#
#     print(username, pincode)
#
#
# d3("Sai Kiran")
# d3("Sai Ram"),
# d3("Sai Kumar")
# d3("Sai Kumar", 500029)

# Create a function and add arbitrary-arguments
# * args
# def d4(*color):
#
#     print(color)
#
#
# d4('red')
# d4('red', 'orange', 'pink')

# **kwargs
# def d5(**colors):
#
#     print(colors)
#
#
# d5(color_one="red", color_two="blue", color_three="yellow", color_four="green")
#
# #  {'color_one': 'red', 'color_two': 'red', 'color_three': 'red', 'color_four': 'red'}

# Create a function and add return keyword
def d6():

    return "Hello World"


print(d6())


def d7():

    return print("Hello Python")


d7()


def d8():

    return "Hello Java"


d = d8()
print(d)


def d9():

    l1 = [10, 20, 30, 40, 50]

    return len(l1)


print(d9())
