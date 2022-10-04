# Introduction to While Loop Practice in Python
# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
# See PyCharm help at https://www.jetbrains.com/help/pycharm/


# Guessing Game
guess_Word = "Malike"
guess_Answer = ""
guess_Count = 0
guess_Limit = 3
out_of_Guesses = False

while guess_Answer.upper() != guess_Word.upper() and not out_of_Guesses:
    if guess_Count < guess_Limit:
        guess_Answer = input("Enter The Developers' Alias: ")
        guess_Count += 1
    else:
        out_of_Guesses = True
if out_of_Guesses:
    print("Sorry you have exhausted all your chances, YOU LOOSE!")
    print("Let's Just move to the next game")
else:
    print("Yes: Correct Answer is: " + guess_Answer.upper() + " You Win!")
print()

