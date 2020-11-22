import sys


def new_item():
    global list
    name = str(input("Name : "))
    list.append(name)
    print(f"{name} added")

def menu_text():
    global list
    if len(list) <= 0:
        cmd = str(input("(N)ew (Q)uit : "))
    else:
        cmd = str(input("(N)ew (S)how (D)elete (Q)uit : "))
    return cmd

def show_item():
    global list
    if len(list)==0:
        print("Incorrect Menu")
    else:
        for i in range(len(list)):
            print(f"({i + 1}) {list[i]}")


def delete_item():
    global list
    del_confirm = 0
    if len(list)==0:
        print("Incorrect Menu")
    else:
        while True:
            number = input("Number? : ")
            try:
                number = int(number)
            except ValueError:
                print("Not a number")
            else:
                while True:
                    if number <= 0 or number > len(list):
                        print("Not in range")
                        break
                    elif number == len(list):
                        del list[number - 1]
                        del_confirm = 1
                        break
                    else:
                        del list[number - 1]
                        for i in range(len(list)):
                            print(f"({i + 1}) {list[i]}")
                        del_confirm = 1
                        break
                if del_confirm == 1:
                    break


list = []
while True:
    ans = menu_text()
    if ans == "N" or ans == "n":
        new_item()
    elif ans == "S" or ans == "s":
        show_item()
    elif ans == "D" or ans == "d":
        delete_item()
    elif ans == "Q" or ans == "q":
        print("Bye")
        sys.exit()
    else:
        print("Incorrect Menu")