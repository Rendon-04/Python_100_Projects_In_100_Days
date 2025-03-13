from game_art import logo, vs
from game_data import data
import random

print(logo)

score = 0

play_game = True
while play_game:
    first_random_item = random.choice(data)
    second_random_item = random.choice(data)
    def pick_items_to_compare():
        print(
            f'Compare A: {first_random_item["name"]}, a {first_random_item["description"]}, from {first_random_item["country"]}')
        print(vs)
        print(
            f'Compare B: {second_random_item["name"]}, a {second_random_item["description"]}, from {second_random_item["country"]}')
    pick_items_to_compare()



    def comparison(user_answer):
        global score, play_game
        if user_answer == 'a' and first_random_item['follower_count'] > second_random_item['follower_count']:
            score += 1
            print(f"You're right, your current score is: {score}")
        elif user_answer == 'b' and second_random_item['follower_count'] > first_random_item['follower_count']:
            score += 1
            print(f"You're right, your current score is: {score}")
        else:
            print(f"You're wrong, your final score is: {score}")
            play_game = False
            return


    user_answer = input("Who has more followers, type A or B").lower()
    comparison(user_answer)
