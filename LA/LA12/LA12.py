class Toy:
  def __init__(self, name, price):
    self.name = name
    self.price = price
  def describe_toy(self):
    print(f"This toy is a {self.name} with a price of {self.price}")

class Car(Toy):
  def __init__(self, name, price):
    super().__init__(name, price)

car1 = Car("Remote Control Car", "3000")
car1.describe_toy()
    