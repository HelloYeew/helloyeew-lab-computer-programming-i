player_list = []
player_list = open("team_a.txt").read().splitlines()
for i in range(len(player_list)):
    player_list[i] = player_list[i].split(",")
print(player_list)