# winterScene.py
# Creating a winter scene with the graphics library.
# By: Kristal Dow 10/20/19

#importing graphics library
from graphics import *

#create the Window object
win = GraphWin("Testing", 400, 400)
win.setBackground("Light Blue")

#making the snow background
snow = Rectangle(Point(0, 275), Point(399, 399))
snow.setFill("White")
snow.setOutline("White")
snow.draw(win)

#making a snowman
#body of the snowman
snowball = Circle(Point(100, 100), 30)
snowball.setFill("White")
snowball.setOutline("White")
snowball.draw(win)

snowball2 = Circle(Point(100, 160), 40)
snowball2.setFill("White")
snowball2.setOutline("White")
snowball2.draw(win)

snowball3 = Circle(Point(100, 230), 50)
snowball3.setFill("White")
snowball3.setOutline("White")
snowball3.draw(win)

#hat of the snowman
hatTop = Rectangle(Point(80, 25), Point(120, 80))
hatTop.setFill("Black")
hatTop.draw(win)

hatBottom = Rectangle(Point(65, 65), Point(135, 80))
hatBottom.setFill("Black")
hatBottom.draw(win)

#eyes and buttons of the snowman
eye1 = Circle(Point(85, 90), 5)
eye1.setFill("black")
eye1.draw(win)

eye2 = eye1.clone()
eye2.move(30, 0)
eye2.draw(win)

button1 = eye1.clone()
button1.move(15, 50)
button1.draw(win)

button2 = button1.clone()
button2.move(0, 15)
button2.draw(win)

button3 = button2.clone()
button3.move(0, 15)
button3.draw(win)

#mouth of the snowman
dot1 = Circle(Point(88, 110), 2)
dot1.setFill("black")
dot1.draw(win)

dot2 = dot1.clone()
dot2.move(6, 3)
dot2.draw(win)

dot3 = dot2.clone()
dot3.move(6, 1)
dot3.draw(win)

dot4 = dot2.clone()
dot4.move(12, 0)
dot4.draw(win)

dot5 = dot1.clone()
dot5.move(24, 0)
dot5.draw(win)

#nose of the snowman
nose = Polygon(Point(97, 95), Point(97, 105), Point(105, 100))
nose.setFill("Orange")
nose.setOutline("Orange")
nose.draw(win)


#Making a tree.
#tree leaves
tree = Polygon(Point(250, 25), Point(180, 260), Point(320, 260))
tree.setFill("Green")
tree.setOutline("Green")
tree.draw(win)

#tree trunk
treeTrunk = Rectangle(Point(230, 260), Point(270, 275))
treeTrunk.setFill("Brown")
treeTrunk.setOutline("Brown")
treeTrunk.draw(win)

#Tree ornaments
orn1 = Circle(Point(250, 50), 5)
orn1.setFill("yellow")
orn1.setOutline("light yellow")
orn1.setWidth(2)
orn1.draw(win)

orn2 = orn1.clone()
orn2.move(15, 30)
orn2.draw(win)

orn3 = orn2.clone()
orn3.move(-25, 30)
orn3.draw(win)

orn4 = orn3.clone()
orn4.move(10, 20)
orn4.draw(win)

orn5 = orn4.clone()
orn5.move(22, -15)
orn5.draw(win)

orn6 = orn5.clone()
orn6.move(0, 45)
orn6.draw(win)

orn7 = orn6.clone()
orn7.move(-50, 5)
orn7.draw(win)

orn8 = orn7.clone()
orn8.move(25, 25)
orn8.draw(win)

orn9 = orn8.clone()
orn9.move(25, 25)
orn9.draw(win)

orn10 = orn9.clone()
orn10.move(-65, 0)
orn10.draw(win)

orn11 = orn10.clone()
orn11.move(25, 25)
orn11.draw(win)

orn12 = orn11.clone()
orn12.move(75, 0)
orn12.draw(win)
