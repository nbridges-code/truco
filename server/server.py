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

    v = "ayo"
    game = GameState()

    def threaded_client(connection):
        connection.send(str.encode('connected'))
        global v
        while True:
            data = connection.recv(2048)
            v = data.decode('utf-8')
            if v == "exit":
                break
            reply = 'Server Says: ' + v
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