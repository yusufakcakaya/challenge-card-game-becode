import player
from player import Player


class Board:
    def __init__(self,
                 players,
                 turn_count: int,
                 active_cards,
                 history_cards
                 ):
        self.players = players
        self.turn_count = turn_count
        self.active_cards = active_cards
        self.history_cards = history_cards


    def start_game(self):
        """
        Start the game,
        Fill a Deck,
        Distribute the cards of the Deck to the players.
        Make each Player play() a Card, where each player should only play 1 card per turn, and all players have to play at each turn until they have no cards left.
        At the end of each turn, print:
        The turn count.
        The list of active cards.
        The number of cards in the history_cards.

        """
        return 0
