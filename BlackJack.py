import random

# These are the suits, rank and card-values which we will use in the game.
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
card_values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9,
               'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}

# Creating different classes and functions which will be used in the game logic.


class Card:

    """This class is for creating all the cards present in a deck."""

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = card_values[rank]

    def __str__(self):
        return self.rank + " of " + self.suit


class Deck:

    """This class creates a deck of 52 cards and do different operations like shuffling and removing cards."""

    def __init__(self):
        self.all_cards = []
        for x in suits:
            for y in ranks:
                created_card = Card(x, y)
                self.all_cards.append(created_card)

    def __str__(self):
        deck_contents = []
        for card in self.all_cards:
            deck_contents.append(str(card))
        return str(deck_contents)

    def shuffle(self):
        random.shuffle(self.all_cards)

    def give_one(self):
        try:
            r = random.choice(self.all_cards)
            self.all_cards.remove(r)
            return r
        except:
            print("No more cards.")


class Player:

    """This class will be used to perform certain actions by the player."""

    def __init__(self, amount=100):
        self.has_cards = []
        self.value = 0
        self.aces = 0
        self.amount = amount
        self.bet = 0

    def add_card(self, card):
        self.has_cards.append(card)
        self.value += card_values[card.rank]
        if card.rank == 'Ace':
            self.aces += 1
        while self.value > 21 and self.aces > 0:
            self.value -= 10
            self.aces -= 1

    def win_bet(self):
        self.amount += self.bet

    def lose_bet(self):
        self.amount -= self.bet


def take_bet(player):
    while True:
        try:
            player.bet = int(input("How many chips do you want to bet? \n"))
        except:
            print("Please enter an integer value!")
        else:
            if player.bet > player.amount:
                print("Sorry you don't have enough chips to bet!\nYou have {} chips available".format(player.amount))
            else:
                break
    return player.bet


def hit(hand, deck):
    hand.add_card(deck.give_one())


def hit_or_stand(player, deck):
    global playing
    while playing:
        choice = input("\nHit or Stand?\nEnter 'H' or 'S': ")
        if choice.lower() == 'h' or choice.lower() == 'hit':
            hit(player, deck)

        elif choice.lower() == 's' or choice.lower() == 'stand':
            print("Player STANDS!, Dealer's Turn")
            playing = False
        else:
            print("Sorry! that's not a valid input, please select 'H' or 'S'")
            continue
        break


def show_some(player, dealer):
    print("\nYou have:")
    print(*player.has_cards, sep="\n")
    print("\nDealer has:")
    print("<Card Hidden>", end="\n")
    print(*dealer.has_cards[1:], sep="\n")


def show_all(player, dealer):
    print("\nYou have:")
    print(*player.has_cards, sep="\n")
    print(f"\nPlayer's hand total value = {player.value}")
    print("\nDealer has:")
    print(*dealer.has_cards, sep="\n")
    print(f"\nDealer's hand total value = {dealer.value}")


def player_wins(player, dealer):
    print("\nPlayer Wins!")
    player.win_bet()
    dealer.lose_bet()


def dealer_wins(player, dealer):
    print("\nDealer Wins!")
    dealer.win_bet()
    player.lose_bet()


def player_busts(player, dealer):
    print("\nPlayer BUSTS! Dealer Wins")
    player.lose_bet()
    dealer.win_bet()


def dealer_busts(player, dealer):
    print("\nDealer BUSTS! Player Wins")
    dealer.lose_bet()
    player.win_bet()


def push():
    print("\nIt's a Tie! PUSH")


while True:
    print("\nWELCOME TO BLACKJACK\nTry to get as close as possible to 21 without going over!")
    print("Dealer hits until she reaches 17. Aces count as 1 or 11.")

    player1 = Player()
    computer = Player()

    game_deck = Deck()
    game_deck.shuffle()

    player1.add_card(game_deck.give_one())
    player1.add_card(game_deck.give_one())
    computer.add_card(game_deck.give_one())
    computer.add_card(game_deck.give_one())
    print("\n")
    print(f"\nYou bet for {take_bet(player1)} chips.")

    show_some(player1, computer)

    playing = True
    while playing:
        hit_or_stand(player1, game_deck)
        show_some(player1, computer)
        if player1.value > 21:
            player_busts(player1, computer)
            break

    if player1.value <= 21:
        while computer.value < 17:
            hit(computer, game_deck)

        show_all(player1, computer)

        if computer.value > 21:
            dealer_busts(player1, computer)
        elif computer.value < player1.value:
            player_wins(player1, computer)
        elif computer.value > player1.value:
            dealer_wins(player1, computer)
        else:
            push()

    print("\nPlayer's total chips stands at", player1.amount)

    # Ask to play again
    new_game = input("\nWould you like to play another hand? Enter 'Y' or 'N': ")

    if new_game[0].lower() == 'y':
        playing = True
        continue
    else:
        print("\nThanks for playing!")
        break
