from personnage import Person


class Warrior(Person):
    """
    docstring
    """

    max_life = 400

    def __init__(self, name):
        """ initialiation of a warrior """
        super().__init__(name, 400, "Guerrier", 20, 10, 15)

    def drink_potion(self, potion):
        """ drink heal potion """
        if self.life < Warrior.max_life:
            print(Warrior.max_life)
            print("Besoin de potions")
        else:
            # print(Warrior.max_life)
            print("pas besoin de potions")
