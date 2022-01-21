from config import *
from socket import *

client = socket(AF_INET, SOCK_STREAM)
client.connect((ADDRESS, PORT))

while True:
    data = input("Enter a message")

    client.sendall(data.encode())

    if data == "exit":
        client.close()
        break

    data = client.recv(2048).decode()
    print("Message from server: {0}".format(data))
