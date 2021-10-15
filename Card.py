class Card:
    def __init__(self, number, suit):
        self.number = number
        self.suit = suit

    def toString(self):
        string = ""
        if self.number > 10:
            if self.number == 11:
                string += "JACK"
            if self.number == 12:
                string += "QUEEN"
            if self.number == 13:
                string += "KING"
        else:
            string += str(self.number)

        string += " of "

        if self.suit == 1:
            string += "SPADES"
        if self.suit == 2:
            string += "HEARTS"
        if self.suit == 3:
            string += "CLUBS"
        if self.suit == 4:
            string += "DIAMONDS"

        return string
