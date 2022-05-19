# File: DaysInMonth.py
# Student: Harini Shanmugam
# UT EID: hs28663
# Course Name: CS303E
#
# Date Created: 9/20/2021
# Date Last Modified: 9/20/2021
# Description of the Program: This program prompts the user to enter a month and year and displays the number of days
# in that month

year = int(input("Please enter a year: "))
month = int(input("Please enter a month: "))

if month == 1:
    nameMonth = "January"
    numDays = 31
elif month == 2:
    nameMonth = "February"
    numDays = 28
elif month == 3:
    nameMonth = "March"
    numDays = 31
elif month == 4:
    nameMonth = "April"
    numDays = 30
elif month == 5:
    nameMonth = "May"
    numDays = 31
elif month == 6:
    nameMonth = "June"
    numDays = 30
elif month == 7:
    nameMonth = "July"
    numDays = 31
elif month == 8:
    nameMonth = "August"
    numDays = 31
elif month == 9:
    nameMonth = "September"
    numDays = 30
elif month == 10:
    nameMonth = "October"
    numDays = 31
elif month == 11:
    nameMonth = "November"
    numDays = 30
elif month == 12:
    nameMonth = "December"
    numDays = 31

isLeapYear = (year % 4 == 0) and (not (year % 100 == 0) or (year % 400 == 0));
if month == 2 and isLeapYear == True:
    print(nameMonth, year, "has 29 days")
else:
    print(nameMonth, year, "has", numDays, "days")
