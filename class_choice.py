class ChoiceClass:
    """ Choose your player class """

    playable_class = ["warrior", "rogue", "wizard"]

    def __init__(self):
        pass

    def choose_class(self):
        """ choose what you want play """
        print(f"Please, do your choice: {ChoiceClass.playable_class}")
        class_name = input("I want play a : ").lower()
        print(f"Hello! So you want play a {class_name}, good choice!!")
        return class_name

    def get_class(self, class_name):
        """ return the class choose by the player """
        if class_name == "warrior":
            from guerrier import Warrior

            name = input("Enter your name: ")
            return Warrior(name)
        elif class_name == "rogue":
            from voleur import Rogue

            name = input("Enter your name: ")

            return Rogue(name)
        elif class_name == "wizard":
            from mage import Wizard

            name = input("Enter your name: ")

            return Wizard(name)
