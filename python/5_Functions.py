# Introduction to Functions in Python
# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
# See PyCharm help at https://www.jetbrains.com/help/pycharm/

"""
def print_hi(name):
# Use a breakpoint in the code line below to debug your script.
# print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.
# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#    print_hi('PyCharm')
"""


def say_hi():
    print("I am here to just say Hi today")


print()
say_hi()
print()


def print_hi(name, age):
    print("Your name is " + name + " and you are " + age)


print_hi("John", "38")
print_hi("Tom", "28")
print()

"""USING RETURN IN FUNCTIONS"""


# Defining a function to computes the square of the number.
def square(num):
    return num ** 2  # End of function Block


sq_result = square(9)
print("The square of the number is: ", sq_result)
print()


# defining a function to cube a number
def cube(numb):
    return numb * numb * numb  # End of function Block


cube_result = cube(3)
print("The cube of the number is ", cube_result)
print()


# Defining a function to prints the value of length of string
def l_function(string):
    return len(string)  # End of function Block


# Calling the function we defined
print("Length of the string Functions is: ", l_function("Functions"))
print("Length of the string Python is: ", l_function("Python"))
print()

"""
NOTE:
The return keyword breaks YOU out of the code block and so any 
instruction given in that block after the return code shall not be printed
"""


# Python code to show how to access variables of a nested functions
# defining a nested function
def function1():
    string = 'This is a Python functions tutorial'

    def function2():
        print(string)

    function2()


function1()
