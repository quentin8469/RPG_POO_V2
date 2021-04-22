# coding: utf-8

from arene import Arena
from choice_class import ChoiceClass


if __name__ == "__main__":
    """ """
    choice = ChoiceClass()
    print("Create your playeur!!")
    player_choice = choice.choose_class()
    player = choice.get_class(player_choice)
    player.presentation()
    print(f"{player.name} you can now create your enemy!!")
    enemy_choice = choice.choose_class()
    enemy = choice.get_class(enemy_choice)
    enemy.presentation()
    arena = Arena(player, enemy)
    arena.battle()
