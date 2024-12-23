class MLHero:
  def __init__(self, name, role):
    self.name = name
    self.role = role
  def introduce(self):
    return f"{self.name} is a {self.role} hero"
  def __str__(self):
    return f"{self.name} is a {self.role} hero"

hero = MLHero("Balmond", "Fighter")
print(hero)