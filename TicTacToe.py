def display_board(board):
    print('  ' + board[1] + '  |  ' + board[2] + '  |  ' + board[3])
    print('-----------------')
    print('  ' + board[4] + '  |  ' + board[5] + '  |  ' + board[6])
    print('-----------------')
    print('  ' + board[7] + '  |  ' + board[8] + '  |  ' + board[9])


def player_choice():
    x = False

    while not x:
        p_choice = input("What do you want to select 'X' or 'O': ")

        if p_choice.upper() == 'X':
            p_player = 'Player1'
            x = True

        elif p_choice.upper() == 'O':
            p_player = 'Player2'
            x = True

        else:
            print("Sorry! I didn't understood.")
            print("Please select between 'X' or 'O' only.")
            x = False

    print('\n')
    print("You are", p_player)
    print('\n')
    print("Player1 = 'X'\nPlayer2 = 'O'")


def r_position(my_list):
    cp = False

    while not cp:
        pos = input("Select a position: ")

        if pos.isdigit() and int(pos) in range(1, 10):
            if my_list[int(pos)] == ' ':
                cp = True

            elif my_list[int(pos)] != ' ':
                print("Sorry! that position is already filled up.")
                cp = False

        if pos.isdigit() and int(pos) not in range(1, 10):
            print("Please enter a valid position (1-9).")
            cp = False

        if not pos.isdigit():
            print("Sorry!", pos, "is not a digit.")
            print("Please enter a digit (1 - 9).")
            cp = False

    return int(pos)


def replace(list_board, i_position, obj):
    list_board[i_position] = obj

    return list_board


def win_check(board, mark1):
    if board[1] == board[2] == board[3] == mark1:
        p_win = True
    elif board[4] == board[5] == board[6] == mark1:
        p_win = True
    elif board[7] == board[8] == board[9] == mark1:
        p_win = True
    elif board[1] == board[4] == board[7] == mark1:
        p_win = True
    elif board[2] == board[5] == board[8] == mark1:
        p_win = True
    elif board[3] == board[6] == board[9] == mark1:
        p_win = True
    elif board[1] == board[5] == board[9] == mark1:
        p_win = True
    elif board[3] == board[5] == board[7] == mark1:
        p_win = True
    else:
        p_win = False

    return p_win


def draw_check(t_list):
    for i in range(0, 10):
        if t_list[i] == ' ':
            return False
    return True


def replay():
    while True:
        choice = input("Would you like to keep playing? Y or N: ")

        if choice.lower() == 'y':
            game_on_1 = True
            break
        elif choice.lower() == 'n':
            game_on_1 = False
            break
        else:
            print("Sorry! I didn't understood, please select 'y' for 'yes' and 'n' for 'no'.")
            continue

    return game_on_1


board_list = ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']


while True:
    print('\n')
    print("WELCOME TO TIC TAC TOE !")
    print('\n')
    player_choice()
    print('\n')
    input("Press ENTER to continue")
    print('\n')
    print("To choose a position, please refer the table below: ")
    print('\n')
    ins_list = ['#', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    display_board(ins_list)
    print('\n')
    input("Press ENTER to continue")
    print('\n')
    board_list = ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    display_board(board_list)

    game_on = True

    while game_on:

        print('\n')
        print("Player1 (X)'s turn")
        mark = 'X'
        position = r_position(board_list)
        board_list = replace(board_list, position, mark)
        print('\n')
        display_board(board_list)
        win = win_check(board_list, mark)
        draw = draw_check(board_list)
        if draw:
            print('\n')
            print("It's a DRAW")
            print('\n')
            break
        if win:
            print('\n')
            print("Congratulations! Player1(X) wins the game.")
            print('\n')
            break

        print('\n')
        print("Player2 (O)'s turn")
        mark = 'O'
        position = r_position(board_list)
        board_list = replace(board_list, position, mark)
        print('\n')
        display_board(board_list)
        win = win_check(board_list, mark)
        draw = draw_check(board_list)
        if draw:
            print('\n')
            print("It's a DRAW")
            print('\n')
            break
        if win:
            print('\n')
            print("Congratulations! Player2(O) wins the game.")
            print('\n')
            break

    if not replay():
        break
