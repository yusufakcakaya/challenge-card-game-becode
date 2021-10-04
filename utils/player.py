from card import Card
import random


class Player:
    def __init__(self,
                 player_name: str,
                 cards,
                 turn_count: int,
                 number_of_cards: int,
                 history: list
                 ):
        self.player_name = player_name
        self.cards = cards  # this is equivalent to the cards that the player has in his hands
        self.turn_count = turn_count  # which is an int starting at 0.
        self.number_of_cards = number_of_cards
        self.history = history



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
        colors = ["black","red"]
        
        for icon in icons:
            if color = "black"
            for value in values:
                self.card.append(Card(icon,value))
        return 0

    def shuffle(self):
        """
        method that will shuffle all the list of cards.

        """

        return 0

    def distribute(self):
        """
        that will take a list of Player as parameter and
        will distribute the cards evenly between all the players.

        """

        return 0


