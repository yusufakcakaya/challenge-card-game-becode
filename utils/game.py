from utils.player import Deck


class Board:
    def __init__(self,
                 players: list,
                 ):
        self.Deck = Deck()
        self.players = players
        self.turn_count = 0
        self.active_cards = []
        self.history_cards = []

    def play_game(self):
        while self.turn_count < 13:
            self.turn_count += 1
            for player in self.players:
                card = player.play()
                self.history_cards.append(card)
                for index, o in enumerate(self.active_cards):
                    if o.attr == card:
                        del self.active_cards[index]
                        break

    def start_game(self):
        """
       - Start the game,
       - Fill a Deck,
       - Distribute the cards of the Deck to the players.
       - Make each Player play() a Card, where each player should only play 1 card per turn,
        and all players have to play at each turn until they have no cards left.
       - At the end of each turn, print:
        -The turn count.
        -The list of active cards.
        -The number of cards in the history_cards.

        """
        print("Game is starting! Take your seat and enter players name.")

        self.active_cards = self.Deck.fill_deck()
        self.Deck.shuffle()
        self.Deck.distribute(self.players)



