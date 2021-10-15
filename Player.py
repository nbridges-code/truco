from Card import Card


class Player:
    def __init__(self):
        self.myCards = []

    # Anticipates a singular card
    def take_card(self, card):
        # print("1:" + card.toString())
        self.myCards.append(card)
        # for i in range(0, len(self.myCards)):
        #     print(str(i) + ">" + self.myCards[i].toString())

    # Anticipates a list of cards
    def take_cards(self, cards):
        self.myCards.extend(cards)

    def drop_cards(self):
        ret = self.myCards
        self.__init__()
        return ret

    def toString(self):
        for card in self.myCards:
            print(card.toString() + " ")


        # string = ""
        # for card in self.myCards:
        #     string += card.toString()
        #     string += "\n"
