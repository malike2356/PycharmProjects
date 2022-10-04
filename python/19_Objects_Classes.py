# Introduction to objects and classes in Python
# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
# See PyCharm help at https://www.jetbrains.com/help/pycharm/


from Student_Class import Student

student1 = Student("Selorm", "Geology", 3.5, False)
student2 = Student("Malike", "Web design", 3.0, True)

print("Name: ", student1.name)
print("GPA: ", student1.gpa)
print("Major: ", student1.course)
print("On Honour Roll: ", student1.on_honor_roll())

print("- - - - - - - - - - - -")

print("Name: ", student2.name)
print("GPA: ", student2.gpa)
print("Major: ", student2.course)
print("On Honour Roll: ", student2.on_honor_roll())

