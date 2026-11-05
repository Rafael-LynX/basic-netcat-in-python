# Client
import socket

### Create socket
s = socket.socket()

### Define the port
port = 5789


def client_socket_connect():
    try:
        s.connect(("127.0.0.1", port))
        print(s.recv(1024).decode())  # recebe até 1024 bytes de conexão
    except Exception as e:
        print(e)


client_socket_connect()
