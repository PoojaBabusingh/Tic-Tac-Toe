#STEPS for building tic tac toe#
# create board
# display -  board
# play game
# handle turn
# check win
# check rows
# check columns
# check diagonals
# check tie
# flip player


# Global variables
game_still_going = True  # if game is still going on then true else false
winner = None  # who won x or o or tie
current_player = "X"  # starting the game with X

# Game board
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]


# to display the board
def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])


def play_game():
    # display the board at first
    display_board()

    # while the game is still going on
    while game_still_going:
        # handle a single turn of an arbitary player
        handle_turn(current_player)

        # check if the game has ended
        check_if_game_over()

        # Flip to other player
        flip_player()

    if winner == "X" or winner == "0":
        print(winner + " won.")
    elif winner == None:
        print("Its a tie")


def check_if_game_over():
    check_for_winner()
    check_if_tie()


def check_for_winner():
    global winner
    # check rows
    row_winner = check_rows()
    # check colums
    column_winner = check_columns()
    # check diagonals
    diagonal_winner = check_diagonals()

    if row_winner:
        # there was a win
        winner = row_winner
    elif column_winner:
        # there was a win
        winner = column_winner
    elif diagonal_winner:
        # there was a win
        winner = diagonal_winner
    else:
        # there was no win
        winner = None
    return


def check_rows():
    # to atlter global variables
    global game_still_going

    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"

    if row_1 or row_2 or row_3:
        game_still_going = False

    if row_1:
        return board[0]
    if row_2:
        return board[3]
    if row_3:
        return board[6]
    return


def check_columns():

    global game_still_going

    column_1 = board[0] == board[3] == board[6] != "-"
    column_2 = board[1] == board[4] == board[7] != "-"
    column_3 = board[2] == board[5] == board[8] != "-"

    if column_1 or column_2 or column_3:
        game_still_going = False

    if column_1:
        return board[0]
    if column_2:
        return board[1]
    if column_3:
        return board[2]
    return


def check_diagonals():

    global game_still_going

    diagonals_1 = board[0] == board[4] == board[8] != "-"
    diagonals_2 = board[2] == board[4] == board[6] != "-"

    if diagonals_1 or diagonals_2:
        game_still_going = False
    if diagonals_1:
        return board[0]
    if diagonals_2:
        return board[2]
    return


def check_if_tie():

    global game_still_going

    if "-" not in board:
        game_still_going = False
    return


def flip_player():

    global current_player

    # if player is X change it to O
    if current_player == "X":
        current_player = "O"
    # if player is O change it to X
    if current_player == "O":
        current_player = "X"
    return


def handle_turn(player):

    print(player + "'s turn now ")
    position = input("Choose the position from 1 - 9 : ")

    valid = False
    while not valid:
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input(
                "Invalid input. Choose the position from 1 - 9 : ")

        position = int(position) - 1  # index start from 1

        if board[position] == "-":
            valid = True
        else:
            print("You cant go there, choose a different spot")

    board[position] = player

    display_board()


play_game()
