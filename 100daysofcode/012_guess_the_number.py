import random

ATTEMPTS_EASY = 5
ATTEMPTS_HARD = 10

print(
    r"""
   ___                       _____ _                                  _
  / _ \_   _  ___  ___ ___  /__   \ |__   ___   _ __  _   _ _ __ ___ | |__   ___ _ __
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \ | '_ \| | | | '_ ` _ \| '_ \ / _ \ '__|
/ /_\\| |_| |  __/\__ \__ \  / /  | | | |  __/ | | | | |_| | | | | | | |_) |  __/ |
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| |_| |_|\__,_|_| |_| |_|_.__/ \___|_|
    """
)
print("Welcome to Number Guessing Game!")
print("I'm thinking of a number between 1 and 100!")

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
if difficulty not in ["easy", "hard"]:
    raise ValueError("difficulty is not 'easy' or 'hard'")
attempts = ATTEMPTS_EASY if difficulty == "hard" else ATTEMPTS_HARD

number = random.randint(1, 100)

guess = 0
while attempts:
    print(f"You have {attempts} remaining to guess the number.")
    guess = input("Make a guess: ")

    if guess.isdigit():
        guess = int(guess)
        if guess == number:
            break
        elif guess > number:
            print("Too high.")
        else:
            print("Too low.")
    attempts -= 1

if guess == number:
    print(f"You win! The answer was {number}.")
else:
    print(f"You lost. The answer was {number}.")
