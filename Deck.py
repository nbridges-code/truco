import random
from Card import Card


def buildCardsList():
    cardsList = []
    # Add 1-7 for every suit
    for num in range(1, 8):
        for suit in range(1, 5):
            cardsList.append(Card(num, suit))
    for num in range(11, 14):
        for suit in range(1, 5):
            cardsList.append(Card(num, suit))
    return cardsList


class Deck:

    def __init__(self):
        self.cards = buildCardsList()
        random.shuffle(self.cards)

    # Anticipates a single card
    def put_card_in_deck(self, card):
        self.cards.append(card)

    # Anticipates a list of cards
    def put_cards_in_deck(self, cards):
        self.cards.extend(cards)

    def draw(self):
        first = self.cards[0]
        self.cards = self.cards[1:]
        return first

    def reset_and_shuffle(self):
        self.__init__()
