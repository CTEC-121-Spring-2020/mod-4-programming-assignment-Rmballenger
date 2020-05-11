# Module 5
#   Programming Assignment 6
#       Prob-1.py

# Robert Ballenger

# INSTRUCTIONS:
#   Insert a comment above each line of code in the program below to describe
#   what the code does

# Grab the graphics.py file
from graphics import *

def main():
     # Create a window using graphics.py
     win = GraphWin()

     # Create a circle at x50 y50 with a radius of 20. Call it 'shape'.
     shape = Circle(Point(50,50), 20)

     # Set the outline for shape to the color red.
     shape.setOutline("red")

     # Set the color to fill in shape with to red as well.
     shape.setFill("red")

     # Have the program draw the shape. Without this, it woulnd't appear.
     shape.draw(win)

     # Do the following for the next 5 times.
     for i in range(5):

          # Get the Mouse location when clicked, and assign it to 'p'.
          p = win.getMouse()

          # Get the location of the where the center of the shape currently is, and assign it to 'c'.
          c = shape.getCenter()

          # Find how far on the X value away the shape is from the new mouse clicked location.
          # Assign it to the value 'dx'
          dx = p.getX() - c.getX()

          # Find how far on the Y value away the shape is from the new mouse clicked location.
          # Assign it to the value 'dy'         
          dy = p.getY() - c.getY()
          
          # Move the shape to the location of the mouse click.
          shape.move(dx,dy)
     
     # After clicking 5 times, close the window.
     win.close()

main()