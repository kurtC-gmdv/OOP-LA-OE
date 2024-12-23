from  abc import ABC, abstractmethod
class Character(ABC):
    @property
    @abstractmethod
    def alias(self):
        pass

class Spiderman(Character):
    def __init__(self, real_name, alias):
        self.real_name = real_name
        self.__alias = alias

    @property
    def alias(self):
        return self.__alias

spiderman = Spiderman("Peter Parker", "Spiderman")
print(spiderman.alias)