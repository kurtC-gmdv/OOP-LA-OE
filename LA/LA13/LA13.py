class Animal:
  def __init__(self, name, type):
    self.name = name
    self.type = type
  def describe_animal(self):
    print(f"This animal is {self.name} with the type of {self.type}")

class fish(Animal):
  def __init__(self, name, type):
    super().__init__(name, type)
    self.can_swim = True

animal1 = fish("Nemo", "Clown Fish")
animal1.describe_animal()
print(animal1.can_swim)