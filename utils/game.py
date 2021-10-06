from utils.player import Deck


class Board:
    def __init__(self, players: list):
        self.Deck = Deck()
        self.players = players
        self.turn_count = 0
        self.active_cards = []
        self.history_cards = []
        self.players_list = []

    def start_game(self):
        """
        - it starts the game,
        - it fills a Deck,
        - it distributes the cards of the Deck to the players.
        - Make each Player play() a Card, where each player should only play 1 card per turn,
         and all players have to play at each turn until they have no cards left.
        - At the end of each turn, print:
         -The turn count.
         -The number of active cards.
         -The number of cards in the history_cards.

        """
        print("Game is starting! Take your seat and good luck!")

        self.Deck.fill_deck()
        self.Deck.shuffle()
        self.Deck.distribute(self.players)

        while self.turn_count < 13:
            self.turn_count += 1
            print(
                f"Turned count is {self.turn_count}, \nActive cards number is {len(self.active_cards)},\nNumber of cards on history is {len(self.history_cards)}"
            )
            self.active_cards.clear()
            for player in self.players:
                card = player.play()
                self.history_cards.append(card)
                self.active_cards.append(card)

        print("Thanks for your playing :)")

