# Module 5
#   Programming Assignment 6
#       Prob-6.py

# Robert Ballenger

from graphics import *


def main():
    
    win = GraphWin("Steppy Steppy Owe Owe",1100,1000)

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    # blue brick
    blueBrick = Rectangle(Point(10,280), Point(510, 100))
    blueBrick.setFill("blue")
    blueBrick.setOutline("black")
    blueBrick.setWidth(5)
    blueBrick.draw(win)

    # blue nibs
    blueBrickNib = Rectangle(Point(35, 100), Point(85, 80))
    blueBrickNib.setFill("blue")
    blueBrickNib.setOutline("black")
    blueBrickNib.setWidth(5)
    blueBrickNib.draw(win)
    
    # dupeing nibs
    for i in range(1, 5):
        blueBrickNextNib = blueBrickNib.clone()
        blueBrickNextNib.move(100 *i, 0)
        blueBrickNextNib.draw(win)

 #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    # green brick
    greenBrick = blueBrick.clone()
    greenBrick.setFill("green")
    greenBrick.move(575, 0)
    greenBrick.draw(win)

    # green nibs
    greenBrickNib = blueBrickNib.clone()
    greenBrickNib.setFill("green")
    greenBrickNib.move(575, 0)
    greenBrickNib.draw(win)

    # dupeing nibs
    for i in range(1, 5):
        greenBrickNextNib = greenBrickNib.clone()
        greenBrickNextNib.move(100 *i, 0)
        greenBrickNextNib.draw(win)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    # yellow brick
    yellowBrick = blueBrick.clone()
    yellowBrick.setFill("yellow")
    yellowBrick.move(0, 300)
    yellowBrick.draw(win)

    # yellow nibs
    yellowBrickNib = blueBrickNib.clone()
    yellowBrickNib.setFill("yellow")
    yellowBrickNib.move(0, 300)
    yellowBrickNib.draw(win)

    # dupeing nibs
    for i in range(1, 5):
        yellowBrickNextNib = yellowBrickNib.clone()
        yellowBrickNextNib.move(100 *i, 0)
        yellowBrickNextNib.draw(win)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    # red brick
    redBrick = greenBrick.clone()
    redBrick.setFill("red")
    redBrick.move(0, 300)
    redBrick.draw(win)

    # red nibs
    redBrickNib = greenBrickNib.clone()
    redBrickNib.setFill("red")
    redBrickNib.move(0, 300)
    redBrickNib.draw(win)

    # dupeing nibs
    for i in range(1, 5):
        redBrickNextNib = redBrickNib.clone()
        redBrickNextNib.move(100 *i, 0)
        redBrickNextNib.draw(win)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    # light blue brick
    lightBlueBrick = yellowBrick.clone()
    lightBlueBrick.setFill("light blue")
    lightBlueBrick.move(0, 300)
    lightBlueBrick.draw(win)

    # lightBlue nibs
    lightBlueBrickNib = yellowBrickNib.clone()
    lightBlueBrickNib.setFill("light blue")
    lightBlueBrickNib.move(0, 300)
    lightBlueBrickNib.draw(win)

    # dupeing nibs
    for i in range(1, 5):
        lightBlueBrickNextNib = lightBlueBrickNib.clone()
        lightBlueBrickNextNib.move(100 *i, 0)
        lightBlueBrickNextNib.draw(win)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    # black brick
    blackBrick = redBrick.clone()
    blackBrick.setFill("black")
    blackBrick.move(0, 300)
    blackBrick.draw(win)

    # the inner red for the black brick
    innerBlackBrick= Rectangle(Point(590, 705), Point(1080, 875))
    innerBlackBrick.setOutline("dark red")
    innerBlackBrick.draw(win)

    # black brick
    blackBrickNib = redBrickNib.clone()
    blackBrickNib.setFill("black")
    blackBrickNib.move(0, 300)
    blackBrickNib.draw(win)

    # inner red for the nib
    innerBlackBrickNib = Rectangle(Point(610, 682), Point(660, 699))
    innerBlackBrickNib.setOutline("dark red")
    innerBlackBrickNib.draw(win)

    # dupeing nibs
    
    for i in range(1, 5):
        blackBrickNextNib = blackBrickNib.clone()
        innerBlackBrickNextNib = innerBlackBrickNib.clone()
        blackBrickNextNib.move(100 *i, 0)
        innerBlackBrickNextNib.move(100 * i, 0)
        blackBrickNextNib.draw(win)
        innerBlackBrickNextNib.draw(win)
    
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    win.getMouse()

main()