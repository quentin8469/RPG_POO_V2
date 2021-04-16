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
        print(
            f"Bonjour {player1.name} le {player1.classe} et {player2.name} le \
{player2.classe} pret pour le combat ???"
        )

    def battle(self):
        """ start to fight"""

        print("Tout les combattants sont dans l'arene, le combat peut commencer!!")
        round_nb = 0
        while self.player1.life > 0 and self.player2.life > 0:
            round_nb += 1
            print("Round:", round_nb)
            self.player1.init = random.randrange(1, 10)
            self.player2.init = random.randrange(1, 10)

            if self.player1.init > self.player2.init:
                print(f"{self.player1.name} tu a l'initiative")
                damage = self.player1.attacks(self.player2)
                print(
                    f"{self.player1.name} attack {self.player2.name} and do \
{damage} of damages"
                )
                self.player2.damage(damage)

            else:
                print(f"{self.player2.name} tu a l'initiative")
                damage = self.player2.attacks(self.player1)
                print(
                    f"{self.player2.name} attack {self.player1.name} and do \
{damage} of damages"
                )
                self.player1.damage(damage)
