class TekkenCharacter:
    def __init__(self,name,ability):
        self.name = name
        self.ability = ability
    def introduce(self, func):
        def wrapper_method():
            print("introducing...")
            func()
            print("This character is amazing!")
        return wrapper_method

tCharacter = TekkenCharacter("Lili", "Matterhorn Ascension")

@tCharacter.introduce
def char_intro():
    print(f"I am {tCharacter.name} and I can use {tCharacter.ability}")
char_intro()