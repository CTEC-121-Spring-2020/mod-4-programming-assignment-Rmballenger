# Module 5
#   Programming Assignment 6
#       Prob-2.py

# Robert Ballenger

from graphics import *


def main():
    # To start, I created a size requirement for the window as it was giving me a hard time seeing everything. I changed the circle to rectangle and adjusted the points. Other than that the rest is the same.

    win = GraphWin(title="Clicky Clicky Square Square", height=400, width=400)
    shape = Rectangle(Point(10, 40), Point(40, 10))
    shape.setOutline("red")
    shape.setFill("red")
    shape.draw(win)

    # The for loop gets slightly changed, instead of having c being the center of the shape, I assign it to the first point of the originally defined rectangle, which I made sure Point 1 was the bottom left for the assignment requirement. The math is still the same, however I added a variable called 'shapeCopy' so when the clicks happen it creates a new one and moves/draws it.
    for i in range(5):
        p = win.getMouse()
        c = shape.getP1()
        dx = p.getX() - c.getX()
        dy = p.getY() - c.getY()
        shapeCopy = shape.clone()
        shapeCopy.move(dx, dy)
        shapeCopy.draw(win)

    # Text to show bonus starting.
    Bonus = Text(Point(200, 20), "Bonus Round!").draw(win)
    win.getMouse()
    Bonus.undraw()

    # Another for loop, same thing as before but changed shape.getP1 to getCenter.
    for i in range(5):
        p = win.getMouse()
        c = shape.getCenter()
        dx = p.getX() - c.getX()
        dy = p.getY() - c.getY()
        shapeCopy = shape.clone()
        shapeCopy.move(dx, dy)
        shapeCopy.draw(win)

    # Same as above for text, just changed point location and text itself. Followed by a getMouse to close the window.
    Text(Point(200, 375), "Click again to quit.").draw(win)
    win.getMouse()
    win.close()


main()
