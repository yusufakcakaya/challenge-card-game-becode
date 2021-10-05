from card import Card
import random


class Player:
    def __init__(self, name: str, cards, ):

        self.name = name  # it keeps name of the player
        self.cards = cards  # this is equivalent to the cards that the player has in his hands
        self.turn_count = 0  # which is an int starting at 0.
        self.number_of_cards = 0  #which is an int starting at 0
        self.history = []  #which is a list of Card that will contain all the cards played by the player

    def play(self):
        """
        randomly pick a Card in cards.
        Add the Card to the Player's history.
        Print: {PLAYER_NAME} {TURN_COUNT} played: {CARD_NUMBER} {CARD_SYMBOL_ICON}.
        Return the Card.
        """
        return 0


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
        colors = ["black", "red"]

        for icon in icons:
            if icon == icons[0] or icons[3]:
                color = colors[0]
            else:
                color = colors[1]
                for value in values:
                    self.card.append(Card(color, icon, value))

        return Card(color, icon, value)

    def shuffle(self):
        """
        method that will shuffle all the list of cards.

        """
        random.shuffle(self.card)

        return self.card

    def distribute(self):
        """
        that will take a list of Player as parameter and
        will distribute the cards evenly between all the players.

        """
        player1 = []
        player2 = []
        player3 = []
        player4 = []

        for i in range(len(self.card)):
            player1.append(self.card.pop())
            player2.append(self.card.pop())
            player3.append(self.card.pop())
            player4.append(self.card.pop())

        return 0
