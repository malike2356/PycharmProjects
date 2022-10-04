# Introduction to For Loop Practice in Python
# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
# See PyCharm help at https://www.jetbrains.com/help/pycharm/

#  Using a for loop and functions to creation an exponent program

def raise_to_power(base_number, power_number):
    result = 1
    for index in range(power_number):  # Loop from Zero to power_number
        result = result * base_number
    return result


print(raise_to_power(3, 4))

