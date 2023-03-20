##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.


import datetime
import os
import random
import smtplib

import pandas

EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_USER = os.getenv("EMAIL_USER")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

templates = []

for filename in os.listdir("letter_templates"):
    with open(f"letter_templates/{filename}") as file:
        templates.append(file.read())

today = datetime.date.today()

df = pandas.read_csv("birthdays.csv")

with smtplib.SMTP(EMAIL_HOST, EMAIL_PORT) as connection:
    connection.starttls()
    connection.login(user=EMAIL_USER, password=EMAIL_PASSWORD)

    for idx, (name, email, year, month, day) in df.iterrows():
        if month == today.month and day == today.day:
            message = random.choice(templates).replace("[NAME]", name)

            connection.sendmail(
                from_addr=EMAIL_USER,
                to_addrs=email,
                msg=f"Subject:Happy Birthday\n\n{message}",
            )
