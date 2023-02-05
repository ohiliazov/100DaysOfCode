import random
import string

print("Welcome to the PyPassword Generator!")

letters = int(input("How many letters would you like in your password?\n"))
assert 0 <= letters, "number of letters cannot be negative"

symbols = int(input("How many symbols would you like?\n"))
assert 0 <= symbols, "number of symbols cannot be negative"

numbers = int(input("How many numbers would you like?\n"))
assert 0 <= numbers, "number of numbers cannot be negative"

password_list = [
    *random.choices(string.ascii_letters, k=letters),
    *random.choices(string.punctuation, k=symbols),
    *random.choices(string.digits, k=numbers),
]

print(password_list)
random.shuffle(password_list)
print(password_list)

password = "".join(password_list)

print(f"Your password is: {password}")
