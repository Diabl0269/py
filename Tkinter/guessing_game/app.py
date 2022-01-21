import eel
import random

words = ['python', 'javascript', 'pascal', 'program', 'weed']
word = ""
user_guess = ''

eel.init('web')


@eel.expose
def init_game():
    print("Initializing game!")
    global word, user_guess
    word = random.choice(words)
    user_guess = "_" * len(word)
    print("The hidden word is {0}, user guess is {1}".format(word, user_guess))

    return user_guess


@eel.expose
def check_guess(guess):
    print(guess)
    if len(guess) > 1:
        return False

    global user_guess
    for ind, ltr in enumerate(word):
        if guess == ltr:
            user_guess = user_guess[:ind] + ltr + user_guess[ind + 1:]

    return user_guess

    print(guess)


try:
    eel.start('index.html', size=(300, 300), port=0)  # python will select free ephemeral ports.

except (SystemExit, MemoryError, KeyboardInterrupt):
    print("Program Exit")
