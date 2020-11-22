import random

class Player:
    def __init__(self,name='None',num_wins=0,num_plays=0):
        self.__name = name
        self.__num_wins = num_wins
        self.__num_plays = num_plays
        self.__hand = None

    def __str__(self):
        output = f"{self.__name}: Wins = {self.__num_wins}: Plays = {self.__num_plays} Hand = {self.__hand}"
        return output

    def get_name(self):
        return self.__name

    def set_name(self,value):
        self.__name = value

    def get_num_wins(self):
        return self.__num_wins

    def set_num_wins(self,value):
        self.__num_wins = value

    @property
    def num_plays(self):
        return self.__num_plays

    @num_plays.setter
    def num_plays(self,value):
        self.__num_plays = value

    @property
    def hand(self):
        return self.__hand

    @hand.setter
    def hand(self,value):
        self.__hand = value

    def randomize_hand(self):
        x = random.randint(1, 3)
        if x == 1:
            self.hand = 'Rock'
        elif x == 2:
            self.hand = 'Paper'
        else:
            self.hand = 'Scissors'