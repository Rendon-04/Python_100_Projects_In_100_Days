import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

draw = '''
    _______
---'   ____)
      (____)
       __________)
      (____)
---.__(___)
'''
choices = ["rock", "paper", "scissors"]
display = {"rock": rock , "paper": paper, "scissors": scissors, "draw": draw}

user_choice = input("Choose rock, paper, scissors").lower()
if user_choice in choices:
    print(display[user_choice])
random_choice = random.choice(choices)
print("Computer chose: ")
print(random_choice)
print(display[random_choice])

# rock beats scissors
# paper beats rock
# scissors beat paper

if user_choice == "rock" and random_choice == "scissors":
    # print(display[0])
    # print(display[2])
    print("You won")
elif user_choice == "scissors" and random_choice == "paper":
    # print(display[2])
    # print(display[1])
    print("You won")
elif user_choice == "paper" and random_choice == "rock":
    # print(display[1])
    # print(display[0])
    print("You won")
elif user_choice == random_choice:
    print("Its a draw")
    # print(display[3])
else:
    print("Please type in a valid word, no numbers")