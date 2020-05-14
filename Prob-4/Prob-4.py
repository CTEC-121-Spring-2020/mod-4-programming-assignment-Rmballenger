# Module 5
#   Programming Assignment 6
#       Prob-4.py

# <YOUR NAME>

from graphics import *

def main():

    win = GraphWin(title= "Buildy Buildy House House", height=400, width=400)
    firstInstruction = Text(Point(200, 20), "Let's build a house!\n Click in two different areas to define corners").draw(win)

    houseCorner1 = win.getMouse()
    houseCorner2 = win.getMouse()

    houseFrame = Rectangle(houseCorner1, houseCorner2)
    houseFrame.setOutline("black")
    houseFrame.setFill("beige")
    firstInstruction.undraw()
    houseFrame.draw(win)



    input()
    
"""

        Bonus = Text(Point(200, 20), "Bonus Round!").draw(win)
    win.getMouse()
    Bonus.undraw()
    win = GraphWin(title="Clicky Clicky Square Square", height=400, width=400)
    shape = Rectangle(Point(10, 40), Point(40, 10))
    shape.setOutline("red")
    shape.setFill("red")
    shape.draw(win)

    # The for loop gets slightly changed, instead of having c being the center of the shape, I assign it to the first point of the originally defined rectangle, which I made sure Point 1 was the bottom left for the assignment requirement. The math is still the same, however I added a variable called 'shapeCopy' so when the clicks happen it creates a new one and moves/draws it.
    for i in range(5):
        p = win.getMouse()
        c = shape.getP1()
"""


main()
