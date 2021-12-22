from GameState import GameState

def main():
    game = GameState()
    
    game.host("poop")

    game.newPlayer("poop")

    print(game.gameStart("poop"))

    print(game.getPlayer("poop").toString())



if __name__ == "__main__":
    main()

