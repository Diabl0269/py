from socket import *
from config import PORT

server = socket(AF_INET, SOCK_STREAM)

server.bind(("", PORT))
server.listen()

print("Socket is live!")

client, addr = server.accept()
print("Client connected from: {0}".format(addr))

while True:
    try:
        data = client.recv(2048).decode()
        print("Data from client: {0}".format(data))
        client.sendall("Message received".encode())

        if data == 'exit':
            client.close()
            break

    except:
        socket.close()
