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
        print(f"Coucou je suis {self.name}")

    def presentation(self):
        print(f"Nom: {self.name}, Points de vie: {self.life}")

    def attacks(self, ennemy):
        """ function for attacks an ennemy """
        print(f"{self.name} attack {ennemy.name}")

    def protection(self):
        """ function for attacks protection """
        print(f"{self.name} se protege")
