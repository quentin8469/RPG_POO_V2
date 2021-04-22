class ChoiceClass:
    """ Choose your player class """

    playable_class = ["warrior", "rogue", "wizard"]

    def __init__(self):
        pass

    def choose_class(self):
        """ choose what you want play """
        print(f"faites votre choix: {ChoiceClass.playable_class}")
        class_name = input("Je veux un : ").lower()
        print(f"Hello! So you want play a {class_name}, good choice!!")
        return class_name

    def get_class(self, player_class):
        """ return the class choose by the player """
        pass
