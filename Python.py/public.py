class Car:
    def __init__(self,brand,price):
        self.brand=brand
        self.price=price

car1=Car("Toyota",30000)
print("Brand:",car1.brand)

class Bike(Car):
    def __init__(self,brand,price):
        super().__init__(brand,price)
        self.brand=brand
        self.price=price
bike1=Bike("Yamaha",15000)
print("Brand:",car1.brand)