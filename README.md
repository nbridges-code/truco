# truco
Python implementation of Truco card game.
See https://www.pagat.com/put/truco_br.html for rules


_Program use and how it works currently_

Start server with `python3 server.py`
Start client(s) with `python3 client.py`
Use `pip install [library]` for missing dependencies

The server starts first and starts an instance of GameState. When a client connects, they will be prompted to enter a username with which they will be identified. Any user can call the `host` command, which makes them the host. They have the ability to call the `start` command which will deal the cards out. This is the current extent of the start command. `hand` lets them see a string output of their hand.

Upon starting, the server is waiting for connections. When a client starts, they are given a whole new thread on the server. The clients cannot communicate with themselves without first walking through the server. 

The server should do as little manipulation of the game itself as possible. It should only call methods from the GameState. The GameState class is a layer of abstraction to make less work on the server instance. 
A big step in making the game easy to use is figuring out how to make the server send broadcasts to any connected client. 
Something else that needs to get done is that some of the client commands should be allowed to run an arbitrary number of times each turn, and only commands like `use` should end a user's turn.
