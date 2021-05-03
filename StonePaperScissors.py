import random

my_dict = {1: 'Stone', 2: 'Paper', 3: 'Scissors'}


def select_one():

    while True:
        n = input()
        if n.isdigit():
            if int(n) in range(1, 4):
                return int(n)
            else:
                print("Not a valid number!")
        else:
            print("Please select a number.")


def replay():
    while True:
        choice = input("Would you like to play again?\nSelect 'Y' for 'Yes' and 'N' for 'No': ")

        if choice.lower() == 'y':
            return True
        elif choice.lower() == 'n':
            return False
        else:
            print("Sorry! wrong input.")
            continue


print("WELCOME TO STONE PAPER SCISSORS.")
while True:
    rounds = 1
    comp_wins = 0
    player_wins = 0
    while rounds <= 10:
        print(f"\nRound {rounds}")
        for key, value in my_dict.items():
            print(f"Select '{key}' for '{value}'", end="  |  ")
        player_choice = select_one()
        comp_choice = random.choice(list(my_dict.keys()))
        print(f"Your choice: {my_dict[player_choice]}\nComputer's choice: {my_dict[comp_choice]}\n")
        if player_choice == comp_choice:
            print("TIE!")
        elif player_choice == 1:
            if comp_choice == 2:
                print("YOU LOSE :(")
                comp_wins += 1
            elif comp_choice == 3:
                print("HURRAY! YOU WON :)")
                player_wins += 1
        elif player_choice == 2:
            if comp_choice == 3:
                print("YOU LOSE :(")
                comp_wins += 1
            elif comp_choice == 1:
                print("HURRAY! YOU WON :)")
                player_wins += 1
        elif player_choice == 3:
            if comp_choice == 1:
                print("YOU LOSE :(")
                comp_wins += 1
            elif comp_choice == 2:
                print("HURRAY! YOU WON :)")
                player_wins += 1
        rounds += 1
    print(f"\nYour score: {player_wins}  |  Computer's score: {comp_wins}\n")
    if player_wins > comp_wins:
        print("HURRAY! YOU WON THE GAME :)\n")
    elif player_wins < comp_wins:
        print("OOPS! YOU LOST THE GAME :(\nBETTER LUCK NEXT TIME!\n")
    else:
        print("THE GAME IS DRAWN\n")

    if not replay():
        break
