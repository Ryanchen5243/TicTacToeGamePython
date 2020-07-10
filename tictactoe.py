# Default game board
tictactoe_board = [
    ["  ", "1 ", "2 ", "3 "],
    ["1 ", "- ", "- ", "- "],
    ["2 ", "- ", "- ", "- "],
    ["3 ", "- ", "- ", "- "]
]


# Prints game board
def print_game_board():
    for row in range(len(tictactoe_board)):
        for col in range(len(tictactoe_board[row])):
            print(tictactoe_board[row][col], end='')
        print("\n")


# Checks whether user input [character] is valid-should only be 'X' or 'O'
def is_input_valid(choice):
    if choice.upper() == 'X' or choice.upper() == 'O':
        return True
    else:
        return False


# Checks and returns whether a given move is valid
def is_valid_move(row, column):
    if (is_valid_row(row) and is_valid_column(column) and
            tictactoe_board[int(row)][int(column)] == "- "):
        return True
    else:
        return False


# Checks and returns whether a given row is valid
def is_valid_row(row):
    if row.isalpha() or row == "":
        return False
    elif int(row) > 0 and int(row) < 4:
        return True


# Checks and returns whether a given column is valid
def is_valid_column(column):
    if column.isalpha() or column == "":
        return False
    elif int(column) > 0 and int(column) < 4:
        return True




# Executes move
def execute_move(character, row, column):
    tictactoe_board[row][column] = character + " "


# Computer's Move
def computer_move(character, row, column):
    tictactoe_board[row][column] = character + " "


# Check Win Conditions
def check_win():
    # check rows
    if (tictactoe_board[1][1] == tictactoe_board[1][2] ==
            tictactoe_board[1][3] != "- "):
        return True
    elif (tictactoe_board[2][1] == tictactoe_board[2][2] ==
            tictactoe_board[2][3] != "- "):
        return True
    elif (tictactoe_board[3][1] == tictactoe_board[3][2] ==
            tictactoe_board[3][3] != "- "):
        return True
    # check columns
    elif (tictactoe_board[1][1] == tictactoe_board[2][1] ==
            tictactoe_board[3][1] != "- "):
        return True
    elif (tictactoe_board[1][2] == tictactoe_board[2][2] ==
            tictactoe_board[3][2] != "- "):
        return True
    elif (tictactoe_board[1][3] == tictactoe_board[2][3] ==
            tictactoe_board[3][3] != "- "):
        return True
    # check diagonals
    elif (tictactoe_board[3][1] == tictactoe_board[2][2] ==
            tictactoe_board[1][3] != "- "):
        return True
    elif (tictactoe_board[1][1] == tictactoe_board[2][2] ==
            tictactoe_board[3][3] != "- "):
        return True
    else:
        return False


# resets board
def board_reset():
    tictactoe_board[1][1] = "- "
    tictactoe_board[1][2] = "- "
    tictactoe_board[1][3] = "- "
    tictactoe_board[2][1] = "- "
    tictactoe_board[2][2] = "- "
    tictactoe_board[2][3] = "- "
    tictactoe_board[3][1] = "- "
    tictactoe_board[3][2] = "- "
    tictactoe_board[3][3] = "- "