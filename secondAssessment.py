class Vehicle:
    def __init__(self, make, model, year, mileage = 0):
        self.make = make
        self.model = model
        self.year = year
        self.__mileage = mileage

    def drive(self, distance):
        self.__mileage += distance

    def get_info(self):
        return f"This is a {self.make}, {self.model}, a {self.year} model with {self.__mileage}"
    
    def __str__(self):
        pass


class Car(Vehicle):
    vehicle_type = "Car"
    def __init__(self, make, model, year, fuel_capacity, mileage=0):
        super().__init__(make, model, year, mileage)
        self.fuel_capacity = fuel_capacity
    
    def  get_info(self):
        return f"This is a {self.make}, {self.model}, a {self.year} model with {self.__mileage} and {self.fuel_capacity} litres fuel capacity"
    

class ElectricScooter(Vehicle):
    def __init__(self, make, model, year, battery_percentage, mileage=0):
        super().__init__(make, model, year, mileage)
        self.battery_percentage = battery_percentage
    
    def  get_info(self):
        return f"This is a {self.make}, {self.model}, a {self.year} model with {self.__mileage} and {self.battery_percentage} litres fuel capacity"
    