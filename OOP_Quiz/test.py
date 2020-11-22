import time

class Route:
    def __init__(self):
        self.__all_route = []

    @property
    def all_route(self):
        return self.__all_route

    @all_route.setter
    def all_route(self,name):
        self.__all_route.append(name)

    def add_route(self,name):
        self.__all_route.append(name)

class Bus:
    def __init__(self):
        self.__in_route = []
        self.__status = []
        self.__time = []
        self.__start_time = 0

    @property
    def in_route(self):
        return self.__in_route

    @property
    def status(self):
        return self.__status

    @property
    def time(self):
        return self.__time

    @in_route.setter
    def in_route(self,in_route):
        self.__in_route.append(in_route)

    @status.setter
    def status(self,status):
        self.__status.append(status)

    @time.setter
    def time(self,time):
        self.__time.append(time)


    def display_route(self,number):
        print(f"Round {number} : {route.all_route[number - 1]}")
        for i in range(len(self.__in_route[number-1])):
            print(f"{i + 1}.{self.in_route[number - 1][i]} is {self.status[number - 1][i]} (Current {self.time[number - 1][i][0]} secs / All {self.time[number - 1][i][1]} secs")

    def run(self):
        self.__start_time = time.time()

    def time_elapse(self,group,code):
        elapse = time.time() - self.__start_time
        self.time[group - 1][code][1] = elapse




# class App:

import time
def current_time():
    return time.time()

route = Route()
in_route = Bus()
while True:
    main_input = input("(n)ew Route, (s)how, (c)hoose, (q)uit : ")
    if main_input == "n":
        route_name = input("Enter route name : ")
        route.add_route(route_name)
        for i in range(len(route.all_route)):
            print(f"Round {i+1} : {route.all_route[i]}")
    elif main_input == "s":
        for i in range(len(route.all_route)):
            print(f"Round {i+1} : {route.all_route[i]}")
    elif main_input == "c":
        choose_route_number = int(input("Enter a route number: "))
        while True:
            choose_input = input("(a)dd bus, (p)rint, (r)un/stop, (m)ain menu : ")
            if choose_input == "a":
                bus_code = input("Bus Code : ")
                in_route.in_route(bus_code)
                in_route.status("Stop")
                in_route.time([0,0])
            elif choose_input == "p":
                in_route.display_route(choose_route_number)
            elif choose_input == "r":
                in_route.run()
                in_route.display_route(choose_route_number)
            elif choose_input == "m":
                break






# while True:
#     menu = input("(s)tart, (e)lapse, (q)uit: ")
#     if menu == "s":
#         start = current_time()
#     elif menu == "e":
#         elapse = current_time() - start
#         print(f"{elapse:.0f} seconds")
#     elif menu == "q":
#         stop = current_time()
#         difference = int(stop-start)
#         print(f'Total {difference} seconds')
#         break
#     else:
#         print("Incorrect Menu")