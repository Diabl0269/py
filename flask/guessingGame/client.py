import requests
from config import *

url = "http://localhost:{0}".format(PORT)


def start_game():
    r = requests.get("{0}{1}".format(url, START_GAME_URL))
    print(r.text)


def guess_the_number():
    number = int(input("Guess a number between 1 and {0}".format(MAX_NUMBER)))
    r = requests.get("{0}{1}".format(url, GUESS_THE_NUMBER_URL), params={"number": number}).json()
    print(r['message'])
    return r['success']


if __name__ == '__main__':
    start_game()
    success = False

    while not success:
        success = guess_the_number()
