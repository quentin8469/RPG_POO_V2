from personnage import Personnage


class Rogue(Personnage):
    """
    docstring
    """

    def __init__(self, name):
        """ initialitation of a rogue"""
        super().__init__(name)
        print(f"I am {self.name} a rogue")
