# Parent class (superclass)
class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def drive(self):
        print(f"{self.make} {self.model} is driving.")

# Child class (subclass) inheriting from Vehicle
class Car(Vehicle):
    def __init__(self, make, model, year):
        # Call the constructor of the parent class
        super().__init__(make, model)
        self.year = year

    def honk(self):
        print(f"{self.make} {self.model} goes 'Honk, honk!'")

# Example usage:
my_car = Car("Toyota", "Camry", 2022)
print(f"My car is a {my_car.year} {my_car.make} {my_car.model}.")
my_car.drive()
my_car.honk()
