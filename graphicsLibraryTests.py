#some basic tests of the graphic library
from graphics import *

#create the Window object
win = GraphWin("Testing", 400, 400)
win.setBackground("green")


#create two Point objects and print the coordinates of the first to commandline
p = Point(50, 60)
p.draw(win)

print(p.getX())
print(p.getY())

p2 = Point(100, 150)
p2.draw(win)

#create a line
line = Line(p, p2)
line.draw(win)

#create an oval
anOval = Oval(p, p2)
anOval.setOutline("blue")
anOval.setFill("")
anOval.draw(win)

#draw a circle
center = Point(300, 300)
circ = Circle(center, 60)
circ.setFill("dark orchid")
circ.setOutline("chartreuse")
circ.setWidth(5)
circ.draw(win)


#add a text label to the center of the circle
label = Text(center, "My wonderful circle")
label.setSize(8)
label.setTextColor("yellow")
label.draw(win)

label1 = Text(Point(200, 200), "Is this centered?")
label1.setSize(18)
label1.setTextColor("white")
label1.draw(win)

#add a rectangle
rect = Rectangle(Point(20, 30), Point(180, 165))
rect.draw(win)

#making scary eyes
eye1 = Circle(Point(100, 50), 15)
eye1.setFill("yellow")
eye1.setOutline("red")
eye1.setWidth(2)
eye1.draw(win)

eye2 = eye1.clone()
eye2.move(60, 0)
eye2.draw(win)
