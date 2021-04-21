from personnage import Person


class Warrior(Person):
    """
    Create a warrior
    """

    max_life = 400

    def __init__(self, name):
        """ initialisation of a warrior """
        super().__init__(name, 400, "Guerrier", 20, 10, 15)

    def attacks(self):
        """ """
        degats = self.strength * 2
        return degats


    def drink_potion(self, potion):
        """ drink heal potion """
        if self.life < Warrior.max_life:
            self.life = self.life + potion.hp
            if self.life > Warrior.max_life:
                self.life = Warrior.max_life
            print(self.life)
            print("vous avez pris une potions")
        else:
            print(self.life)
            print("pas besoin de potions")
