import pandas as pd

df = pd.read_csv("nato_phonetic_alphabet.csv")

nato_alphabet = {letter: word for _, (letter, word) in df.iterrows()}

while True:
    name = input("Enter a word: ")

    try:
        print([nato_alphabet[letter.upper()] for letter in name])
        exit()
    except KeyError:
        print("Only letters in the alphabet.")
