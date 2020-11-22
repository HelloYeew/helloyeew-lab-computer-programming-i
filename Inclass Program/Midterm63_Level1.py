import sys


def new():
    global list
    name = str(input("Name : "))
    list.append(name)
    print(f"{name} added")


def show():
    global list
    for i in range(len(list)):
        print(f"({i + 1}) {list[i]}")


def quit():
    print("Bye")
    sys.exit()


list = []
while True:
    if len(list) <= 0:
        cmd = str(input("(N)ew (Q)uit : "))
        if cmd == "N" or cmd == "n":
            new()
        elif cmd == "Q" or cmd == "q":
            quit()
        else:
            print("Incorrect Menu")
    else:
        cmd = str(input("(N)ew (S)how (Q)uit : "))
        if cmd == "N" or cmd == "n":
            new()
        elif cmd == "S" or cmd == "s":
            show()
        elif cmd == "Q" or cmd == "q":
            quit()
        else:
            print("Incorrect Menu")
