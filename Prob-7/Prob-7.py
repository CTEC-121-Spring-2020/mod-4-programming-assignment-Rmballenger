# Module 5
#   Programming Assignment 6
#       Prob-7.py

# Robert Ballenger

from graphics import *


def main():

    win = GraphWin(title="Face Face McFace Face", height=800, width=800)

    #~~~~~~~~~~~~~~~~~~~BASE~~~~~~~~~~~~~~~~~~~~~~~

    faceBase = Oval(Point(60.0, 3.0), Point(757.0, 787.0))
    faceBase.setOutline("black")
    faceBase.setFill("light grey")
    faceBase.draw(win)

    #~~~~~~~~~~~~~~~~~~~MOUTH~~~~~~~~~~~~~~~~~~~~~~~

    faceMouth = Polygon(Point(108, 450), Point(290, 555), Point(523, 555), Point(705, 450), Point(535, 745), Point(290, 745))
    faceMouth.setOutline("black")
    faceMouth.setFill("dark red")
    faceMouth.draw(win)

    #~~~~~~~~~~~~~~~~~~~TEETH~~~~~~~~~~~~~~~~~~~~~~~

    faceTooth1 = Polygon(Point(290, 555), Point(320.0, 696.0), Point(357.0, 555.0))
    faceTooth1.setOutline("black")
    faceTooth1.setFill("light grey")
    faceTooth1.draw(win)

    faceTooth2 = faceTooth1.clone()
    faceTooth2.move(165, 0)
    faceTooth2.draw(win)

    faceTooth3 = Polygon(Point(290.0, 745.0), Point(305.0, 720.0), Point(375.0, 720.0), Point(390.0, 745.0))
    faceTooth3.setOutline("black")
    faceTooth3.setFill("light grey")
    faceTooth3.draw(win)

    faceTooth4 = faceTooth3.clone()
    faceTooth4.move(145, 0)
    faceTooth4.draw(win)

    #~~~~~~~~~~~~~~~~~~~NOSE~~~~~~~~~~~~~~~~~~~~~~~~

    faceNose = Polygon(Point(409.0, 321.0), Point(364.0, 500.0), Point(453.0, 500))
    faceNose.setOutline("black")
    faceNose.setFill("dark grey")
    faceNose.draw(win)

    #~~~~~~~~~~~~~~~~~~~EYES~~~~~~~~~~~~~~~~~~~~~~~~

    faceEye1 = Circle(Point(270, 235), 90)
    faceEye1.setOutline("black")
    faceEye1.setFill("white")
    faceEye1.draw(win)

    faceInnerEye1 = Circle(Point(270, 235), 20)
    faceInnerEye1.setFill("black")
    faceInnerEye1.draw(win)

    faceEye2 = faceEye1.clone()
    faceEye2.move(275, 0)
    faceEye2.draw(win)

    faceInnerEye2 = faceInnerEye1.clone()
    faceInnerEye2.move(275, 0)
    faceInnerEye2.draw(win)

    #~~~~~~~~~~~~~~~~~~~EARS~~~~~~~~~~~~~~~~~~~~~~~~

    faceEar1 = Oval(Point(14.0, 174.0), Point(104.0, 436.0))
    faceEar1.setOutline("black")
    faceEar1.setFill("darkgrey")
    faceEar1.draw(win)

    faceEar2 = faceEar1.clone()
    faceEar2.move(675, 0)
    faceEar2.draw(win)

    #~~~~~~~~~~~~~~~~~~~HAIR~~~~~~~~~~~~~~~~~~~~~~~~

    faceHair = Polygon(Point(109.0, 0.0), Point(11.0, 181.0), Point(190.0, 123.0), Point(154.0, 256.0), Point(505.0, 87.0), Point(732.0, 76.0), Point(730, 0))
    faceHair.setOutline("orange")
    faceHair.setFill("dark orange")
    faceHair.draw(win)
   
    #~~~~~~~~~~~~~~~~~~TRASH~~~~~~~~~~~~~~~~~~~~~~~~
    

    Text(Point(400, 10), "Click again to quit...").draw(win)
    win.getMouse()



main()