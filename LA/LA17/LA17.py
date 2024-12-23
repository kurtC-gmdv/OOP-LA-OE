class Player:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, target):
        if self.health <= 0:
            print(f"{self.name} can't attack because he/she is dead")
            return
        if target.health <= 0:
            print(f"{target.name} is already defeated.")
            return

        target.health -= self.attack_power
        print(f"{self.name} attacks {target.name} for {self.attack_power} damage.")

        if target.health > 0:
            print(f"{target.name}'s remaining health: {target.health}")
        else:
            print(f"{target.name} has been defeated!")

    def heal(self, amount):
        if self.health <= 0:
            print(f"{self.name} can't give heal he/she is dead")
            return

        self.health += amount
        print(f"{self.name} heals for {amount} points. Current health: {self.health}")


player1 = Player("Argus", 100, 15)
player2 = Player("Miya", 120, 20)

player1.attack(player2)

if player1.health > 0:
    print(f"{player1.name} is the winner!")
elif player2.health > 0:
    print(f"{player2.name} is the winner!")
else:
    print("Both players are defeated!")
