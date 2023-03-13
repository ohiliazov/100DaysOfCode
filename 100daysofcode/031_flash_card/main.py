import random
from tkinter import Button, Canvas, PhotoImage, Tk

import pandas

BACKGROUND_COLOR = "#B1DDC6"
CARD_TITLE_FONT = ("Arial", 40, "italic")
CARD_WORD_FONT = ("Arial", 60, "bold")

try:
    df = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    df = pandas.read_csv("data/ukrainian_words.csv")

data = df.to_dict(orient="records")
current_card = {}
timer_id = ""


def flip_card():
    global current_card
    card_canvas.itemconfig(card_image, image=card_back_image)
    card_canvas.itemconfig(card_title, text="Найкращий переклад", fill="white")
    card_canvas.itemconfig(card_word, text=current_card["translation"], fill="white")


def next_card():
    global current_card, timer_id
    if timer_id:
        window.after_cancel(timer_id)
        timer_id = ""

    current_card = random.choice(data)

    card_canvas.itemconfig(card_image, image=card_front_image)
    card_canvas.itemconfig(card_title, text="Слово", fill="black")
    card_canvas.itemconfig(card_word, text=current_card["word"], fill="black")

    timer_id = window.after(3000, flip_card)


def is_known_card():
    global current_card
    data.remove(current_card)

    df = pandas.DataFrame.from_records(data)
    df.to_csv("data/words_to_learn.csv", index=False)

    next_card()


window = Tk()
window.title("Flashy")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

card_front_image = PhotoImage(file="images/card_front.png")
card_back_image = PhotoImage(file="images/card_back.png")
right_image = PhotoImage(file="images/right.png")
wrong_image = PhotoImage(file="images/wrong.png")

card_canvas = Canvas(
    bg=BACKGROUND_COLOR,
    width=800,
    height=526,
    highlightthickness=0,
)
card_image = card_canvas.create_image(400, 263, image=card_front_image)
card_title = card_canvas.create_text(400, 150, font=CARD_TITLE_FONT)
card_word = card_canvas.create_text(400, 263, font=CARD_WORD_FONT)
card_canvas.grid(row=0, column=0, columnspan=2)

right_button = Button(
    image=right_image,
    bg=BACKGROUND_COLOR,
    highlightthickness=0,
    borderwidth=0,
    command=is_known_card,
)
right_button.grid(row=1, column=0)

wrong_button = Button(
    image=wrong_image,
    bg=BACKGROUND_COLOR,
    highlightthickness=0,
    borderwidth=0,
    command=next_card,
)
wrong_button.grid(row=1, column=1)

next_card()

window.mainloop()
