# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from math import *

myFav_num = int(input("Enter your Old PIN ? "))
fName = (input("Enter your First Name? "))
# lName = (input("Enter your Last Name? "))

print()
print("The square of your old PIN is: " + str(round(pow(myFav_num, 2))))  # square of input rounded to the nearest whole
print("The floor of your old PIN is: " + str(abs(floor(myFav_num))))  # taking the floor values
print("The Ceiling of your old PIN is: " + str(abs(ceil(myFav_num))))  # taking the ceiling values

my_float: float = (sqrt(abs(myFav_num)))
my_Dec2 = round(my_float, 3)  # my_Dec2 = "{0:.4g}".format(my_float) will produce same result
print("The square root of your old PIN is: " + str(my_Dec2))  # String of the square root of the input

new_Fav = abs(myFav_num) % 2  # making the input an absolute value
if new_Fav == 0:
    print(" Hint: Your Old PIN \"" + str(abs(myFav_num)) + "\" is an Even Number ")  # get absolute value
else:
    print("Hint: Your PIN is an Odd Number")
print()
print("Thanks for using my program "+fName.upper())
