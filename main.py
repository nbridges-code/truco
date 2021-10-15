from Deck import Deck
from Player import Player


def main():
    deck = Deck()
    players = [Player(), Player(), Player(), Player()]
    for i in range(0, 4):
        for j in range(0, 3):
            players[i].take_card(deck.draw())

    count = 0
    for p in players:
        count = count + 1
        print("Player " + str(count) + " has:")
        p.toString()
        print("\n")


if __name__ == "__main__":
    main()
