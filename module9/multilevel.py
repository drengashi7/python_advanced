class Vehicle:
    def __int__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
         print(f"Make: {self.make}, Model:{self.model}, Year:{self.year}")

class Car(Vehicle):
    def __int__(self, make, year, body_style):
        super().__int__(make,model,year)
        self.body_style = body_style


class ElectricalCar(Car):
    def __init__(self,make ,model ,year, body_style, battery_capacity):
        super().__int__(make, model, year, body_style)
        self.battery_capacity = battery_capacity

    def charger(self):
        print("Charging the electric car.")

tesla = ElectricalCar("tesla", "cybertruck", "2023", "triangular",112)
tesla.display_info()
print(tesla.body_style)
print(tesla.battery_capacity)
tesla.charger()
