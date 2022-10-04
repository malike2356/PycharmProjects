# Introduction to GIT
# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
# See PyCharm help at https://www.jetbrains.com/help/pycharm/


from turtle import Pen as Turtle

"yertle = Turtle()"


def ternary_tree(size, factor, t):
    if size >= 1:
        for i in range(3):
            t.forward(size)
            ternary_tree(size * factor, factor, t)
            t.backward(size)
            t.right(120)


t = Turtle()
ternary_tree(75, 0.5, t)

