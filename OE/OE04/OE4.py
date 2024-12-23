class Character:
    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power

    def attack(self, target):
        damage = self.power
        target.health -= damage
        print(f"{self.name} attacks {target.name} for {damage} damage. {target.name}'s health is now {target.health}.")

    def special_move(self):
        pass

    def defend(self, attacker):
        damage_reduction = self.power // 2
        actual_damage = max(attacker.power - damage_reduction, 0)
        self.health -= actual_damage
        print(f"{self.name} defends against {attacker.name}'s attack. Damage reduced to {actual_damage}. {self.name}'s health is now {self.health}.")

class Warrior(Character):
    def __init__(self, name, health, power):
        super().__init__(name, health, power)
        self._next_attack_multiplier = 1

    def attack(self, target):
        damage = self.power * self._next_attack_multiplier
        target.health -= damage
        print(f"{self.name} attacks {target.name} with enhanced power for {damage} damage. {target.name}'s health is now {target.health}.")
        self._next_attack_multiplier = 1

    def special_move(self):
        print(f"{self.name} uses Shield Bash! Power doubled for the next attack.")
        self._next_attack_multiplier = 2

class Mage(Character):
    def special_move(self):
        damage = 100
        print(f"{self.name} casts Fireball! It deals {damage} damage directly.")
        self.power += damage

class Archer(Character):
    def special_move(self):
        print(f"{self.name} shoots a Piercing Arrow! Damage bypasses defenses.")
        self.power+=25

class Monster(Character):
    def special_move(self):
        health_gain = 50
        self.health += health_gain
        print(f"{self.name} roars and gains {health_gain} extra health! Health is now {self.health}.")


warrior = Warrior("Warrior", 150, 20)
mage = Mage("Mage", 100, 30)
archer = Archer("Archer", 120, 25)
monster = Monster("Monster", 200, 40)


characters = [warrior, mage, archer]

for character in characters:
    character.attack(monster)
    character.special_move()

monster.special_move()

for character in characters:
    monster.attack(character)
    monster.special_move()



all_characters = characters + [monster]
for char in all_characters:
    char.special_move()
