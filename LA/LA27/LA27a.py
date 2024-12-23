from abc import ABC, abstractmethod
class NinjaTurtle(ABC):
    @property
    @abstractmethod
    def name(self):
        pass
class Leonardo(NinjaTurtle):
    def __init__(self, real_name, alias):
        self.real_name = real_name
        self.__alias = alias
    @property
    def name(self):
        return self.__alias
class Michaelangelo(NinjaTurtle):
    def __init__(self, real_name, alias):
        self.real_name = real_name
        self.__alias = alias
    @property
    def name(self):
        return self.__alias
class Donatello(NinjaTurtle):
    def __init__(self, real_name, alias):
        self.real_name = real_name
        self.__alias = alias
    @property
    def name(self):
        return self.__alias
class Raphael(NinjaTurtle):
    def __init__(self, real_name, alias):
        self.real_name = real_name
        self.__alias = alias
    @property
    def name(self):
        return self.__alias
if __name__ == "__main__":
    leonardo = Leonardo("Leonard", "Leopard")
    print(leonardo.name)