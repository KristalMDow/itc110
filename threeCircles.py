# threeCircles.py
# Using a function to create three growing circles.
# By: Kristal Dow 11/12/19

def drawCircle(x, y, size):
    #create the Window object
    win = GraphWin("Testing", 800, 800)
    win.setBackground("Light Blue")

    for i in range(1, 4):
        # scale size and position of circles
        x = i*x
        y = i*y
        size = i*size

        #outputCircle
        outputCircle = Circle(Point(x, y), size)
        outputCircle.setOutline("White")
        outputCircle.draw(win)

#importing graphics library
from graphics import *

#call function to draw circle
drawCircle(100, 100, 30)
