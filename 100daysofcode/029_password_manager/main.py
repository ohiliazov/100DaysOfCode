import csv
import random
import string
import tkinter as tk
from tkinter import messagebox

import pyperclip


def generate_password():
    password_list = [
        *random.choices(string.ascii_letters, k=random.randint(8, 10)),
        *random.choices(string.punctuation, k=random.randint(2, 4)),
        *random.choices(string.digits, k=random.randint(2, 4)),
    ]
    random.shuffle(password_list)
    password = "".join(password_list)

    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)
    pyperclip.copy(password)


def store_data():
    website = website_entry.get().strip()
    username = username_entry.get().strip()
    password = password_entry.get().strip()

    if not website or not username or not password:
        messagebox.showerror(title=website, message="Please fill all entries.")
    else:
        is_ok = messagebox.askokcancel(title=website, message="Are you sure?")

        if is_ok:
            with open("data.csv", mode="a") as file:
                writer = csv.writer(file)
                writer.writerow([website, username, password])

            website_entry.delete(0, tk.END)
            password_entry.delete(0, tk.END)


window = tk.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

image = tk.PhotoImage(file="logo.png")
canvas = tk.Canvas(
    width=200,
    height=200,
    highlightthickness=0,
)
canvas.create_image(100, 100, image=image)
canvas.grid(row=0, column=1)

website_label = tk.Label(text="Website:")
website_label.grid(row=1, column=0, sticky=tk.E)

username_label = tk.Label(text="Email/Username:")
username_label.grid(row=2, column=0, sticky=tk.E)

password_label = tk.Label(text="Password:")
password_label.grid(row=3, column=0, sticky=tk.E)

website_entry = tk.Entry(width=50)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()

username_entry = tk.Entry(width=50)
username_entry.grid(row=2, column=1, columnspan=2)
username_entry.insert(0, "test@gmail.com")

password_entry = tk.Entry(width=25)
password_entry.grid(row=3, column=1)

generate_password_btn = tk.Button(
    text="Generate Password",
    width=20,
    command=generate_password,
)
generate_password_btn.grid(row=3, column=2)

add_btn = tk.Button(text="Add", width=47, command=store_data)
add_btn.grid(row=4, column=1, columnspan=2)

window.mainloop()
