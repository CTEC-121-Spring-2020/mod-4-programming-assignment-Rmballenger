# Module 5
#   Programming Assignment 6
#       Prob-5.py

# Robert Ballenger

from graphics import *

def main():
    win = GraphWin(title="Wheely Wheely toot toot", height=400, width=800)
    instruction1 = Text(Point(
        400, 20), "Look at this magestic car!").draw(win)

    # Wheels up first! Did some inner and outer circles, then cloned them and moved them.
    frontOuterWheel = Circle(Point(200, 340), 50)
    frontOuterWheel.setFill("black")
    frontOuterWheel.draw(win)

    frontInnerWheel = Circle(Point(200, 340), 40)
    frontInnerWheel.setOutline("white")
    frontInnerWheel.setFill("grey")
    frontInnerWheel.draw(win)

    backOuterWheel = frontOuterWheel.clone()
    backOuterWheel.move(400, 0)
    backOuterWheel.draw(win)

    backInnerWheel = frontInnerWheel.clone()
    backInnerWheel.move(400, 0)
    backInnerWheel.draw(win)


    # Next up is the upper half of the car. I want it partly hidden by the lower half so I'm having it draw first.
    topHalf = Polygon(Point(200, 195), Point(290, 90), Point(540, 90), Point(621, 195))
    topHalf.setOutline("black")
    topHalf.setFill("red")
    topHalf.draw(win)

    # Now we begin on our bottom half of the car. A nice rectangle should do.
    bottomHalf = Rectangle(Point(70, 321), Point(728, 185))
    bottomHalf.setOutline("black")
    bottomHalf.setFill("maroon")
    bottomHalf.draw(win)

    # Next some windows
    carWindows = Polygon(Point(250, 180), Point(300, 110), Point(530, 110), Point(575, 180))
    carWindows.setOutline("black")
    carWindows.setFill("lightblue")
    carWindows.draw(win)

    # A split to seperate them...
    windowSplit = Line(Point(409, 110), Point(409, 180))
    windowSplit.draw(win)

    # Last some circles for a front and back bumper.
    frontBumper = Circle(Point(80, 275), 50)
    frontBumper.setFill("black")
    frontBumper.draw(win)

    backBumper = frontBumper.clone()
    backBumper.move(640, 0)
    backBumper.draw(win)


    # This is how I went about getting the coord locations for the  Polygons.
    '''
    click1 = win.getMouse()
    click1.draw(win)
    click2 = win.getMouse()
    click2.draw(win)
    click3 = win.getMouse()
    click3.draw(win)
    click4 = win.getMouse()
    click4.draw(win)

    print(click1, click2, click3, click4)
    '''

    Text(Point(400, 380), "Click again to quit...").draw(win)
    win.getMouse()


main()