class FavoriteFood:
    def __init__(self, name, ingredient1, ingredient2, ingredient3):
        self.__name = name
        self.__ingredient1 = ingredient1
        self.__ingredient2 = ingredient2
        self.__ingredient3 = ingredient3

    def __str__(self):
        return f"My favorite food is {self.__name}. Ingredients: {self.__ingredient1}, {self.__ingredient2}, {self.__ingredient3}"
    
food1 = FavoriteFood("Shawarma", "Ground Pork", "Cucumber", "Sauce")
food2 = FavoriteFood("Sinigang", "KangKong", "Sampaloc", "Okra")
food3 = FavoriteFood("Dinuguan","Pork","Vinegar","Spices")

print(f"""
{food1}
{food2}
{food3}
""")