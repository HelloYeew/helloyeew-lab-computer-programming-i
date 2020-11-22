LAB = "turtlelab6.py"
import urllib.request
urllib.request.urlretrieve(f"http://elab.cpe.ku.ac.th/turtlelab/{LAB}.6",LAB)

from turtlelab6 import turtle,home,crush,koopa,check
from math import atan2,pi

crush_koopa_home_dis = ((crush.x**2 + crush.y**2)**0.5)+((((koopa.x-crush.x)**2) + ((koopa.y-crush.y)**2))**0.5) + ((((home.x-koopa.x)**2) + ((home.y-koopa.y)**2))**0.5)
koopa_crush_home_dis = ((koopa.x**2 + koopa.y**2)**0.5)+((((crush.x-koopa.x)**2) + ((crush.y-koopa.y)**2))**0.5) + ((((home.x-crush.x)**2) + ((home.y-crush.y)**2))**0.5)
if crush_koopa_home_dis < koopa_crush_home_dis:
    # start to crush
    angle_origin_crush = (atan2(crush.y, crush.x)) * 180 / pi
    distance_origin_crush = (((crush.y) ** 2) + ((crush.x) ** 2)) ** 0.5
    # check turtle want to rotate right or left to crush
    if