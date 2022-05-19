# File: MinMax.py
# Student: Harini Shanmugam
# UT EID: hs28663
# Course Name: CS303E
#
# Date Created: 9/25/2021
# Date Last Modified: 10/3/2021
# Description of the Program: This program accepts an arbitrary number of integer inputs
# from the user and prints out the minimum and maximum of the numbers entered

value = input("Enter an integer or 'stop' to end: ")

if value == "stop":
    print("You didn't enter any numbers")
else:
    maxNum = int(value)
    minNum = int(value)
    while value != "stop":
        if int(value) >= maxNum:
            maxNum = int(value)
        if int(value) <= minNum:
            minNum = int(value)
        value = input("Enter an integer or 'stop' to end: ")
    print("The maximum is", maxNum)
    print("The minimum is", minNum)
