from threading import *
from socket import *
from config import *

clients = []

server = socket(AF_INET, SOCK_STREAM)
server.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
server.bind(("", PORT))
server.listen()


def handle_clients():
    while True:
        try:
            client, addr = server.accept()
            print("Client connected from: {0}".format(addr))
            clients.append(client)

        except ConnectionAbortedError:
            print("Connection aborted from thread")
            break


t = Thread(target=handle_clients)
t.start()

while True:
    command = input("Insert a command to send to all client, [E]xit to quit. ")

    if command == 'E':
        for c in clients:
            c.sendall(command.encode('utf-8'))
            c.close()
        server.close()
        break

    for c in clients:
        c.sendall(command.encode())
