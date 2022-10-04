# Building Translator in Python
# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
# See PyCharm help at https://www.jetbrains.com/help/pycharm/


def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter in "AaEeIiOoUu":
            if letter.isupper():
                translation = translation + "C"
            else:
                translation = translation + "c"
        else:
            translation = translation + letter
    return translation


print(translate(input("Enter a phrase: ")))
