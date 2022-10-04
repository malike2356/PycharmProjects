# Introduction to IF ELSE STATEMENTS and BOOLEANS in Python
# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
# See PyCharm help at https://www.jetbrains.com/help/pycharm/

# If Statements
# Using OR/AND instead

is_male = True
is_tall = False


if is_male or is_tall:
    print("You are a Tall male")
elif is_male and not is_tall:
    print("You are a short male")
elif not is_male and is_tall:
    print("You are not a male but are tall")
else:
    print("You are neither a male nor tall")


