from socket import *
from config import *


class Server(object):
    def __init__(self, port=PORT, listen_count=1):
        self.port = port
        self.listen_count = listen_count
        self.server = socket(AF_INET, SOCK_STREAM)

    def __call__(self, *args, **kwargs):
        self.server.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        self.server.bind(("", self.port))
        self.server.listen(self.listen_count)

        print("Server is live on port {0}".format(self.port))

        client, addr = self.server.accept()
        print("{0} is connected".format(addr))

        while True:
            print("Waiting for messages...")
            message = client.recv(2048).decode()
            print(message)

            if message == 'exit':
                client.close()
                self.server.close()
                break

            client.sendall(input("Send a message back! Send 'exit' to quit. ").encode())

    def __del__(self):
        self.server.close()
        print("Bye bye.")


if __name__ == "__main__":
    server = Server()
    server()
