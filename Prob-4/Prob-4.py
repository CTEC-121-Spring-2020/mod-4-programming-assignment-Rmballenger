# Module 5
#   Programming Assignment 6
#       Prob-4.py

# Robert Ballenger

from graphics import *


def main():

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    #               Prep/Frame
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    # To start, I create a window with a title and size specs. I also add a bit of text to tell the user what I'd like them to do.
    win = GraphWin(title="Buildy Buildy House House", height=400, width=400)
    instruction1 = Text(Point(
        200, 20), "Let's build a house!\nClick in two different areas to define corners").draw(win)

    # Here I define some variables. I grab the first two clicks and get the X and Y value of each as well. I also created a point for each click so the user can better see that its working and where they clicked.
    click1 = win.getMouse()
    click1.draw(win)
    click2 = win.getMouse()
    click2.draw(win)

    houseX1 = click1.getX()
    houseY1 = click1.getY()

    houseX2 = click2.getX()
    houseY2 = click2.getY()

    # A set of if/else statements create some variables that will com up later. Essentually it's finding out which corner of the house is which by finding out if the user started with a top corner or a bottom corner when defining the shape.
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

    # Similar, here I define two variables to the top left and top right of the house frame that the user creates. Using the if/else above I make sure that if the user starts with the top or the bottom, the variables here always are the top left and right.
    frameTopLeft = Point(topLeft, topRight)
    frameTopRight = Point(bottomRight, topRight)

    # Finally we come to the drawing of the frame itself. A rectangle shape using the two clicks as corner points, a black frame so it shows a little better and even through in color.
    houseFrame = Rectangle(click1, click2)
    houseFrame.setOutline("black")
    houseFrame.setFill("beige")
    houseFrame.draw(win)

    # Just cleaning up the garbage.
    click1.undraw()
    click2.undraw()
    instruction1.undraw()

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    #               Door
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    # Now we begin the create a door section! Some instructions to help guide the user...
    instruction2 = Text(Point(
        200, 20), "Next, click where you would like\nthe center of the top of the door").draw(win)

    # Adding some more variables here! We have a new click variable to give us an X and Y position. 
    click3 = win.getMouse()
    doorX = click3.getX()
    doorY = click3.getY()

    # We know the door has to be 1/5 the width of the house. So using the points from above when we defined the corners of the house, we can find the width. Now the secret here is in the /2 at the end of it all. I want the point where the user clicks to be the center of the top, so I need to take half the doors width.
    halfDoorWidth = (((houseX2 - houseX1)/5)/2)
    
    # Now I use this to find three of the four coord points for the door. I only need the y value that tells how tall the door is. Luckily I have that from above as doorY.
    doorX1 = doorX - halfDoorWidth
    doorX2 = doorX + halfDoorWidth
    doorFloor = bottomLeft


    # Like the house frame above, now we add it all together using the coord points from above, add some outline and color and BAM! We got a door.
    doorFrame = Rectangle(Point(doorX1, doorY), Point(doorX2, doorFloor))
    doorFrame.setOutline("black")
    doorFrame.setFill("brown")
    doorFrame.draw(win)

    # Trash cleanup
    instruction2.undraw()

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    #               Window
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    # Onto the window section. More instructions to help out.
    instruction3 = Text(Point(
        200, 20), "Why don't we put up a nice little window.\nClick where you would like one.").draw(win)

    # Another variable made from the click with it's X and Y values taken from it.
    click4 = win.getMouse()
    windowclickX = click4.getX()
    windowclickY = click4.getY()

    # Knowing that I want the click point to be the center of the window, and that the window is a square, and the width of the window, I just half the width and walk my way to each corner from that center point to define the x and y points for the rectangle requirements.
    windowWidth = halfDoorWidth/2
    windowX1 = windowclickX - windowWidth
    windowY1 = windowclickY - windowWidth
    windowX2 = windowclickX + windowWidth
    windowY2 = windowclickY + windowWidth

    # Like before, here we draw out the window itself.
    windowFrame = Rectangle(Point(windowX1, windowY1), Point(windowX2, windowY2))
    windowFrame.setOutline("black")
    windowFrame.setFill("blue")
    windowFrame.draw(win)

    # Takin' out the trash.
    instruction3.undraw()

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    #               Roof
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    # Last bit of helpful text for the user
    instruction4 = Text(Point(
        200, 20), "Last, please click where you would like\nthe peak of the roof to be.").draw(win)

    # Last click taken, and variable assigned. I also grabbed the top left and top right variables created in the house frame section.
    click5 = win.getMouse()

    p1 = frameTopLeft
    p2 = click5
    p3 = frameTopRight

    # Now with my three points already defined, I ask the polygon to make the shape and we get our roof!
    roofFrame = Polygon(p1, p2, p3)
    roofFrame.setOutline("black")
    roofFrame.setFill("grey")
    roofFrame.draw(win)

    # More trash disposal and a goodbye message with a click to close.
    instruction4.undraw()

    instruction5 = Text(Point(
    200, 20), "Excellent! You built a house!\nClick again to quit...").draw(win)
    win.getMouse()


main()
