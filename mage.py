from personnage import Person


class Wizzard(Person):
    """
    Create a Wizzard
    """

    max_life = 200

    def __init__(self, name):
        """ initialitation of a wizzard"""
        super().__init__(name, 200, "Mage", 5, 20, 20)

    def drink_potion(self, potion):
        """ drink heal potion """
        if self.life < Wizzard.max_life:
            self.life = self.life + potion.hp
            if self.life > Wizzard.max_life:
                self.life = Wizzard.max_life
            print(self.life)
            print("vous avez pris une potions")
        else:
            print(self.life)
            print("pas besoin de potions")
