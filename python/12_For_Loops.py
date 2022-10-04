# Introduction to For Loop Practice in Python
# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
# See PyCharm help at https://www.jetbrains.com/help/pycharm/


import random

# Simple Libray Program using For Loop
print()
print("The following books are found on a Bookshelf:")
Bookshelf = ["Loyalty", "Transform", "Mega Church", "Tithing"]
length_of_list = len(Bookshelf)
counter = 1
for item in Bookshelf:
    print(str(counter) + ". " + str(item))
    counter += 1
print("ONLY " + str(length_of_list) + " Books in Library. Do not request more than " + str(length_of_list))

print()

# Looping through user inputs and printing the range
try:
    order = int(input("How many books do you need out of the " + str(length_of_list) + "?: "))
    book_choice = random.sample(Bookshelf, k=order)

    if order <= length_of_list:
        print("You can get the following books: ")
        print(book_choice)
except ValueError:
    print("Either an Invalid Entry OR You requested more than " + str(length_of_list) + "books.\n Sorry we "
                                                                                        "can't serve you!")
