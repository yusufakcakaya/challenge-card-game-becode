from utils.game import Board
from utils.player import Player

# Press the green button in the gutter to run the script.
if __name__ == "__main__":

    print("Enter player names:")
    name1 = input("Name: ")
    name2 = input("Name: ")
    name3 = input("Name: ")
    name4 = input("Name: ")

    players_list = [
                    Player(name1),
                    Player(name2),
                    Player(name3),
                    Player(name4)
                   ]

    game1 = Board(players_list)
    game1.start_game()
