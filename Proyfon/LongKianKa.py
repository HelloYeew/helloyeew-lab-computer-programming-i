team_list = []
team_name = []
win = []
lose = []
win_rate = []
dict1 = {}

# file = open("input2.txt").read().splitlines()

def open_file(file_name):
    with open(file_name) as f:
        team_list = f.readline()
        for i in range(len(team_list) - 1):
            print(team_list)
            if i < len(team_list) - 1:
                team_list[i] = team_list[i][:-1]
    print(team_list)

open_file("input1.txt")
for i in file:
    a = i.split(",")
    team_name.append(a[0])
    win.append(a[1])
    lose.append(a[2])

for i in range(len(team_name)):
    win_rate_cal = int(win[i]) / (int(win[i]) + int(lose[i]))
    win_rate.append(win_rate_cal)
    dict1[team_name[i]] = [win_rate[i]]

print(f"Total team(s): {len(team_name)}")
for k, v in dict1.items():
    print(f"{k}: got win rate {v:.5f}")