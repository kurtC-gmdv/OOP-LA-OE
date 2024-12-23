class Car:
  def __init__(self, brand, color):
    self.brand = brand
    self.color = color

car1 = Car("Audi", "Black")
print(car1.brand, car1.color)

car1.color = "white"
print(car1.brand, car1.color)

car2 = Car("Volkswagen", "Red")
print(car2.brand, car2.color)