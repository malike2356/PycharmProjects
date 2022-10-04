# Introduction to list
# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
# See PyCharm help at https://www.jetbrains.com/help/pycharm/


Days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
Jackpot = [1, 5, 6, 7, 2, 3, 4, 9, 8, 4, 9, 8, 9]

print(Days_of_week)
print(Days_of_week[-5])
print(Days_of_week[6])

Days_of_week.insert(7, "Holiday")
print(Days_of_week)

Days_of_week.clear()
print(Days_of_week)

print(Jackpot)

print(Jackpot.count(9))

Jackpot.sort()
print(Jackpot)

Jackpot.reverse()
print(Jackpot)

Jackpot.pop()
print(Jackpot)
