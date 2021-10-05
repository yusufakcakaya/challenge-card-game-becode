from utils.card import Card
import random


class Player:
    """
    This class is created to initiate the players
    """

    def __init__(self, name):
        self.name = name    # it keeps name of the player
        self.cards = []     #it keeps the list of icons and symbols
        self.turn_count = 0     # which is an int starting at 0.
        self.number_of_cards = 0    # which is an int starting at 0
        self.history = []   # which is a list of Card that will contain all the cards played by the player

    def set_cards(self, cards):
        self.cards = cards

    def play(self):
        """
        randomly pick a Card in cards.
        Add the Card to the Player's history.
        Print: {PLAYER_NAME} {TURN_COUNT} played: {CARD_NUMBER} {CARD_SYMBOL_ICON}.
        Return the Card.
        """
        random_card = random.choice(self.cards)
        self.history.append(random_card)
        self.cards.remove(random_card)
        self.turn_count += 1
        print(
            f"{self.name},{self.turn_count} played: {random_card.value}{random_card.icon}"
        )

        return Card


class Deck:
    def __init__(self):
        self.card = []

    def fill_deck(self):
        """
        that will fill cards with a complete card game
        (an instance of 'A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K' for each possible
        symbol [♥, ♦, ♣, ♠]).
        """
        icons = ["♠", "♡", "♢", "♣"]
        values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

        for icon in icons:
            if icon == icons[0] or icons[3]:
                color = "Black"
            else:
                color = "Red"
            for value in values:
                self.card.append(Card(color, icon, value))
        return self.card

    def shuffle(self):
        """
        method that will shuffle all the list of cards.

        """
        random.shuffle(self.card)

    def distribute(self, Players):
        """
        that will take a list of Player as parameter and
        will distribute the cards evenly between all the players.

        """

        player1_cards = []
        player2_cards = []
        player3_cards = []
        player4_cards = []

        for i in range(13):
            player1_cards.append(self.card.pop())
            player2_cards.append(self.card.pop())
            player3_cards.append(self.card.pop())
            player4_cards.append(self.card.pop())

        Players[0].set_cards(player1_cards)
        Players[1].set_cards(player2_cards)
        Players[2].set_cards(player3_cards)
        Players[3].set_cards(player4_cards)
