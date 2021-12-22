from Card import Card


class Player:
    def __init__(self, Id):
        self.Id = Id
        self.myCards = []

    def get_Id(self):
        return self.Id

    def set_Id(self, Id):
        self.Id = Id

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

    def drop_card(self, index):
        yup = []
        count = 0
        ret = self.myCards[0]
        for i in range(0, 3):
            if i != index:
                yup.append(self.myCards[count])
            else:
                ret = self.myCards[count]
            count = count + 1
        self.myCards = yup
        return ret

    def get_cards(self):
        return self.myCards

    def toString(self):
        myCardsStr = ""
        for card in self.myCards:
            myCardsStr = myCardsStr + card.toString() + "\n"
        return myCardsStr

        # string = ""
        # for card in self.myCards:
        #     string += card.toString()
        #     string += "\n"
