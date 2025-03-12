from guessing_game_art import logo
import random
print(logo)
print("Welcome to the Number Guessing Game!")

number_to_guess = random.randint(1, 100)
print(number_to_guess)

def random_num():
    print("I'm thinking of a number between 1 and 100.")
random_num()

difficulty_level = input("Choose a difficulty. Type 'easy' or 'hard':").lower()

guesses = 10 if difficulty_level == "easy" else 5

not_guessed = True
while not_guessed:
    def easy_pickings():
        global guesses
        global not_guessed

        print(f"You have {guesses} attempts remaining to guesses the number.")

        user_guesses = int(input("make a guess: "))

        if user_guesses > number_to_guess:
            print("You guessed too high, try again.")
        elif user_guesses < number_to_guess:
            print("You guessed too low, try again.")
        else:
            not_guessed = False
            print(f"You guessed the correct number!{number_to_guess}")
            return
        guesses -= 1
    easy_pickings()
if guesses == 0 and not_guessed:
    print(f"You've run out of attempts! The correct number was: {number_to_guess}")


