class MLTeam:
  def __init__(self, name, role, dmg_type):
    self.name = name
    self.role = role
    self.dmg_type = dmg_type
  def __str__(self):
    return f"Name:{self.name} Role: {self.role} Damage Type: {self.dmg_type}"
  def describe_hero(self):
    print(f"{self.name} is {self.role} hero with a damage type of {self.dmg_type}")

hero1 = MLTeam("Suyou", "Fighter/Assassin", "Physical Attack")
hero2 = MLTeam("Bruno", "Marksman", "Physical Attack")
hero3 = MLTeam("Arlott", "Fighter", "Physical Attack")
hero4 = MLTeam("Yve", "Mage", "Magic Damge")
hero5 = MLTeam("Chou", "Tank/Fighter", "Physical Attack")

hero1.describe_hero()
hero2.describe_hero()
hero3.describe_hero()
hero4.describe_hero()
hero5.describe_hero()