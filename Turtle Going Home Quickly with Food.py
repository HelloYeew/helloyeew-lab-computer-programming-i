LAB = "turtlelab3x.py"
import urllib.request
urllib.request.urlretrieve(f"http://elab.cpe.ku.ac.th/turtlelab/{LAB}",LAB)

from turtlelab3x import turtle,home,shop,check
from math import atan2,pi

#start to shop
angle_shop = (atan2(shop.y,shop.x))*180/pi
distance_shop = (((shop.y)**2)+((shop.x)**2))**0.5
turtle.left(angle_shop)
turtle.forward(distance_shop)
#set turtle's angle to zero
turtle.right(angle_shop)
#shop to home
angle_home = (atan2(home.y-shop.y,home.x-shop.x))*180/pi
distance_home = (((home.y-shop.y)**2)+((home.x-shop.x)**2))**0.5
turtle.left(angle_home)
turtle.forward(distance_home)

check()