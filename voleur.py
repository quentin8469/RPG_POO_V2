from personnage import Person


class Rogue(Person):
    """
    docstring
    """

    max_life = 300

    def __init__(self, name):
        """ initialitation of a rogue"""
        super().__init__(name, 300, "Voleur", 15, 12, 15)

    def steal(self):
        """ steal a potion """
        print(f"{self.name} à volé la potion")

    def drink_potion(self, potion):
        """ drink heal potion """
        if self.life < Rogue.max_life:
            print(Rogue.max_life)
            print("Besoin de potions")
        else:
            # print(Rogue.max_life)
            print("pas besoin de potions")
