
from personnage import Person
from guerrier import Warrior
from mage import Wizzard
from voleur import Rogue
from arene import Arena
from potion import Potion


if __name__ == "__main__":
    """ """
    # instanciation des personnages
    warrior = Warrior("Edgar")
    warrior.presentation()
    wizzard = Wizzard("Tristan")
    wizzard.presentation()
    # instanciation de l'arene avec les personnages
    arena = Arena(wizzard, warrior)
    # Début du combat
    arena.battle()
