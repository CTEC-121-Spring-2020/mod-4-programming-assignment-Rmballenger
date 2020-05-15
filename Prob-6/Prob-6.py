# Module 5
#   Programming Assignment 6
#       Prob-6.py

# Robert Ballenger

from graphics import *


def main():
    
    win = GraphWin("Legos",1100,1000)
    # draw basic brick
    blueBrick = Rectangle(Point(10,280), Point(510, 100))
    blueBrick.setFill("blue")
    blueBrick.setOutline("black")
    blueBrick.setWidth(5)
    blueBrick.draw(win)
    # draw first nib
    blueBrickNib = Rectangle(Point(35, 100), Point(85, 80))
    blueBrickNib.setFill("blue")
    blueBrickNib.setOutline("black")
    blueBrickNib.setWidth(5)
    blueBrickNib.draw(win)
    # test
    for i in range(1, 5):
        blueBrickNextNib = blueBrickNib.clone()
        blueBrickNextNib.move(100 *i, 0)
        blueBrickNextNib.draw(win)
    input()

main()