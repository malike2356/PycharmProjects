# Introduction to Nested Loops in Python
# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
# See PyCharm help at https://www.jetbrains.com/help/pycharm/

number_grid =[
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

for row in number_grid:
    for column in row:
        print(column)

# Using nested loop to generate binary numbers
for column1 in range(2):
    for column2 in range(2):
        for column3 in range(2):
            print(column1, column2, column3)

