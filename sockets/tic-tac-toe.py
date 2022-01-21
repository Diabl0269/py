def main():
    board = [['', '', ''], ['', '', ''], ['', '', '']]
    turn = True

    while True:
        print_board(board)
        line = int(input("Please choose a line with an empty cell: "))
        cell = int(input("Please choose an empty cell: "))

        if board[line][cell] != '':
            print("The cell you chose is taken!")
            continue

        symbol = "X" if turn else "O"

        board[line][cell] = symbol

        winner = check_lines(board)
        print("winner " + str(winner))
        if winner:
            print('{0} wins!'.format(symbol))

        turn = not turn


def check_lines(board):
    for line in board:
        win = True
        old_cell = '';
        for index, cell in enumerate(line):
            if cell == '':
                win = False
                continue

            # First check should always copy the first cell
            if index == 0:
                old_cell = cell

            # If the cells don't match then return False
            if old_cell != cell:
                win = False
                continue

            old_cell = cell

    return win


def print_board(board):
    for line in board:
        print(line)


if __name__ == '__main__':
    main()
