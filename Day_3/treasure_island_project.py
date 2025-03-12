print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
first_move = input("Lets get started, would you like to go left or right")
first_move.lower()
if first_move == "left":
    print("Good going, you are safe, lets continue our journey")
else:
    print("Oh no you fell to your doom. Play again.")
    exit()

second_move = input("Would you like to swim or wait?")
second_move.lower()
if second_move == "wait":
    print("Good thinking, patience is key. Let continue.")
else:
    print("Oh no you were attacked by piranhas")
    exit()
third_move = input("This is the home stretch. Which door would you like to open. Red, Blue, or Yellow?")
third_move.lower()

if third_move == "red":
    print("Gahhhh you're buring alive. Game over try again.")
    exit()
elif third_move == "blue":
    print("AHHH you're getting torn about by beasts. Game over try again.")
    exit()
else:
    print("Woohoo! We found the treasure. You're rich! Thanks for playing.")
