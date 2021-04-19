from personnage import Person


class Wizard(Person):
    """
    Create a Wizard
    """

    max_life = 200

    def __init__(self, name):
        """ initialisation of a wizard"""
        super().__init__(name, 200, "Mage", 5, 20, 20)

    def drink_potion(self, potion):
        """ drink heal potion """
        if self.life < Wizard.max_life:
            self.life = self.life - potion.hp/2
            if self.life > Wizard.max_life:
                self.life = Wizard.max_life
            print(self.life)
            print("vous avez pris une potions")
        else:
            print(self.life)
            print("pas besoin de potions")
