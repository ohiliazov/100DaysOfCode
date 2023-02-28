art = r'''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************'''
print(art)
crossroad_choice = input(
    "Welcome to Treasure Island.\n"
    "Your mission is to find the treasure.\n"
    'You\'re at a cross road. Where do you want to go? Type "left" or "right"\n'
)

if crossroad_choice == "right":
    print("You fell into a hole. Game Over.")
    exit()

if crossroad_choice != "left":
    print("The road dead-ended halfway up the mountain. Game Over.")
    exit()

lake_choice = input(
    "You've come to a lake. "
    "There is an island in the middle of the lake. "
    'Type "wait" to wait for a boat. '
    'Type "swim" to swim across.\n'
)

if lake_choice == "swim":
    print("You get attacked by an angry trout. Game Over.")
    exit()

if lake_choice != "wait":
    print("You get attacked by a deadly starting_positions. Game Over.")
    exit()

island_choice = input(
    "You arrive at the island unharmed. "
    "There is a house with 3 doors. "
    "One red, one yellow and one blue. "
    "Which colour do you choose?\n"
)

if island_choice == "red":
    print("🔥🔥🔥 It's a room full of fire. Game Over. 🔥🔥🔥")
    exit()

if island_choice == "yellow":
    print("🗝️🗝️🗝 You found the treasure! You Win! 🗝️🗝️🗝")
    exit()

if island_choice == "blue":
    print("👹👹👹 You enter a room of beasts. Game Over. 👹👹👹")
    exit()

print("You chose a door that doesn'writer exist. Game Over.")
