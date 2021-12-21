from Deck import Deck
from Player import Player

class GameState:
    def __init__(self):
        self.deck = Deck()
        self.players = []

    


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

anotherTurn = True
currentBet = 1
while anotherTurn:
    for p in range(0, 4):
        print("Pot is " + str(currentBet))
        print("Player " + str(p) + "'s turn\n")
#           Other players shouldn't have access to this menu
        print("Press [t] for truco\n")
        count = 0
        for c in players[p].get_cards():
            count = count + 1
            print("Select [" + str(count) + "] for " + c.toString())
        userIn = input("What will you do?")

        if userIn == "t":
            print("Player " + str(p) + " calls truco! Does Player " + str(p+1) + " accept?")
        #   TODO: Give next player the ability to accept or decline truco
            if True:
                print("Player " + str(p+1) + " accepts!")
                currentBet = currentBet + 2
            else:
                print("Player " + str(p + 1) + " declines!")
        else:

            while True:
                if userIn != "1" and userIn != "2" and userIn != "3":
                    userIn = "Invalid input. Go again:"
                else:
                    break

            if userIn == "1":
                print("Player " + str(p) + " plays " + players[p].drop_card(0).toString())
            elif userIn == "2":
                print("Player " + str(p) + " plays " + players[p].drop_card(1).toString())
            elif userIn == "3":
                print("Player " + str(p) + " plays " + players[p].drop_card(2).toString())
