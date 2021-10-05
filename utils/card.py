class Symbol:
    # Parent class
    """
    This class is created to initiate the icons and colors of the deck.
    """

    def __init__(self, color: str , icon):
        self.color = color
        self.icon = icon


class Card(Symbol):
    # Child class
    """
    This class is created to initiate the values of the deck.
    This class is inherits from Symbol class.
    """

    def __init__(self, color, icon, value):
        super().__init__(color, icon)
        self.value = value
