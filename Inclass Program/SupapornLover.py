import sys


def open_file(file_name):
    with open(file_name) as f:
        team_list = f.readlines()
        for i in range(len(team_list) - 1):
            if i < len(team_list) - 1:
                team_list[i] = team_list[i][:-1]
    for i in range(len(team_list)):
        team_list[i] = team_list[i].split(",")
    return team_list


def first_print():
    global team_list
    for i in range(len(team_list)):
        team_list[i][1] = int(team_list[i][1])
        team_list[i][2] = int(team_list[i][2])
        win_rate = team_list[i][1] / (team_list[i][1] + team_list[i][2])
        print(f"{team_list[i][0]}: got win rate {win_rate:.5f}")
        team_list[i].append(win_rate)
    print("==========")
    maximum_win_rate, minimum_win_rate = return_max_min()
    for i in range(len(team_list)):
        if maximum_win_rate in team_list[i]:
            print(f"{team_list[i][0]} got maximum win rate {maximum_win_rate:.5f}")
    for i in range(len(team_list)):
        if minimum_win_rate in team_list[i]:
            print(f"{team_list[i][0]} got maximum win rate {minimum_win_rate:.5f}")


def return_max_min():
    global team_list
    list = []
    for i in range(len(team_list)):
        list.append(team_list[i][3])
    return max(list), min(list)


def minimum():
    global team_list
    maxi, mini = return_max_min()
    for i in range(len(team_list)):
        if mini in team_list[i]:
            print(f"{team_list[i][0]} got minimum win rate {mini:.5f}")


def maximum():
    global team_list
    maxi, mini = return_max_min()
    for i in range(len(team_list)):
        if maxi in team_list[i]:
            print(f"{team_list[i][0]} got maximum win rate {maxi:.5f}")


def order_max_min():
    global team_list
    list = []
    for i in range(len(team_list)):
        list.append(team_list[i][3])
    list.sort(reverse=True)
    print(f"Total team(s) : {len(team_list)}")
    for j in range(len(list)):
        for k in range(len(list)):
            if list[j] == team_list[k][3]:
                print(f"{team_list[k][0]} got win rate {team_list[k][3]:.5f}")


def order_min_max():
    global team_list
    list = []
    for i in range(len(team_list)):
        list.append(team_list[i][3])
    list.sort()
    print(f"Total team(s) : {len(team_list)}")
    for j in range(len(list)):
        for k in range(len(list)):
            if list[j] == team_list[k][3]:
                print(f"{team_list[k][0]} got win rate {team_list[k][3]:.5f}")


file_name = str(input("Enter a file name: "))
team_list = open_file(file_name)
print(f"Total team(s) : {len(team_list)}")
first_print()
print()
while True:
    menu = str(input("What do you want to know ? (m)in , ma(x), (o)rder max to min, o(r)der min to max, (q)uit : "))
    if menu == "m":
        print()
        minimum()
        print()
    elif menu == "x":
        print()
        maximum()
        print()
    elif menu == "o":
        print()
        order_max_min()
        print()
    elif menu == "r":
        print()
        order_min_max()
        print()
    elif menu == "q":
        print("Bye")
        sys.exit()
