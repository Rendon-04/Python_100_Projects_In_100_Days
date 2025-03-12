from blackjack_art import logo
import random

print(logo)

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
player_cards = []
computer_cards = []

def blackjack_winner():
    blackjack = 21
    if player_total > blackjack:
        print("You went over 21! You lose.")
    elif computer_total > blackjack or player_total > computer_total:
        print("You win!")
    elif player_total < computer_total:
        print("You lose!")
    elif player_total == blackjack:
        print("You win")
    else:
        print("It's a tie!")

def first_player_round(player_total):
    player_deal = random.sample(cards, 2)
    player_total += sum(player_deal)
    player_cards.extend(player_deal)
    print(f"Your cards:{player_cards}, current score: {player_total}")
    return player_total

def player_hit_me(player_total):
    new_card = random.choice(cards)
    player_total += new_card
    player_cards.append(new_card)
    return player_total

def first_computer_hit(computer_total):
    computer_deal = random.sample(cards, 2)
    computer_total += sum(computer_deal)
    computer_cards.extend(computer_deal)
    print(f"Computer's first card: {computer_deal[0]}")
    return computer_total

def computer_hit_me(computer_total):
    new_card = random.choice(cards)
    computer_total += new_card
    computer_cards.append(new_card)
    return computer_total

# HIT ME FUNCTIONS ARE NOT WORKING

while True:

    player_total = 0
    computer_total = 0

    begin_game = input("Dp you want to play a game of Blackjack? Type 'y' or 'n': ")

    if begin_game == 'n':
        break
    player_total =  first_player_round(player_total)
    computer_total = first_computer_hit(computer_total)


    continue_deal = input("Do you want to play another card? Type 'y' or 'n': ").lower()
    if continue_deal == 'y':
        player_total = player_hit_me(player_total)
        computer_total = computer_hit_me(computer_total)
        print(f"Your cards: {player_cards}, current score: {player_total}")
        print(f"Computer's cards: {computer_cards}, current score: {computer_total}")
        blackjack_winner()


    else:
        print(f"Your final hand: {player_cards}, final score: {player_total}")
        print(f"Computer's final hand: {computer_cards}, final score: {computer_total}")
        blackjack_winner()

