import random


class Arena:
    """
    docstring
    """

    print("L'Arene est crée")

    def __init__(self, player1, player2):
        """ initialisation of the arena """
        self.player1 = player1
        self.player2 = player2
        print(f"Bonjour {player1.name} et {player2.name} pret pour le combat???")

    def battle(self):
        """ start to fight"""
        print("le combat commence")
        if self.player1.init > self.player2.init:
            print(f"coucou {self.player1.name} tu a l'initiative")
            self.player1.attacks(self.player2)
            print(
                f"{self.player1.name} attack {self.player2.name} and do {self.player1.attacks(self.player2)} PV"
            )
        else:
            print(f"coucou {self.player2.name} tu a l'initiative")
            self.player1.attacks(self.player2)
            print(
                f"{self.player2.name} attack {self.player1.name} and do {self.player2.attacks(self.player1)} PV"
            )
