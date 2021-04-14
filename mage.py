from personnage import Person


class Wizzard(Person):
    """
    docstring
    """

    max_life = 200

    def __init__(self, name):
        """ initialitation of a wizzard"""
        super().__init__(name, 200, "Mage", 5, 20, 20)

    def drink_potion(self, potion):
        """ drink heal potion """
        if self.life < Wizzard.max_life:
            print(Wizzard.max_life)
            print("Besoin de potions")
        else:
            # print(Wizzard.max_life)
            print("pas besoin de potions")
