class Appliance:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model
  def operate(self):
     print("Operating!")

class WashingMachine(Appliance):
  def operate(self):
    print("Washing clothes!")

class Refrigerator(Appliance):
  def operate(self):
    print("Keeping food cold!")

class Microwave(Appliance):
  def operate(self):
    print("Heating food!")

washing_machine = WashingMachine("Fujidenzo", "WMX123")
refrigerator = Refrigerator("Panasonic", "RF200")
microwave = Microwave("LG", "MH6565DIS ")


appliances = [washing_machine, refrigerator, microwave]

for appliance in appliances:
    appliance.operate()