# Introduction to Objects and Classes
# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
# See PyCharm help at https://www.jetbrains.com/help/pycharm/

from Student_Class import Question  # Question Class called from the Student object

test_questions = [
    "What color are Apples?\n(a) Red/Green\n(b)Purple\n(c) Orange\n\n",
    "What color are Banana?\n(a) Teal/Green\n(b)Magenta\n(c) Yellow\n\n",
    "What color are Strawberries?\n(a) Yellow\n(b)Red\n(c) Blue\n\n"
]

question_prompts = [
    Question(test_questions[0], "a"),
    Question(test_questions[1], "c"),
    Question(test_questions[2], "b"),
]


def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(test_questions)) + " Correct")


run_test(question_prompts)
