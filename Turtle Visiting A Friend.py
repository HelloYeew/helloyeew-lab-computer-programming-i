LAB = "turtlelab5.py"
import urllib.request

urllib.request.urlretrieve(f"http://elab.cpe.ku.ac.th/turtlelab/{LAB}.9", LAB)

from turtlelab5 import turtle, mario, check

# q1
if mario.x > 0 and mario.y > 0:
    turtle.forward(mario.x)
    turtle.left(90)
    turtle.forward(mario.y)
# q2
elif mario.x < 0 and mario.y > 0:
    turtle.left(180)
    turtle.forward(mario.x * -1)
    turtle.right(90)
    turtle.forward(mario.y)
# q3
elif mario.x < 0 and mario.y < 0:
    turtle.left(180)
    turtle.forward(mario.x * -1)
    turtle.left(90)
    turtle.forward(mario.y * -1)
# q4
elif mario.x > 0 and mario.y < 0:
    turtle.forward(mario.x)
    turtle.right(90)
    turtle.forward(mario.y * -1)
# on y
elif mario.x == 0:
    if mario.y > 0:
        turtle.left(90)
        turtle.forward(mario.y)
    elif mario.y < 0:
        turtle.right(90)
        turtle.forward(mario.y * -1)
# on x
elif mario.y == 0:
    if mario.x > 0:
        turtle.forward(mario.x)
    elif mario.x < 0:
        turtle.right(180)
        turtle.forward(mario.x * -1)
check()
