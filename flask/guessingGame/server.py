import random
from flask import Flask, session, request
from config import *

# Initialize
app = server = Flask("Random text")
app.secret_key = "suih*DSiundq9DNILU@uie29823nd="


# secret = 0


@app.route(START_GAME_URL)
def start_game():
    # global secret
    session["secret"] = random.randint(1, MAX_NUMBER)
    print(session.values())
    return "A random number has been selected between 1 and {0}, please guess".format(MAX_NUMBER)


@app.route(GUESS_THE_NUMBER_URL)
def guess_the_number():
    number = int(request.args.get("number"))
    success = False
    print(session.values())
    message = "Hello"
    # if number > session.get("secret"):
    #     message = "Lower"
    # elif number < session['secret']:
    #     message = "Higher"
    # else:
    #     message = "You have guessed the correct number {0}".format(session['secret'])
    #     success = True

    return {"message": message, "success": success}


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=PORT, debug=True)
