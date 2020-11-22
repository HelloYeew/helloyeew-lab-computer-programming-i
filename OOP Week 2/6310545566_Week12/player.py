import random

class Player:
    def __init__(self,name):
        self.__name = name
        self.__current_pos = 0
        self.__current_hold = False
        self.__current_move = 0

    def __str__(self):
        return f"{self.__name}: Pos = {self.__current_pos}: Hold = {self.__current_hold}: Move = {self.__current_move}"

    @property
    def name(self):
        return self.__name

    def move(self,board):
        if int(self.__current_move) > (int(board.cell_list[-1].id) - self.__current_pos):
            self.__current_pos = board.cell_list[-1].id
            self.__current_move = 0
        else :
            self.__current_pos += int(self.__current_move)
            self.__current_move = 0

    def obtain_cell_status(self,board):
        self.__current_hold = board.access_cell(self.__current_pos).hold
        self.__current_move = int(board.access_cell(self.__current_pos).move)

    def randomize_dice(self):
        self.__current_move = random.randint(1,6)

    @property
    def current_pos(self):
        return self.__current_pos

    @property
    def current_move(self):
        return self.__current_move

    @property
    def current_hold(self):
        return self.__current_hold