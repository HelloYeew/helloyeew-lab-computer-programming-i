class Cell:
    def __init__(self,id,move,hold):
        self.__id = id
        self.__move = move
        self.__hold = hold
        self.__occupy_list = []

    @property
    def occupy_list(self):
        return self.__occupy_list

    def get_occupy_list_str(self):
        listt = []
        for i in self.__occupy_list:
            listt.append(f"{i.name},")
        return "".join(listt)

    def add_occupy_list(self,x):
        self.__occupy_list.append(x)

    def remove_occupy_list(self,x):
        self.__occupy_list.remove(x)

    def __str__(self):
        return f"{self.__id},{self.__move},{self.__hold}"

    @property
    def id(self):
        return self.__id

    @property
    def move(self):
        return self.__move

    @move.setter
    def move(self,value):
        self.__current_move += value

    @property
    def hold(self):
        return self.__hold