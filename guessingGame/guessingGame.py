import random

count = 0
number = random.randint(1, 1000)
guess = 0

with open('guessingGame/record.txt', 'r+') as fd:
    isSavedGame = fd.read().find('number') != -1
    fd.seek(0)
    if isSavedGame:
        inp = input("Do you want to proceed the saved game? Y/N")
        if inp.lower() == 'y':
            for line in fd.readlines():
                value = int(line.split(':')[1].split('\n')[0])
                if line.find("count") != -1:
                    count = value
                else:
                    number = value
            print("Found the hidden number, you already tried " + str(count) + " times")

#     Add logic for 'N'

print("Welcome to the guessing game, to exit insert -1")
guess = int(input('Gambler, guess a number!'))
count += 1

while guess != number:
    print("Lower" if guess > number else "Higher")
    guess = int(input('Gambler, guess a number!'))

    if guess == -1:
        with open('guessingGame/record.txt', 'r+') as fd:
            fd.writelines(["number:" + str(number), "\ncount:" + str(count)])
            print("Your record has been saved")
            break

    else:
        count += 1

if guess == number:
    print("You should fill a lottery ticket, you got it right in only " + str(count) + " tries")
    with open('guessingGame/record.txt', 'r+') as fd:
        fd.seek(0)
        fd.truncate()
