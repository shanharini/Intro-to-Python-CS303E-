# File: Project1.py
# Student: Harini Shanmugam
# UT EID: hs28663
# Course Name: CS303E
#
# Date Created: 9/24/2021
# Date Last Modified: 10/07/2021
# Description of Program: This program prints the calendar for any month in 2022 prompted by the user

def monthName(month):
    if month == 1:
        return "January"
    elif month == 2:
        return "February"
    elif month == 3:
        return "March"
    elif month == 4:
        return "April"
    elif month == 5:
        return "May"
    elif month == 6:
        return "June"
    elif month == 7:
        return "July"
    elif month == 8:
        return "August"
    elif month == 9:
        return "September"
    elif month == 10:
        return "October"
    elif month == 11:
        return "November"
    else:
        return "December"


def firstDayOfMonth(month):
    if month == 1:
        return 6
    elif month == 2:
        return 2
    elif month == 3:
        return 2
    elif month == 4:
        return 5
    elif month == 5:
        return 0
    elif month == 6:
        return 3
    elif month == 7:
        return 5
    elif month == 8:
        return 1
    elif month == 9:
        return 4
    elif month == 10:
        return 6
    elif month == 11:
        return 2
    else:
        return 4


def daysInMonth(month):
    if month == 1:
        return 31
    elif month == 2:
        return 28
    elif month == 3:
        return 31
    elif month == 4:
        return 30
    elif month == 5:
        return 31
    elif month == 6:
        return 30
    elif month == 7:
        return 31
    elif month == 8:
        return 31
    elif month == 9:
        return 30
    elif month == 10:
        return 31
    elif month == 11:
        return 30
    else:
        return 31


def calendar(month):
    header = monthName(month) + " 2022"
    headerCentered = header.center(20, " ")

    print()
    print(headerCentered)
    print("Su Mo Tu We Th Fr Sa")

    space = "   "
    columnCounter = firstDayOfMonth(month)
    print(columnCounter * space, end="")

    for i in range(1, daysInMonth(month)+1):
        print(format(i, "2d"), end=" ")
        columnCounter += 1
        if columnCounter % 7 == 0:
            print()

    print()


def main():
    while True:
        month = int(input("Enter the number of a month [1..12]: "))
        if 1 <= month <= 12:
            calendar(month)
            break
        else:
            print("Month must be between 1 and 12. Try again!")
            continue


main()
