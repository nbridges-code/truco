import socket

ClientSocket = socket.socket()
host = '127.0.0.1'
port = 1233

print('Waiting for connection')
try:
    ClientSocket.connect((host, port))
except socket.error as e:
    print(str(e))

username = input("Please enter a username:")
ClientSocket.send(str.encode(username))
Response = ClientSocket.recv(1024)
print(Response.decode('utf-8'))

while True:
    Input = input('enter command (\"help\" for command usage): ')
    if Input == "exit":
        ClientSocket.close()
        exit()
    ClientSocket.send(str.encode(Input))
    Response = ClientSocket.recv(1024)
    print(Response.decode('utf-8'))

