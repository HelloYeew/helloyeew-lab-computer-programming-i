LAB = "turtlelab5x.py"
import urllib.request

urllib.request.urlretrieve(f"http://elab.cpe.ku.ac.th/turtlelab/{LAB}", LAB)

from turtlelab5x import turtle, check, mickey, raph, leo, donnie

def definewalkandwalkback(x, y):
    # q1
    if x > 0 and y > 0:
        turtle.forward(x)
        turtle.left(90)
        turtle.forward(y)
        turtle.right(180)
        turtle.forward(y)
        turtle.right(90)
        turtle.forward(x)
        turtle.right(180)
    # q2
    elif x < 0 and y > 0:
        turtle.left(180)
        turtle.forward(x * -1)
        turtle.right(90)
        turtle.forward(y)
        turtle.right(180)
        turtle.forward(y)
        turtle.left(90)
        turtle.forward(x * -1)
    # q3
    elif x < 0 and y < 0:
        turtle.left(180)
        turtle.forward(x * -1)
        turtle.left(90)
        turtle.forward(y * -1)
        turtle.right(180)
        turtle.forward(y * -1)
        turtle.right(90)
        turtle.forward(x * -1)
    # q4
    elif x > 0 and y < 0:
        turtle.forward(x)
        turtle.right(90)
        turtle.forward(y * -1)
        turtle.left(180)
        turtle.forward(y * -1)
        turtle.left(90)
        turtle.forward(x)
        turtle.right(180)
    # on y
    elif x == 0:
        if y > 0:
            turtle.left(90)
            turtle.forward(y)
            turtle.right(180)
            turtle.forward(y)
            turtle.left(90)
        elif y < 0:
            turtle.right(90)
            turtle.forward(y * -1)
            turtle.left(180)
            turtle.forward(y * -1)
            turtle.right(90)
    # on x
    elif y == 0:
        if x > 0:
            turtle.forward(x)
            turtle.left(180)
            turtle.forward(x)
            turtle.left(180)
        elif x < 0:
            turtle.right(180)
            turtle.forward(x * -1)
            turtle.right(180)
            turtle.forward(x * -1)


definewalkandwalkback(raph.x, raph.y)
definewalkandwalkback(mickey.x, mickey.y)
definewalkandwalkback(leo.x, leo.y)
definewalkandwalkback(donnie.x, donnie.y)
check()
