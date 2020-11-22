from car import *

def compare(car1,car2):
    print(car1)
    print(car2)

car1 = Car("Nissan","Tiida",450000)
car2 = Car("Toyota","Vios",400000)
car3 = Car("BMW","X3",3400000)

compare(car3,car1)
compare(car1,car2)