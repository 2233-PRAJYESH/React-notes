# Variable holds the and stores the value

# Python:
# Function: Global V and Local V
# OOPS: Class V, Static V, Instance V
# Create a function and pass global variable and local variable
# Scope: Global V scope is in the file
user_name = "Sai Kiran"  # global V


def user_details():
    # we can access global variable in the function scope and in the file scope
    # local variables are declared inside the function
    # scope of the local v is inside the function
    user_email = "saikiran@gmail.com"  # Local V
    print('Global v inside: ', user_name)
    print('Local v : ', user_email)


user_details()

# we declare global v outside the function
print('Global v outside: ', user_name)
# print('Local v outside: ', user_email)  # NameError: name 'user_email' is not defined. Did you mean: 'user_details'?

