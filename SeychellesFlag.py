# File: SeychellesFlag.py
# Student: Harini Shanmugam
# UT EID: hs28663
# Course Name: CS303E
#
# Date Created: 11/28/21
# Date Last Modified: 11/29/21
# Description of Program: This program will use Turtle Graphics to draw the flag of Seychelles

import turtle


def rectangle(ttl, x, y, length, width):
    ttl.penup()
    ttl.goto(x, y)
    ttl.setheading(0)
    ttl.pendown()
    for i in range(2):
        ttl.forward(length)
        ttl.right(90)
        ttl.forward(width)
        ttl.right(90)
    ttl.penup()


def triangle(ttl, a, b, c, d, e, f, color):
    ttl.fillcolor(color)
    ttl.begin_fill()
    ttl.penup()
    ttl.goto(a, b)
    ttl.pendown()
    ttl.goto(c, d)
    ttl.goto(e, f)
    ttl.goto(a, b)
    ttl.penup()
    ttl.end_fill()


def quadrilateral(ttl, a, b, c, d, e, f, g, h, color):
    ttl.fillcolor(color)
    ttl.begin_fill()
    ttl.penup()
    ttl.goto(a, b)
    ttl.pendown()
    ttl.goto(c, d)
    ttl.goto(e, f)
    ttl.goto(g, h)
    ttl.goto(a, b)
    ttl.penup()
    ttl.end_fill()


myBlue = '#003D88'
myYellow = '#FCD955'
myRed = '#D72323'
myWhite = '#FFFFFF'
myGreen = '#007B3A'

Flag = turtle.Turtle()
Flag.speed(10)
Flag.pensize(1)

rectangle(Flag, -300, 300, 600, 300)
triangle(Flag, -300, 0, -300, 300, -100, 300, myBlue)
triangle(Flag, -300, 0, -100, 300, 100, 300, myYellow)
quadrilateral(Flag, -300, 0, 100, 300, 300, 300, 300, 200, myRed)
triangle(Flag, -300, 0, 300, 200, 300, 100, myWhite)
triangle(Flag, -300, 0, 300, 100, 300, 0, myGreen)

turtle.done()
