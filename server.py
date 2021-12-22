import socket
import os
from _thread import *

from GameState import GameState

def main():
    ServerSocket = socket.socket()
    host = '127.0.0.1'
    port = 1233
    ThreadCount = 0
    try:
        ServerSocket.bind((host, port))
    except socket.error as e:
        print(str(e))

    print('Waiting for a Connection..')
    ServerSocket.listen(5)

    input = "ayo"
    game = GameState()

    def threaded_client(connection):
        # connection.send(str.encode('Please enter a username:'))
        username = connection.recv(2048).decode('utf-8')
        game.newPlayer(username)
        connection.send(str.encode("User " + username + " added\n"))

        global command
        turnEndingCommand = False
        while True:
            data = connection.recv(2048)
            input = data.decode('utf-8')
            output = ""
            command = input.split(" ")[0]
            if command == "exit":
                game.removePlayer(username)
                connection.close()
                exit()
            elif command == "help":
                # print rules and/or full list of commands
                output = '''
Commands:            
exit 
    - Close connection and exit client process
rec 
    - Check for any incoming messages
msg [recipient(s)] [text]
    - Send a message
team
    - Print teammates and current winnings
table 
    - Print current pot and cards played by each player
truco [opponent]
    - Challenge a player with truco
hand
    - Print your current hand
use [number]
    - Use a card from your hand         
host   
    - If a user has not already claimed host, then this will make
        the calling player the host. Print host's name
start
    - (Host Only) Start the game
                '''
            elif command == "rec":
                # recieve a message
                output = ("command not implemented yet")
            elif command == "msg":
                # send a message
                output = ("msg to " + input.split(" ")[1] + "\n sike command not implemented yet")
            elif command == "table":
                # display cards and current betting information
                output = ("command not implemented yet")
            elif command == "truco":
                # initiate truco, make sure current user can actually call
                # it, and that the challenged player can accept or deny.
                # Make accepting or denying part of this command.
                output = ("challenging " + input.split(" ")[1] + "\n sike command not implemented yet")
            elif command == "hand":
                # Print hand
                output = game.getPlayer(username).toString()
            elif command == "host":
                output = game.host(username)
            elif command == "start":
                output = game.gameStart(username)
            elif command == "use":
                # Use a card
                output = ("playing " + input.split(" ")[1] + "\n sike command not implemented yet")
            else:
                output = ("Not a recognized command")

            # match command: 
            #     case "exit":
            #         break
            #     case ""
            reply = 'response: \n' + output
            connection.sendall(str.encode(reply))
        connection.close()

    while True:
        Client, address = ServerSocket.accept()
        print('Connected to: ' + address[0] + ':' + str(address[1]))
        start_new_thread(threaded_client, (Client, ))
        ThreadCount += 1
        print('Thread Number: ' + str(ThreadCount))
    ServerSocket.close()


if __name__ == "__main__":
    main()