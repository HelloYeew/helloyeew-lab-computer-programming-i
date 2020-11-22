from cell import *
from player import *

class Board:
    def __init__(self,filename):
        self.__width = 0
        self.__length = 0
        self.__cell_list = self.read_board(filename)

    @property
    def width(self):
        return self.__width

    @property
    def length(self):
        return self.__length

    def read_board(self,filename):
        file = []
        open_file = open(filename, "r")
        self.__width = open_file.readline().strip()
        self.__length = open_file.readline().strip()
        for i in open_file.read().splitlines():
            file.append(Cell(i.split(",")[0], i.split(",")[1], i.split(",")[2].strip()))
        return file

    def add_player(self,name):
        self.__cell_list[0].add_occupy_list(name)

    @property
    def cell_list(self):
        return self.__cell_list

    # @property
    def access_cell(self,cell_id):
        return self.__cell_list[int(cell_id)]

    def check_winner(self):
        # if self.access_cell(self.cell_list[-1].id).get_occupy_list_str() != "":
        #     return False
        # else:
        #     return True
        if self.access_cell(self.cell_list[-1].id).get_occupy_list_str() == "":
            return False
        else:
            return True

    def get_winner(self):
        if self.check_winner():
            return "Game Over! {0} wins".format(self.access_cell(self.cell_list[-1].id).occupy_list[0].name)
        else:
            return None

    def update_board(self,player):
        # if player.current_hold == False:
        #     self.access_cell(player.current_pos).remove_occupy_list(player)
        #     player.move(self)
        #     player.obtain_cell_status(self)
        #     self.access_cell(player.current_pos).add_occupy_list(player)
        # else:
        #     pass
        if player.current_hold == True:
            pass
        else:
            self.access_cell(player.current_pos).remove_occupy_list(player)
            player.move(self)
            player.obtain_cell_status(self)
            self.access_cell(player.current_pos).add_occupy_list(player)

    def __str__(self):
        return_board = ""
        self.__width = int(self.__width)
        self.__length = int(self.__length)
        board_chong = self.__length*self.__width
        run_board_id_one = 0
        run_board_id_two = 1
        run_board_id_three = 1
        for i in range(self.__length):
            return_board += ("--------" * self.__length)+"\n"
            for j in range(self.__width):
                for k in range(self.__length):
                    return_board += f"|{run_board_id_one:^6}"
                    run_board_id_one += 1
                return_board += "|" + "\n"
                for l in range(self.__length):
                    if self.__cell_list[run_board_id_two-1].hold == "TRUE":
                        sohard = "T"
                    else:
                        sohard = "F"
                    ilovecat = f"{self.__cell_list[run_board_id_two-1].move},{sohard}"
                    return_board += f"|{ilovecat:^6}"
                    run_board_id_two += 1
                return_board += "|" + "\n"
                for m in range(self.__length):
                    return_board += f"|{self.__cell_list[run_board_id_three-1].get_occupy_list_str():<6}"
                    run_board_id_three += 1
                return_board += "|" + "\n"
                return_board += ("--------" * self.__length)+"\n"
            if run_board_id_one == board_chong-1:
                return_board += ("--------" * self.__length)+"\n"
                break
            break
        return return_board







