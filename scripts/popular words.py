import csv

import requests
from bs4 import BeautifulSoup

response = requests.get("https://slovotvir.org.ua/popular")
soup = BeautifulSoup(response.text, "lxml")
words_table = soup.find("table", id="words")

data = []
for row in words_table.find_all("tr"):
    word, translate, *_ = row.find_all("td")
    data.append(
        {
            "word": word.text.strip(),
            "translate": translate.text.strip().split("\n")[-1],
        }
    )

with open("ukrainian_words.csv", mode="w") as f:
    writer = csv.DictWriter(f, ["word", "translate"])
    writer.writeheader()
    writer.writerows(data)
