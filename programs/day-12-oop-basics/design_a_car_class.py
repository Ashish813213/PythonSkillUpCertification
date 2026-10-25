# Design a Car class with brand, model and year and print its details.
class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def displayDetails(self):
        print("Car Details:")
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Year:", self.year)


class Solution:
    def fun(self, brand, model, year):
        car = Car(brand, model, year)
        car.displayDetails()
