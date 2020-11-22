from board import *
from cell import *

class Player:
    def __init__(self,name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    def __str__(self):
        return f"{self.__name}: Pos = 0: Hold = False: Move = 0"