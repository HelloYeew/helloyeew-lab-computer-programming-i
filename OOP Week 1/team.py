import random
from player import *

class Team:
    def __init__(self, filename, team_name='No Name'):
        self.__player_list = self.__read_team(filename)
        self.__team_name = team_name
        self.__score = 0
        self.current_player = None
        self.team_point = 0

    def __read_team(self, filename):
        reader = open(filename).read().splitlines()
        temp = []
        player_list = []
        for i in range(len(reader)):
            temp.append(reader[i].split(","))
        for i in temp:
            player_list.append(Player(i[0],int(i[1]),int(i[2])))
        # for i in range(len(player_list)):
        #     player_list[i] = player_list[i].split(",")
        return player_list

    def __str__(self):
        output = ""
        output += f"Team {self.__team_name}\nTeam Points: {self.team_point} \n"
        for i in self.__player_list:
            output_temp = str(i)
            output += f"{output_temp}\n"
        return output

    def select_player(self):
        random_number = random.randint(0,len(self.__player_list)-1)
        self.__player_list[random_number].randomize_hand()
        player = self.__player_list[random_number]
        self.current_player = player

    def print_player_list(self):
        return self.__player_list

    def update_team_points(self, value):
        if value == 'win':
            self.team_point += 1

# team_a = Team('team_a.txt','A')
# print(team_a)
# team_b = Team('team_b.txt','B')
# print(team_b)
# print(team_a.select_player())
# # print(team_a.current_player)
# print(team_b.select_player())
# # print(team_b.current_player)
