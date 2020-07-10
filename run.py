import tictactoe
import random


def run():
    # Default instructions
    print("Let's Play Tic Tac Toe!!!!!")

    # Show default game board
    tictactoe.print_game_board()

    # a -> user consent to continue playing
    a = True
    while a is True:
        # Prompt user to enter either 'X' or 'O'
        user_choice = input("Pick X or O\n").upper()

        while tictactoe.check_win() is False:
            # if user input is not valid - not 'X' or 'O', reprompt them again
            while tictactoe.is_input_valid(user_choice) is False:
                user_choice = input("Please try again! Pick X or O!\n").upper()

            if user_choice == "X":
                computer_choice = "O"
                print("Your pick: X")
                print("Computer pick: O")
            else:
                computer_choice = "X"
                print("Your pick: O")
                print("Computer pick: X")

            r = input("Enter a row: ")
            c = input("Enter a column: ")

            if tictactoe.is_valid_move(r, c):
                print("valid move!")
                r1 = int(r)
                c1 = int(c)
            else:  # If move is invalid, reprompt them again
                while tictactoe.is_valid_move(r, c) is False:
                    print("Sorry, Invalid Move! Please try again!")
                    r = input("Enter a row: ")
                    c = input("Enter a column: ")
                r1 = int(r)
                c1 = int(c)

            tictactoe.execute_move(user_choice.upper(), r1, c1)
            tictactoe.print_game_board()

            # check win condition for user
            tictactoe.check_win()
            if tictactoe.check_win() is True:
                print("You are the winner!!!!")
                break

            print("Computer's Turn!!")
            comp_r = random.randint(1, 3)
            comp_c = random.randint(1, 3)

            if tictactoe.tictactoe_board[comp_r][comp_c] == '- ':
                comp_move_valid = True
            else:
                comp_move_valid = False

            while comp_move_valid is False:
                comp_r = random.randint(1, 3)
                comp_c = random.randint(1, 3)
                if tictactoe.tictactoe_board[comp_r][comp_c] == '- ':
                    break

            tictactoe.computer_move(computer_choice.upper(), comp_r, comp_c)
            print(tictactoe.print_game_board())

            # check win condition for computer
            tictactoe.check_win()
            if tictactoe.check_win() is True:
                print("Computer is the winner!!!!")
                break
        play_again_inquiry = input("Do you want to play again? 'YES' or 'NO'.")
        if play_again_inquiry.upper() == 'NO':
            break
        elif play_again_inquiry.upper() == 'YES':
            print("Awesome!!!")
            tictactoe.board_reset()
        else:
            while (play_again_inquiry.upper() != 'YES' and
                    play_again_inquiry.upper() != 'NO'):
                play_again_inquiry = input("Do you want to play again?")
                if play_again_inquiry.upper() == 'YES':
                    a = True
                    break
                elif play_again_inquiry.upper() == 'NO':
                    a = False
                    break
                else:
                    print("Please answer 'YES' or 'No'!!!")

    print("Thanks for playing!!! Have a wonderful day!")


run()
