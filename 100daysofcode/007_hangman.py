import random

from replit import clear

lives_left = 6
words = [
    "basketball",
    "baboon",
    "awkward",
    "mouse",
    "personality",
]

word = random.choice(words)
correct_letters = set(word)
guessed = set()

print(
    r"""
 _
| |
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |
                   |___/
"""
)

lives_6 = """
  +---+
  |   |
      |
      |
      |
      |
=========
"""
lives_5 = """
  +---+
  |   |
  O   |
      |
      |
      |
=========
"""
lives_4 = """
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
"""
lives_3 = """
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
"""
lives_2 = r"""
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
"""
lives_1 = r"""
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
"""
lives_0 = r"""
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
"""

lives = [lives_0, lives_1, lives_2, lives_3, lives_4, lives_5, lives_6]


def print_word(word: str, letters: set):
    print(" ".join(c if c in letters else "_" for c in word))


is_game_over = False
while correct_letters != guessed and lives_left > 0:
    print_word(word, guessed)
    guess = input("Guess the letter or substring: ")
    if guess in correct_letters:
        guessed |= set(guess)
        if correct_letters != guessed:
            is_game_over = True
    else:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives_left -= 1
    clear()
    print(lives[lives_left])

if lives_left == 0:
    print("You lost!")
else:
    print("You won!")
