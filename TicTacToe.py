import random


class Player:

    def __init__(self, symbol):

        self.symbol = symbol

    def __str__(self):

        return f"Player with symbol {self.symbol}"

    def play(self, board):

        while True:

            player_position = input("Select a position [1-9]: ")

            if player_position.isdigit():
                if int(player_position) in range(1, 10):
                    if board[int(player_position)] == ' ':
                        board[int(player_position)] = self.symbol
                        break
                    elif board[int(player_position)] != ' ':
                        print("Sorry! that position is already filled up.")
                else:
                    print("Select a value between 1 & 9 only!")
                    continue
            else:
                print("Please select a digit [1-9]")
                continue


class Computer:

    def __init__(self, symbol):

        self.symbol = symbol

    def __str__(self):

        return f"Computer player with symbol {self.symbol}"

    def play(self, board, pl_symbol):

        available_positions = [x for x, letter in enumerate(board) if letter == ' ' and x != 0]
        corner_positions = [1, 3, 7, 9]
        edge_positions = [2, 4, 8, 6]
        middle_position = 5

        for i in range(1, 10):
            if board[i] == ' ':
                testing_board = board.copy()
                testing_board[i] = self.symbol
                if win_check(testing_board, self.symbol):
                    board[i] = self.symbol
                    return i

        for s in range(1, 10):
            if board[s] == ' ':
                testing_board = board.copy()
                testing_board[s] = pl_symbol
                if win_check(testing_board, pl_symbol):
                    board[s] = self.symbol
                    return s

        corners_available = []
        for i in available_positions:
            if i in corner_positions:
                corners_available.append(i)
        if len(corners_available) > 0:
            move = random.choice(corners_available)
            board[move] = self.symbol
            return move

        if board[middle_position] == ' ':
            board[middle_position] = self.symbol
            return middle_position

        edges_available = []
        for v in available_positions:
            if v in edge_positions:
                edges_available.append(v)
        if len(edges_available) > 0:
            r_c = random.choice(edges_available)
            board[r_c] = self.symbol
            return r_c


def display_game(board):
    print(f"  {board[7]}  |  {board[8]}  |  {board[9]}  ")
    print("-----------------")
    print(f"  {board[4]}  |  {board[5]}  |  {board[6]}  ")
    print("-----------------")
    print(f"  {board[1]}  |  {board[2]}  |  {board[3]}  ")


def mode_selection():
    while True:

        mode = input(
            "Which mode do you want to play?\nPress '1' for single player mode  |   Press '2' for two players mode: ")

        if mode.isdigit():

            if int(mode) == 1:
                print("\nSINGLE PLAYER MODE\n")
                return 1
            elif int(mode) == 2:
                print("\nTWO PLAYERS MODE\n")
                return 2
            else:
                print("Please enter a valid input.")
                continue

        else:
            print("Please enter a valid input.")
            continue


def symbol_selection():
    while True:
        s_choice = input("What do you want to be?\n'X' or 'O': ")
        print("\n")

        if s_choice.lower() == 'x':
            print("You selected 'X'\nYou (X) will go first. Computer (O) will go second.")
            return 'X'
        elif s_choice.lower() == 'o':
            print("You selected 'O'\nComputer (X) will go first. You (O) will go second.")
            return 'O'
        else:
            print("Sorry I didn't understood.\nPlease select 'X' or 'O'")
            continue


def win_check(board, symbol):

    if board[1] == board[2] == board[3] == symbol:
        win = True
    elif board[4] == board[5] == board[6] == symbol:
        win = True
    elif board[7] == board[8] == board[9] == symbol:
        win = True
    elif board[1] == board[4] == board[7] == symbol:
        win = True
    elif board[2] == board[5] == board[8] == symbol:
        win = True
    elif board[3] == board[6] == board[9] == symbol:
        win = True
    elif board[1] == board[5] == board[9] == symbol:
        win = True
    elif board[3] == board[5] == board[7] == symbol:
        win = True
    else:
        win = False

    return win


def draw_check(board):
    for i in range(1, 10):
        if board[i] == ' ':
            return False
    else:
        return True


def replay():
    while True:
        ch = input("Do you want to play again?\n'Y' or 'N': ")
        if ch.lower() == 'y' or ch.lower() == 'yes':
            return True
        elif ch.lower() == 'n' or ch.lower() == 'no':
            return False
        else:
            print("Sorry! I didn't understood, please select 'Y' for 'Yes' and 'N' for 'No'.")
            continue


def single_player_game():

    player_symbol = symbol_selection()
    print("\n")
    if player_symbol == 'X':
        computer_symbol = 'O'
    else:
        computer_symbol = 'X'

    real_player = Player(player_symbol)
    comp_player = Computer(computer_symbol)

    display_game(board_list)
    print("\n")

    game_on = True
    while game_on:

        if player_symbol == 'X':

            print(f"Your Turn ({player_symbol})")
            real_player.play(board_list)
            print('\n')
            display_game(board_list)
            print('\n')
            if win_check(board_list, player_symbol):
                print("HURRAY! YOU WON THE GAME :)\n")
                break
            elif draw_check(board_list):
                print("IT'S A TIE!\n")
                break

            print(f"Computer's Turn ({computer_symbol})")
            comp_player.play(board_list, player_symbol)
            print('\n')
            display_game(board_list)
            print('\n')
            if win_check(board_list, computer_symbol):
                print("OOPS! YOU LOST THE GAME :(\n")
                break
            elif draw_check(board_list):
                print("IT'S A TIE!\n")
                break

        elif player_symbol == 'O':

            print(f"Computer's Turn ({computer_symbol})")
            comp_player.play(board_list, player_symbol)
            print('\n')
            display_game(board_list)
            print('\n')
            if win_check(board_list, computer_symbol):
                print("OOPS! YOU LOST THE GAME :(\n")
                break
            elif draw_check(board_list):
                print("IT'S A TIE!\n")
                break

            print(f"Your Turn ({player_symbol})")
            real_player.play(board_list)
            print('\n')
            display_game(board_list)
            print('\n')
            if win_check(board_list, player_symbol):
                print("HURRAY! YOU WON THE GAME :)\n")
                break
            elif draw_check(board_list):
                print("IT'S A TIE!\n")
                break


def two_players_game():

    player_1 = Player('X')
    player_2 = Player('O')
    print("Player One (X) will go first.")
    print("\n")
    display_game(board_list)
    print("\n")

    game_on = True
    while game_on:

        print("Player One's turn (X)")
        player_1.play(board_list)
        print('\n')
        display_game(board_list)
        print('\n')
        if win_check(board_list, 'X'):
            print("HURRAY! Player One (X) WON THE GAME :)\n")
            break
        elif draw_check(board_list):
            print("IT'S A TIE!\n")
            break

        print("Player Two's turn (O)")
        player_2.play(board_list)
        print('\n')
        display_game(board_list)
        print('\n')
        if win_check(board_list, 'O'):
            print("HURRAY! Player Two (O) WON THE GAME :)\n")
            break
        elif draw_check(board_list):
            print("IT'S A TIE!\n")
            break


if __name__ == '__main__':

    while True:

        print('\n')
        print("WELCOME TO TIC TAC TOE !")
        print('\n')

        desired_mode = mode_selection()

        print("To choose a position, please refer the table below: ")
        print('\n')
        ins_list = ['#', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        display_game(ins_list)
        print('\n')
        input("Press enter to continue")
        print('\n')
        board_list = ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

        if desired_mode == 1:
            single_player_game()

        else:
            two_players_game()

        if not replay():
            print("\nTHANKS FOR PLAYING !\n")
            break
