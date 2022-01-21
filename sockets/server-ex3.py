import threading
from socket import *
from config import PORT

lock = threading.Lock()
threads = []
clients = []

server = socket(AF_INET, SOCK_STREAM)
server.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
server.bind(("", PORT))
server.listen()

print("Socket is live!")


def handle_client(client, addr, l):
    print("Client connected from: {0}".format(addr))
    clients.append(client)

    while True:
        data = client.recv(2048).decode()

        if data == 'exit':
            client.close()
            clients.remove(client)
            break

        is_error = False
        for c in clients:
            print("Client:" + str(c))
            with l:
                try:
                    c.sendall("Message from {0}: {1}".format(addr, data).encode())
                except Exception:
                    client.close()
                    clients.remove(client)
                    is_error = True
                    print('Error: ' + str(Exception))
                    break

        if is_error:
            client.close()
            break

    print("Sent data to clients")


try:
    while True:
        client, addr = server.accept()
        t = threading.Thread(target=handle_client, args=(client, addr, lock))
        threads.append(t)
        t.start()

finally:
    server.close()
