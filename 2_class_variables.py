#Task 1

class Car:
    wheels = 4
    cars_in_garage = 0

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

        Car.cars_in_garage+=1

    def describe(self):
        print(f'{self.brand} {self.model} has {self.wheels} wheels')

car1 = Car("Toyota", "Corolla")
car2 = Car("Honda", "Civic")
car3= Car("Porsche", "911 GT3 RS")
car1.describe()
car2.describe()
car3.describe()
print(Car.wheels)
print(Car.cars_in_garage)