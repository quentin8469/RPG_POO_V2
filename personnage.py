class Personnage:
    """
    docstring
    """

    max_life = 100

    def __init__(
        self,
        name,
        life=100,
    ):
        """ initialation of a person """
        self.name = name
        self.life = life
        print(f"coucou je suis {self.name}")

    def presentation(self):
        print(f"Nom: {self.name}, Points de vie: {self.life}")
