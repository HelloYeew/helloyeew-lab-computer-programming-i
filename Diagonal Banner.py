msg = str(input("What is your message? "))
msg.split
space = " "
for i in range(len(msg)):
    print(f"{space*i}{msg[i]}")