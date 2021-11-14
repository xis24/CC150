from enum import Enum
import random


class Suit(Enum):
    CLUB = 1
    DIAMOND = 2
    HEART = 3
    SPADE = 4


class Card:
    def __init__(self, value, suit: Suit) -> None:
        self.value = value
        self.suit = suit


class Deck:
    def __init__(self) -> None:
        self.cards = list(Card)
        for suit in Suit._member_map_.keys():
            for i in range(1, 14):
                self.cards.append(Card(i, suit))

    # deal one card
    def deal(self) -> Card:
        return self.pop()

    # deal multiple cards
    def deal(self, numberOfCards):
        dealCards = []
        for _ in range(numberOfCards):
            dealCards.append(self.deal())
        return dealCards

    def shuffle(self):
        size = len(self.cards)
        for i in range(len(self.cards)):
            j = random.randint(size - i) + i
            self.cards[i], self.cards[j] = self.cards[j], self.cards[i]
