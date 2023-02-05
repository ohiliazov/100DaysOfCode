import string


def shift_letter(letter: str, shift: int) -> str:
    if letter not in string.ascii_letters:
        new_letter = letter
    else:
        if letter.isupper():
            letters = string.ascii_uppercase
        else:
            letters = string.ascii_lowercase
        new_letter = letters[(letters.index(letter) + shift) % len(letters)]

    return new_letter


def caesar(message: str, shift: int):
    return "".join([shift_letter(letter, shift) for letter in message])


def run():
    option = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")

    if option not in ["encode", "decode"]:
        print("Wrong option.")
        return

    user_message = input("Type your message:\n")
    user_shift = int(input("Type the shift number:\n"))

    if option == "decode":
        user_shift = -user_shift

    result = caesar(user_message, user_shift)
    print(f"The result is {result}.")


proceed = True
while proceed:
    run()
    choice = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    proceed = choice == "yes"
