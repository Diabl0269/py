import threading
from socket import *
from config import PORT

lock = threading.Lock()
threads = []

server = socket(AF_INET, SOCK_STREAM)

server.bind(("", PORT))
server.listen()

print("Socket is live!")


def handleClient(client, addr, l):
    print("Client connected from: {0}".format(addr))

    while True:
        data = client.recv(2048).decode()
        print("Data from client: {0}".format(data))

        with l:
            client.sendall("Message received".encode())

        if data == 'exit':
            client.close()
            break


try:
    while True:
        client, addr = server.accept()
        t = threading.Thread(target=handleClient, args=(client, addr, lock))
        threads.append(t)
        t.start()

finally:
    socket.close()
