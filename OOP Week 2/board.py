from cell import *

class Board:
    def __init__(self,filename):
        self.cell_list = ""
        self.length = 0
        self.width = 0
        self.board = []
        self.board = self.read_board(filename)

    def read_board(self,filename):
        reader = open(filename).read().splitlines()
        temp = []
        board = []
        self.width = reader[0]
        self.length = reader[1]
        for i in range(2,len(reader)):
            temp.append(reader[i].split(","))
        for i in temp:
            board.append(Cell(int(i[0]), int(i[1]), bool(i[2])))
            self.cell_list += f"{int(i[0])},{int(i[1])},{bool(i[2])}\n"
        return self.cell_list

    def add_player(self,player):
        self.cell_list.add_occupy_list(player)



    def __str__(self):
        return self.cell_list

print(Board("board1.txt").read_board("board1.txt"))