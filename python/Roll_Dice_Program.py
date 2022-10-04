import random


def roll():
    first = random.randint(1, 6)
    second = random.randint(1, 6)
    return first, second


class Dice:
    pass


dice = Dice()
print(roll())

# The same program can be written as below
"""
import random


class Dice:
    def roll(self):
        first = random.randint(1, 6)
        second = random.randint(1, 6)
        return first, second


dice = Dice()
print(dice.roll())
"""