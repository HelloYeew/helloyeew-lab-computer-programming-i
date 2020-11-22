def find_winner(first_player, second_player):
    player1 = first_player.hand
    player2 = second_player.hand
    if player1 == "Rock":
        if player2 == "Rock":
            return 0
        elif player2 == "Paper":
            return 2
        else:
            return 1
    elif player1 == "Paper":
        if player2 == "Rock":
            return 2
        elif player2 == "Paper":
            return 0
        else:
            return 1
    else:
        if player2 == "Rock":
            return 2
        elif player2 == "Paper":
            return 1
        else:
            return 0

def update_points(winning_team, first_team, second_team):
    if winning_team == 1:
        print("A wins")
        first_team.team_point += 1
    elif winning_team == 2:
        print("B wins")
        second_team.team_point += 1
    else:
        print("Both team tie")

from team import *
team_a = Team('team_a.txt','A')
print(team_a)
team_b = Team('team_b.txt','B')
print(team_b)
while True:
    if team_a.team_point == 5:
        print("Team A wins!")
        break
    elif team_b.team_point == 5:
        print("Team B wins!")
        break

    team_a.select_player()
    print(team_a.current_player)

    team_b.select_player()
    print(team_b.current_player)

    team_a.update_team_points('win')
    print(team_a)
    team_b.update_team_points('lose')
    print(team_b)

    winning_team = find_winner(team_a.current_player, team_b.current_player)
    print(winning_team)

    update_points(winning_team, team_a, team_b)
    print(team_a)
    print(team_b)