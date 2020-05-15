# Module 5
#   Programming Assignment 6
#       Prob-4.py

# <YOUR NAME>

from graphics import *


def main():

    win = GraphWin(title="Buildy Buildy House House", height=400, width=400)
    instruction1 = Text(Point(
        200, 20), "Let's build a house!\nClick in two different areas to define corners").draw(win)

    houseCorner1 = win.getMouse()
    houseCorner2 = win.getMouse()

    houseFrame = Rectangle(houseCorner1, houseCorner2)
    houseFrame.setOutline("black")
    houseFrame.setFill("beige")
    instruction1.undraw()
    houseFrame.draw(win)

    houseX1 = houseCorner1.getX()
    houseX2 = houseCorner2.getX()

    houseY1 = houseCorner1.getY()
    houseY2 = houseCorner2.getY()

    if houseY1 > houseY2:
        bottomLeft = houseY1
        topRight = houseY2
    else:
        bottomLeft = houseY2
        topRight = houseY1

    if houseX1 < houseX2:
        topLeft = houseX1
        bottomRight = houseX2
    else:
        topLeft = houseX2
        bottomRight = houseX1

    frameTopLeft = Point(topLeft, topRight)
    frameTopRight = Point(bottomRight, topRight)

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    instruction2 = Text(Point(
        200, 20), "Next, click where you would like\nthe center of the top of the door").draw(win)

    clickDoor = win.getMouse()
    doorX = clickDoor.getX()
    doorY = clickDoor.getY()

    doorHeight = bottomLeft
    '''
    if houseY1 > houseY2:
        doorHeight = houseY1
    else:
        doorHeight = houseY2
    '''
    doorWidth = (((houseX2 - houseX1)/5)/2)
    doorFrameX1 = doorX - doorWidth
    doorFrameX2 = doorX + doorWidth

    doorFrame = Rectangle(Point(doorFrameX1, doorY),
                          Point(doorFrameX2, doorHeight))

    doorFrame.setOutline("black")
    doorFrame.setFill("brown")
    doorFrame.draw(win)
    instruction2.undraw()

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    instruction3 = Text(Point(
        200, 20), "Why don't we put up a nice little window.\nClick where you would like one.").draw(win)

    windowCenter = win.getMouse()
    windowclickX = windowCenter.getX()
    windowclickY = windowCenter.getY()

    windowWidth = doorWidth/2
    windowX1 = windowclickX - windowWidth
    windowY1 = windowclickY - windowWidth
    windowX2 = windowclickX + windowWidth
    windowY2 = windowclickY + windowWidth

    windowFrame = Rectangle(Point(windowX1, windowY1),
                            Point(windowX2, windowY2))

    windowFrame.setOutline("black")
    windowFrame.setFill("blue")
    windowFrame.draw(win)
    instruction3.undraw()

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    instruction4 = Text(Point(
        200, 20), "Last, please click where you would like\nthe peak of the roof to be.").draw(win)

    housePeak = win.getMouse()

    p1 = frameTopLeft
    p2 = housePeak
    p3 = frameTopRight

    roofFrame = Polygon(p1, p2, p3)

    instruction4.undraw()
    roofFrame.setOutline("black")
    roofFrame.setFill("red")
    roofFrame.draw(win)

    input()


main()
