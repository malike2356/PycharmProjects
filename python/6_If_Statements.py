# Introduction to IF STATEMENTS in Python
# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
# See PyCharm help at https://www.jetbrains.com/help/pycharm/


print()
print("Velox Universal Grade Checker ")
print("----------------------------- ")
print()


marks = int(input("Enter Your marks? "))


if 85 < marks <= 100:
    print("Congrats ! you scored grade A ")
elif 60 < marks <= 85:
    print("You scored grade B + ")
elif 40 < marks <= 60:
    print("You scored grade B ")
elif 30 < marks <= 40:
    print("You scored grade C ")
else:
    print("Sorry you did not pass! ")


print()


print()
print("Velox Universal Basic Calculator ")
print("-------------------------------- ")
print()

# Using IF STATEMENTS TO CREATE A SIMPLE CALCULATOR

number1 = float(input(" Enter First Number: "))
opr = input("Enter one of these Operator +,-,/,x... ")
number2 = float(input(" Enter Second Number: "))


if opr == "+":
    print("Answer is:", round((number1 + number2), 4))  # round the answer to 4 decimal places
elif opr == "-":
    print("Answer is:", round((number1 - number2), 4))  # round the answer to 4 decimal places
elif opr == "x" or opr == "*":
    print("Answer is:", round((number1 * number2), 4))  # round the answer to 4 decimal places
elif opr == "/":
    print("Answer is:", round((number1 / number2), 4))  # round the answer to 4 decimal places
else:
    print("Invalid Operator")

