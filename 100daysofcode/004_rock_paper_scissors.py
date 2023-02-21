import random

art_rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

art_paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""
art_scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

rock_paper_scissors = [art_rock, art_paper, art_scissors]

user_choice = int(
    input("What do you choose? " "Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")
)

if user_choice < 0 or user_choice > 2:
    user_choice = random.randint(0, 2)
    print(f"Invalid choice, randomizing your choice to {user_choice}.")

computer_choice = random.randint(0, 2)

print("You chose:")
print(rock_paper_scissors[user_choice])
print("Computer chose:")
print(rock_paper_scissors[computer_choice])

if (user_choice, computer_choice) in [(0, 2), (1, 0), (2, 1)]:
    print("You win! :)")
elif (user_choice, computer_choice) in [(0, 1), (1, 2), (2, 0)]:
    print("You lost :(")
else:
    print("It's a draw! :|")
