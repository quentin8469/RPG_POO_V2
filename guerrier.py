from personnage import Personnage


class Warrior(Personnage):
    """
    docstring
    """

    def __init__(self, name):
        """ initialiation of a warrior """
        super().__init__(name)
        print(f"I am {self.name} a warrior")
