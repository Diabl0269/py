import random


class GuessingGame(object):
    count = 0

    def __init__(self, max_num):
        self.max = max_num

    def __call__(self, *args, **kwargs):
        print("Welcome to the guessing game! Please guess a number between 1 - {0}".format(self.max))
        self.secret = random.randint(1, self.max)
        has_guessed_correct = False
        while not has_guessed_correct:
            has_guessed_correct = self.handle_input()

        print("Congratulation, you have guessed the number {0}".format(self.secret))
        self.count += 1

    def __del__(self):
        print("Thank you for playing the guessing game {0} times".format(self.count))

    def handle_input(self):
        num = int(input("Please guess a number: "))
        return self.check_number(num)

    def check_number(self, num):
        if num == self.secret:
            return True

        print("Higher" if num < self.secret else "Lower")
        return False


if __name__ == "__main__":
    game = GuessingGame(10)
    is_playing = True

    while is_playing:
        game()
        is_playing = input("Do you want to proceed playing? [Y]es to proceed") == "Y"
