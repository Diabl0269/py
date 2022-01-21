class Game(object):
    def __init__(self, max_games=5):
        self.max = max_games
        self.count = 0

    def __call__(self, *args, **kwargs):
        print("Welcome to [r]ock, [p]aper, [s]cissors, each turn choose a symbol by it's first letter.")
        ties = 0
        score1 = 0
        score2 = 0

        while self.count < self.max:
            sign1 = input("Player 1 >")
            sign2 = input("Player 2 >")

            if self.check_tie(sign1, sign2):
                ties += 1

            if self.check_signs(sign1, sign2):
                score1 += 1
                print("Player 1 wins.")

            if self.check_signs(sign2, sign1):
                score2 += 1
                print("Player 2 wins.")

            self.count += 1

        print("Thank you for playing! Player 1: {0}, Player 2: {1}, Ties: {2} :=D".format(score1, score2, ties))

    def check_tie(self, sign1, sign2):
        return sign1 == sign2

    def check_signs(self, sign1, sign2):
        return (sign1 == 'r' and sign2 == 's') or (sign1 == 'p' and sign2 == 'r') or (sign1 == 's' and sign2 == 'p')


if __name__ == "__main__":
    game = Game()
    game()
