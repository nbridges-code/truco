class Card:
    def __init__(self, number, suit):
        self.number = number
        self.suit = suit

    def toString(self):
        string = "card_"
        string += str(self.number)
        string += "_"

        if self.suit == 1:
            string += "spade.png"
        if self.suit == 2:
            string += "heart.png"
        if self.suit == 3:
            string += "clover.png"
        if self.suit == 4:
            string += "diamond.png"

        return string
