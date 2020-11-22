class Car:
    def __init__(self,brand="_",model="_",price="_"):
        self.__brand = brand
        self.__model = model
        self.__price = price

    @property
    def brand(self):
        return self.__brand

    @property
    def model(self):
        return self.__model

    @property
    def price(self):
        return self.__price

    @brand.setter
    def brand(self,brand):
        self.__brand = brand

    @model.setter
    def model(self,notmodel):
            self.__model = notmodel

    @price.setter
    def price(self,price):
        self.__price = price


    def __str__(self):
        return str(f"Brand: {self.__brand} , Model: {self.__model}, Price: {self.__price}")

def compare(car1,car2):
    print(car1)
    print(car2)

# 1
car1 = Car()

print(car1)

car1.brand = "Toyota"

print(car1)

car1.model = "Vios"
car1.price = 500000

print(car1)

car2 = Car("BMW","X3",3500000)

print(car2)
car2.price = 2000000

print(car2)

print("----------------------")
# 2

car1 = Car("Nissan","Tiida",450000)
car2 = Car("Toyota","Vios",400000)
car3 = Car("BMW","X3",3400000)

compare(car3,car1)
compare(car1,car2)