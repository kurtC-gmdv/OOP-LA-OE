class MLHero:
  def __init__(self, name, role):
    self.name = name
    self.role = role
  def __str__(self):
    return f"{self.name} is a {self.role} hero"

hero = MLHero("Layla", "Marksman")
print(hero)