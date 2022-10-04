# Building Translator in Python
# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
# See PyCharm help at https://www.jetbrains.com/help/pycharm/

try:
    answer = 10 / 0  # an example of error
    number = int(input("Enter a number: "))
    print(number)
except ZeroDivisionError as error:
    print(error)  # We could also have ignored the value err and print("Division by Zero")
except ValueError:
    print("Invalid Value Entered")

#  Best practice in python is to except specific errors not all errors generally
