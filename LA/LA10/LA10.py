class Vehicle:
  def __init__(self, brand, model, fuel_type):
    self.brand = brand
    self.model = model
    self.fuel_type = fuel_type
  def describe_vehicle(self):
    return f"{self.brand} {self.model} is a motorcyle/car tha have a {self.fuel_type} fuel type."
  
class Car(Vehicle):
  pass
class Motorcycle(Vehicle):
  pass

vehicle1 = Car("Audi", "R9", "Gasoline")
vehicle2 = Motorcycle("Yamaha", "R1000", "Gasoline")

print(vehicle1.describe_vehicle())
print(vehicle2.describe_vehicle())