# File: Student.py
# Student: Harini Shanmugam
# UT EID: hs28663
# Course Name: CS303E
#
# Date Created: 10/18/2021
# Date Last Modified: 10/20/2021
# Description of the Program: This program will return a student's name, Exam 1 grade, Exam 2 grade,
# and average of the grades.

class Student:
    def __init__(self, name, exam1grade="None", exam2grade="None"):
        self.__name = name
        self.__exam1grade = exam1grade
        self.__exam2grade = exam2grade

    def __str__(self):
        return "Student: " + str(self.__name) + "\n" + \
               "  Exam1: " + str(self.__exam1grade) + "\n" + \
               "  Exam2: " + str(self.__exam2grade)

    def getName(self):
        return self.__name

    def getExam1Grade(self):
        return self.__exam1grade

    def setExam1Grade(self, exam1grade):
        self.__exam1grade = exam1grade

    def getExam2Grade(self):
        return self.__exam2grade

    def setExam2Grade(self, exam2grade):
        self.__exam2grade = exam2grade

    def getAverage(self):
        if self.__exam1grade == "None" or self.__exam2grade == "None":
            print("Some exam grades not available.")
        else:
            average = float(int(self.__exam1grade + self.__exam2grade) / 2)
            return average
