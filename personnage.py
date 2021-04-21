class Person:
    """
    Mother class with base attributs
    """

    max_life = 100

    def __init__(
        self, name, life=100, classe="", strength=10, intelligence=10, mana=10
    ):
        """ initialisation of a person """
        self.name = name
        self.life = life
        self.classe = classe
        self.strength = strength
        self.intelligence = intelligence
        self.mana = mana

    def presentation(self):
        print(
            f"Nom: {self.name}, Classe: {self.classe},\
 Points de vie: {self.life}"
        )

    def attacks(self):
        """ function for attacks an enemy """
        if self.classe == "":
            degats = self.strength
            return degats
        if self.classe == "Mage":
            degats = self.mana * 2
            return degats
        if self.classe == "Voleur":
            degats = self.strength + self.intelligence
            return degats

    def protection(self):
        """ function for attacks protection """

        print(f"{self.name} se protege")

    def damage(self, degats):
        """ docstring"""
        if self.life > 0:
            self.life -= degats
            if self.life > 0:
                print(f"{self.name} à encore {self.life} PV")
                return self.life
        if self.life <= 0:
            print(f"{self.name} est mort")

    def escape(self):
        if self.life <= 40:
            print(f"{self.name} run away")

    def drink_potion(self, potion):
        """ drink heal potion """
        if self.life < Person.max_life:
            self.life = self.life + potion.hp
            if self.life > Person.max_life:
                self.life = Person.max_life
            print(self.life)
            print("vous avez pris une potions")
        else:
            print(self.life)
            print("pas besoin de potions")
