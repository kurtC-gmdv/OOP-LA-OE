class Party:
    def __init__(self, theme, foods, special_dish):
        self.theme = theme 
        self.foods = foods 
        self.special_dish = special_dish
    def foodList(self):
        return f"Party Theme: {self.theme} Foods: {self.foods}, {self.special_dish}"
    def __secret_dish(self):
        print(f"Adobong Lugaw")
    def show_secretDish(self):
        self.__secret_dish
        

party1 = Party("Pool Party", "Chips", "Cocktails")
party2 = Party("Halloween Part", "Chocalates", "Marshmallows")
party3 = Party("Graduation Party", "Cordon Bleau", "A5 Wagyu Steak")

print(f"""
{party1.foodList()}
{party2.foodList()}
{party3.foodList()}
""")