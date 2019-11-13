# threeCircles.py
# Using a function to create three growing circles.
# By: Kristal Dow 11/12/19

#importing graphics library
from graphics import *

def drawFace(center, size, window):
    head = Circle(center, size)
    head.setFill("yellow")
    head.draw(window)

win = GraphWin("Faces")
drawFace(Point(50,50), 10, win)
drawFace(Point(100,100), 20, win)
drawFace(Point(150,150), 30, win)
win.getMouse()
win.close()

