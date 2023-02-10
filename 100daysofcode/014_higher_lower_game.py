import random
import replit
from copy import deepcopy

data = [
    {
        "name": "Instagram",
        "follower_count": 346,
        "description": "Social media platform",
        "country": "United States",
    },
    {
        "name": "Cristiano Ronaldo",
        "follower_count": 215,
        "description": "Footballer",
        "country": "Portugal",
    },
    {
        "name": "Ariana Grande",
        "follower_count": 183,
        "description": "Musician and actress",
        "country": "United States",
    },
    {
        "name": "Dwayne Johnson",
        "follower_count": 181,
        "description": "Actor and professional wrestler",
        "country": "United States",
    },
    {
        "name": "Selena Gomez",
        "follower_count": 174,
        "description": "Musician and actress",
        "country": "United States",
    },
    {
        "name": "Kylie Jenner",
        "follower_count": 172,
        "description": "Reality TV personality and businesswoman and Self-Made Billionaire",
        "country": "United States",
    },
    {
        "name": "Kim Kardashian",
        "follower_count": 167,
        "description": "Reality TV personality and businesswoman",
        "country": "United States",
    },
    {
        "name": "Lionel Messi",
        "follower_count": 149,
        "description": "Footballer",
        "country": "Argentina",
    },
    {
        "name": "Beyoncé",
        "follower_count": 145,
        "description": "Musician",
        "country": "United States",
    },
    {
        "name": "Neymar",
        "follower_count": 138,
        "description": "Footballer",
        "country": "Brasil",
    },
    {
        "name": "National Geographic",
        "follower_count": 135,
        "description": "Magazine",
        "country": "United States",
    },
    {
        "name": "Justin Bieber",
        "follower_count": 133,
        "description": "Musician",
        "country": "Canada",
    },
    {
        "name": "Taylor Swift",
        "follower_count": 131,
        "description": "Musician",
        "country": "United States",
    },
    {
        "name": "Kendall Jenner",
        "follower_count": 127,
        "description": "Reality TV personality and Model",
        "country": "United States",
    },
    {
        "name": "Jennifer Lopez",
        "follower_count": 119,
        "description": "Musician and actress",
        "country": "United States",
    },
    {
        "name": "Nicki Minaj",
        "follower_count": 113,
        "description": "Musician",
        "country": "Trinidad and Tobago",
    },
    {
        "name": "Nike",
        "follower_count": 109,
        "description": "Sportswear multinational",
        "country": "United States",
    },
    {
        "name": "Khloé Kardashian",
        "follower_count": 108,
        "description": "Reality TV personality and businesswoman",
        "country": "United States",
    },
    {
        "name": "Miley Cyrus",
        "follower_count": 107,
        "description": "Musician and actress",
        "country": "United States",
    },
    {
        "name": "Katy Perry",
        "follower_count": 94,
        "description": "Musician",
        "country": "United States",
    },
    {
        "name": "Kourtney Kardashian",
        "follower_count": 90,
        "description": "Reality TV personality",
        "country": "United States",
    },
    {
        "name": "Kevin Hart",
        "follower_count": 89,
        "description": "Comedian and actor",
        "country": "United States",
    },
    {
        "name": "Ellen DeGeneres",
        "follower_count": 87,
        "description": "Comedian",
        "country": "United States",
    },
    {
        "name": "Real Madrid CF",
        "follower_count": 86,
        "description": "Football club",
        "country": "Spain",
    },
    {
        "name": "FC Barcelona",
        "follower_count": 85,
        "description": "Football club",
        "country": "Spain",
    },
    {
        "name": "Rihanna",
        "follower_count": 81,
        "description": "Musician and businesswoman",
        "country": "Barbados",
    },
    {
        "name": "Demi Lovato",
        "follower_count": 80,
        "description": "Musician and actress",
        "country": "United States",
    },
    {
        "name": "Victoria's Secret",
        "follower_count": 69,
        "description": "Lingerie brand",
        "country": "United States",
    },
    {
        "name": "Zendaya",
        "follower_count": 68,
        "description": "Actress and musician",
        "country": "United States",
    },
    {
        "name": "Shakira",
        "follower_count": 66,
        "description": "Musician",
        "country": "Colombia",
    },
    {
        "name": "Drake",
        "follower_count": 65,
        "description": "Musician",
        "country": "Canada",
    },
    {
        "name": "Chris Brown",
        "follower_count": 64,
        "description": "Musician",
        "country": "United States",
    },
    {
        "name": "LeBron James",
        "follower_count": 63,
        "description": "Basketball player",
        "country": "United States",
    },
    {
        "name": "Vin Diesel",
        "follower_count": 62,
        "description": "Actor",
        "country": "United States",
    },
    {
        "name": "Cardi B",
        "follower_count": 67,
        "description": "Musician",
        "country": "United States",
    },
    {
        "name": "David Beckham",
        "follower_count": 82,
        "description": "Footballer",
        "country": "United Kingdom",
    },
    {
        "name": "Billie Eilish",
        "follower_count": 61,
        "description": "Musician",
        "country": "United States",
    },
    {
        "name": "Justin Timberlake",
        "follower_count": 59,
        "description": "Musician and actor",
        "country": "United States",
    },
    {
        "name": "UEFA Champions League",
        "follower_count": 58,
        "description": "Club football competition",
        "country": "Europe",
    },
    {
        "name": "NASA",
        "follower_count": 56,
        "description": "Space agency",
        "country": "United States",
    },
    {
        "name": "Emma Watson",
        "follower_count": 56,
        "description": "Actress",
        "country": "United Kingdom",
    },
    {
        "name": "Shawn Mendes",
        "follower_count": 57,
        "description": "Musician",
        "country": "Canada",
    },
    {
        "name": "Virat Kohli",
        "follower_count": 55,
        "description": "Cricketer",
        "country": "India",
    },
    {
        "name": "Gigi Hadid",
        "follower_count": 54,
        "description": "Model",
        "country": "United States",
    },
    {
        "name": "Priyanka Chopra Jonas",
        "follower_count": 53,
        "description": "Actress and musician",
        "country": "India",
    },
    {
        "name": "9GAG",
        "follower_count": 52,
        "description": "Social media platform",
        "country": "China",
    },
    {
        "name": "Ronaldinho",
        "follower_count": 51,
        "description": "Footballer",
        "country": "Brasil",
    },
    {
        "name": "Maluma",
        "follower_count": 50,
        "description": "Musician",
        "country": "Colombia",
    },
    {
        "name": "Camila Cabello",
        "follower_count": 49,
        "description": "Musician",
        "country": "Cuba",
    },
    {
        "name": "NBA",
        "follower_count": 47,
        "description": "Club Basketball Competition",
        "country": "United States",
    },
]


def print_logo():
    print(
        r"""
    | | | (_) __ _| |__   ___ _ __ 
    | |_| | |/ _` | '_ \ / _ \ '__|
    |  _  | | (_| | | | |  __/ |   
    |_| |_|_|\__, |_| |_|\___|_|   
    _       |___/                 
    | |    _____      _____ _ __   
    | |   / _ \ \ /\ / / _ \ '__|  
    | |__| (_) \ V  V /  __/ |     
    |_____\___/ \_/\_/ \___|_|     
        """
    )


print_logo()
print("Welcome to Higher Lower Game!")

data = deepcopy(data)
random.shuffle(data)

current_item = data.pop()

score = 0


def print_current_item(item):
    name = item["name"]
    description = item["description"]
    country = item["country"]

    print(f"Compare A: {name}, a {description}, from {country}.")


def print_next_item(item):
    name = item["name"]
    description = item["description"]
    country = item["country"]

    print(f"Against B: {name}, a {description}, from {country}")


def print_choices(a, b):
    print_current_item(a)
    print(
        r"""
 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)
        """
    )
    print_next_item(b)


def correct_guess(a, b, answer) -> bool:
    return any(
        [
            a["follower_count"] > b["follower_count"] and answer == "A",
            a["follower_count"] < b["follower_count"] and answer == "B",
        ]
    )


while data:
    next_item = data.pop()

    print_choices(current_item, next_item)

    option = input("Who has more followers? Type 'A' or 'B': ")

    if not correct_guess(current_item, next_item, option):
        break

    score += 1
    current_item = next_item
    replit.clear()
    print_logo()
    print(f"You are right. Current score: {score}.")


if not data:
    print(f"You win! Final score: {score}")
else:
    print(f"Sorry, that's wrong. Final score: {score}")