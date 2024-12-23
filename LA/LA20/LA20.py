class FavoriteFood:
    def __init__(self, name, ingredient1, ingredient2, ingredient3):
        self.__name = name
        self.ingredient1 = ingredient1
        self._ingredient2 = ingredient2
        self.__ingredient3 = ingredient3
    def __str__(self):
        return f"My favorite food is {self.__name}. Ingredients: {self.__ingredient1}, {self.__ingredient2}, {self.__ingredient3}"
    def may_sauce_ba(self):
        return self.__ingredient3

food1 = FavoriteFood("Shawarma", "Ground Pork", "Cucumber", "Sauce")
print(food1.may_sauce_ba())