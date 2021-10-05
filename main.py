import random
from utils.game import Board
from utils.player import Player


def print_hi(name):
    print(f"Hi, {name}")  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == "__main__":
    players_list = []

    players_list.append(Player("Aubin"))
    players_list.append(Player("Alber"))
    players_list.append(Player("Yusuf"))
    players_list.append(Player("Reena"))

    game1 = Board(players_list)
    game1.start_game()
    game1.play_game()
