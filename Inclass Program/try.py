teamlist = []

with open("input1.txt") as f:
    print(f)
    teamlist = f.readlines()
    print(teamlist)
    for i in range(len(teamlist)-1):
        if i < len(teamlist)-1:
            teamlist[i] = teamlist[i][:-1]
        print(teamlist)
    for i in range(len(teamlist)):
        teamlist[i] = teamlist[i].split(",")
        print(teamlist)
print(teamlist)