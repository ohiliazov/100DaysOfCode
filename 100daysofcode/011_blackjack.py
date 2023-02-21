import random
from typing import List

import replit

logo = r"""
.------.            _     _            _    _            _
|A_  _ |.          | |   | |          | |  (_)          | |
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   <
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |
      `------'                           |__/
"""

CARD_RANKS = {"2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"}
CARD_SUITS = {"♣", "♦", "♥", "♠"}


class Card:
    def __init__(self, rank: str, suit: str):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f"{self.rank}{self.suit}"


class Hand:
    def __init__(self, cards: List[Card]):
        self.cards = cards

    def __str__(self):
        return " ".join(map(str, self.cards))

    def add(self, card):
        self.cards.append(card)

    def score(self):
        aces_count = 0
        score = 0
        for card in self.cards:
            if card.rank == "A":
                aces_count += 1
                score += 11
            elif card.rank in "JQK":
                score += 10
            else:
                score += int(card.rank)

        # treat aces as 1 until score is lower than 22
        for _ in range(aces_count):
            if score < 22:
                break
            score -= 10
        return score

    def is_blackjack(self) -> bool:
        return len(self.cards) == 2 and self.score() == 21

    def is_bust(self) -> bool:
        return self.score() > 21

    def is_low(self) -> bool:
        return self.score() < 17

    def __eq__(self, other):
        return self.score() == other.score()

    def __lt__(self, other):
        return self.score() < other.score()


def hand_str(hand):
    return " ".join(map(str, hand))


def hand_score(hand) -> int:
    return sum(card.value() for card in hand)


while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    replit.clear()
    print(logo)

    deck = [Card(card, suit) for card in CARD_RANKS for suit in CARD_SUITS]
    random.shuffle(deck)

    dealer_hand = Hand([deck.pop(), deck.pop()])
    user_hand = Hand([deck.pop(), deck.pop()])

    while not user_hand.is_bust() and not user_hand.is_blackjack():
        print(f"Your hand: {user_hand}.")
        print(f"Dealer card: {dealer_hand.cards[0]}.")
        if input("Type 'y' to get another card. Type 'n' to pass: ") != "y":
            break
        user_hand.add(deck.pop())

    while dealer_hand.is_low():
        dealer_hand.add(deck.pop())

    print()
    print(f"Your hand: {user_hand}. Your score is {user_hand.score()}.")
    print(f"Dealer hand: {dealer_hand}. " f"Dealer score is {dealer_hand.score()}.")
    print()
    if user_hand.is_bust():
        print("You went over. You lose 😤.")
    elif user_hand == dealer_hand:
        print("Draw 🙃.")
    elif user_hand.is_blackjack():
        print("You win with a Blackjack 😎.")
    elif dealer_hand.is_blackjack():
        print("You lose, opponent has Blackjack 😱.")
    elif dealer_hand.is_bust():
        print("Opponent went over. You win 😁.")
    elif user_hand > dealer_hand:
        print("You win 😃.")
    else:
        print("You lose 😤.")
