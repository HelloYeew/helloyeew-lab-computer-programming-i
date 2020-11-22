class App:
    def __init__(self,name,watt,device):
        self.__name = name
        self.__watt = watt
        self.__status = device

    @property
    def name(self):
        return self.__name

    @property
    def watt(self):
        return self.__watt

    @property
    def status(self):
        return self.__status

    @name.setter
    def name(self,name):
        self.__name = name

    @watt.setter
    def watt(self,watt):
        self.__watt = watt

    @status.setter
    def status(self,status):
        self.__status = status

    def __str__(self):
        return [self.name,self.watt,self.status]


alldevice = []

while True:
    print("(a)dd device, (s)how device, (q)uit")
    ans = input()
    if ans == "a":
        name = input("Device name : ")
        watt = input("Watt : ")
        status = input("On or Off? : ")
        appendthing = App(name,watt,status)
        alldevice.append(appendthing)

    elif ans == "s":
        for i in alldevice:
            print(f"{i.name} {i.watt} Watts is {i.status}")

    elif ans == "q":
        print("bye")
        break