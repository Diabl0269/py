import threading
from config import *
from socket import *

client = socket(AF_INET, SOCK_STREAM)
client.connect((ADDRESS, PORT))


# Listen for messages
def listen(client, l):
    while True:
        with l:
            print("Listening for messages")

        message = client.recv(2048).decode()

        with l:
            print(message)


lock = threading.Lock()
# Start thread for listening for messages
t = threading.Thread(target=listen, args=(client, lock))
t.daemon = True
t.start()

# Input messages
while True:
    data = input("Enter a message: ")

    with lock:
        client.sendall(data.encode())

    if data == "exit":
        client.shutdown(0)
        break
