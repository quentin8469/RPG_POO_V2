from personnage import Personnage


class Wizzard(Personnage):
    """
    docstring
    """

    def __init__(self, name):
        """ initialitation of a wizzard"""
        super().__init__(name)
        print(f"I am {self.name} a wizzard")
