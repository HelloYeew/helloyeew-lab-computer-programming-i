import time
def current_time():
    return time.time()

while True:
    menu = input("(s)tart, (e)lapse, (q)uit: ")
    if menu == "s":
        start = current_time()
    elif menu == "e":
        elapse = current_time() - start
        print(f"{elapse} seconds")
    elif menu == "q":
        stop = current_time()
        difference = int(stop-start)
        print(f'Total {difference} seconds')
        break
    else:
        print("Incorrect Menu")