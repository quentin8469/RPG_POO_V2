class Potion:
    """
    Create a heals potion
    """

    number_max_of_potion = 5

    def __init__(self):
        self.hp = 100
        print("We have", Potion.number_max_of_potion, "potions in the arena")
