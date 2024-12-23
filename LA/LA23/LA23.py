class AnimeCharacter:
    def __init__(self, name, ability):
        self.name = name
        self.ability = ability

    def introduce(self, func):
        def wrapper_method():
            print("Introducing...")
            func()
            print("This character is amazing!")
        return wrapper_method
    
anime = AnimeCharacter("Zhou Yuan", "Mysthic Saint Body")

@anime.introduce
def character_intro():
    print(f"{anime.name} is a charater with of ability of {anime.ability}")

character_intro()