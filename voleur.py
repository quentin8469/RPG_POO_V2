from personnage import Person


class Rogue(Person):
    """
    Create a rogue
    """

    max_life = 300

    def __init__(self, name):
        """ initialisation of a rogue"""
        super().__init__(name, 300, "Voleur", 15, 12, 15)

    def steal(self):
        """ steal a potion """
        print(f"{self.name} à volé la potion")

    def protection(self):
        """ """
        return 15

    def drink_potion(self, potion):
        """ drink heal potion """
        if self.life < Rogue.max_life:
            self.life = self.life + potion.hp
            if self.life > Rogue.max_life:
                self.life = Rogue.max_life
            print(f"vous avez pris une potions vous avez mainenant {self.life}")
        else:
            print(self.life)
            print("pas besoin de potions")
