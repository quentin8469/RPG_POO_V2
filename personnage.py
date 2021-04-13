import random


class Person:
    """
    docstring
    """

    max_life = 100

    def __init__(
        self, name, life=100, classe="", strength=10, intelligence=10, mana=10
    ):
        """ initialation of a person """
        self.name = name
        self.life = life
        self.classe = classe
        self.strength = strength
        self.intelligence = intelligence
        self.init = random.randrange(1, 10)
        self.mana = mana

    def presentation(self):
        print(
            f"Nom: {self.name}, Classe: {self.classe}, Points de vie: {self.life}, initiative:{self.init}"
        )

    def attacks(self, ennemy):
        """ function for attacks an ennemy """
        if self.classe == "":
            degats = self.strength
            return degats
        if self.classe == "Guerrier":
            degats = self.strength * 2
            return degats
        if self.classe == "Mage":
            degats = self.mana * 2
            return degats
        if self.classe == "Voleur":
            degats = self.strength + self.intelligence
            print(f"{self.name} attack {ennemy.name} and do {degats} PV")
            return degats

    def protection(self):
        """ function for attacks protection """

        print(f"{self.name} se protege")
