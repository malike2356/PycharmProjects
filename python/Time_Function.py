import calendar
import datetime
import time

this_year = datetime.datetime.now().year  # We can also use today instead of now for the same result
this_month = datetime.datetime.now().month  # We can also use now instead of today for the same result
today = datetime.datetime.now().day  # We can also use now instead of today for the same result

print(time.localtime(time.time()))  # returns the current time
print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
print(f" This year is: {this_year}")
print(f" This month is: {this_month}")
print(f" This day is: {today}")
print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
print("Formatted time:", time.asctime(time.localtime(time.time())))  # returns the formatted time
print("Total Clock ticks:", time.time())  # returns the number of ticks spent since 12AM, 1st January 970
print("Current Datetime:", datetime.datetime.now())  # returns the current datetime object
print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
print(calendar.prcal(2022))  # returns the calendar of the specified whole year
print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
print(calendar.month(this_year, this_month))  # returns the calendar of the specific year and month
print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")

try:
    user_age = int(input("In which year were you born? "))
    age_result = this_year - user_age
    if user_age >= this_year:
        print("You can not be born in the future")
    else:
        print(f"You are {age_result} years old")
except ValueError:
    print("Invalid Entry. Be serious please!")

