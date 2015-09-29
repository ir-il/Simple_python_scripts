from random import randint

board = []

for x in range(0, 5):
    board.append(["O"] * 5)


def print_board(board):
    for row in board:
        print(" ".join(row))

print_board(board)


def random_row(board):
    return randint(0, len(board) - 1)


def random_col(board):
    return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)

# Where our ship is
print("Ship is located on: row %s, col %s" % (ship_row, ship_col))

# A loop for 4 turns of guessing
for turn in range(4):
    print("Turn: %s" % (turn+1))
    # user's choice
    while True:
        guess_row = input("Guess Row (from 0 to 4): ")
        if len(guess_row) == 0:
            print("Please, enter a number from 0 to 4")
            continue
        else:
            try:
                guess_row = int(guess_row)
                break
            except:
                print("Oops!  That was no valid number.  Try again...")
                continue
    while True:
        guess_col = input("Guess Col (from 0 to 4): ")
        if len(guess_col) == 0:
            print("Please, enter a number from 0 to 4")
            continue
        else:
            try:
                guess_col = int(guess_col)
                break
            except:
                print("Oops!  That was no valid number.  Try again...")
                continue
    # Write your code below!
    if guess_row == ship_row and guess_col == ship_col:
        print("Congratulations! You sank my battleship from the %s attempt!" % turn)
        break
    else:
        if guess_row not in range(5) or guess_col not in range(5):
            print("Oops, that's not even in the ocean.")
        elif board[guess_row][guess_col] == "X":
            print("You guessed that one already.")
        else:
            print("You missed my battleship!")
            board[guess_row][guess_col] = "X"
            print_board(board)
        if turn == 3:
            print("Game Over")