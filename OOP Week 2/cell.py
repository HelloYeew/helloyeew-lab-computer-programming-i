from player import *

class Cell:
    def __init__(self,id,move,hold):
        self.__id = id
        self.__move = move
        self.__hold = bool(hold)
        self.occupy_list = []

    def occupy_list(self):
        return self.occupy_list

    def get_occupy_list_str(self):
        output = ""
        for i in self.occupy_list:
            output += i.name + ","
        return output

    def add_occupy_list(self,player):
        self.occupy_list.append(player)

    def remove_occupy_list(self,name):
        self.occupy_list.remove(name)

    def __str__(self):
        return f"{self.__id},{self.__move},{self.__hold}"