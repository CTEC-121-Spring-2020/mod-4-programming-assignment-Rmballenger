# Module 5
#   Programming Assignment 6
#       Prob-3.py

# Robert Ballenger

from graphics import *

def main():
    win = GraphWin(title="Shooty Shooty Bow Target", height=400, width=400)
    
    # Little bit of shorthand, instead of writing "Point(200, 200)" for the middle of each circle, I just assigned it a variable.
    center = Point(200, 200)

    # First up we work the white circle. The 160 radius seems random, but it's beceause this was the last one I started with.
    whiteC = Circle(center, 160)
    whiteC.setFill("white")
    whiteC.draw(win)

    # Notice here how the black circl is 30 radius smaller... HMMM.
    blackC = Circle(center, 120)
    blackC.setFill("black")
    blackC.draw(win)

    # Blue, just like the rest.
    blueC = Circle(center, 90)
    blueC.setFill("blue")
    blueC.draw(win)

    # Almost done, we do red, which is 30 less on the radius.
    redC = Circle(center, 60)
    redC.setFill("red")
    redC.draw(win)

    # This last one draws a yellow circle with a radius of 30, which is where I actually started.
    yellowC = Circle(center, 30)
    yellowC.setFill("yellow")
    yellowC.draw(win)

    # This last command just keeps the window open until the user clicks, with text to accompany it.
    Text(Point(200, 385), "Click again to quit.").draw(win)
    win.getMouse()

 
main()
