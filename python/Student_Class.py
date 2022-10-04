class Student:
    def __init__(self, name, course, gpa, in_on_probation):
        self.name = name
        self.course = course
        self.gpa = gpa
        self.is_on_probation = in_on_probation

    def on_honor_roll(self):
        if self.gpa >= 3.5:
            return True
        else:
            return False


class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

