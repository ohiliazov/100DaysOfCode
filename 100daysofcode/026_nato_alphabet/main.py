import pandas as pd

df = pd.read_csv("nato_phonetic_alphabet.csv")

nato_alphabet = {letter: word for _, (letter, word) in df.iterrows()}

name = input("Enter a word: ")

print([nato_alphabet[letter.upper()] for letter in name])
