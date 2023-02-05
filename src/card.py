

import enum
import functools
from typing import Iterable


class Color(enum.Enum):
    Black = 0
    Red = 1

# Rank/Value
class Rank(enum.Enum):
    Ace = 14
    King = 13
    Queen = 12
    Jack = 11
    No10 = 10
    No9 = 9
    No8 = 8
    No7 = 7
    No6 = 6
    No5 = 5
    No4 = 4
    No3 = 3
    No2 = 2

class Suit(enum.Enum):
    Hearts = 0
    Diamonds = 1
    Clubs = 2
    Spades = 3

@functools.total_ordering
class Card:
    def __init__(self, suit: Suit, rank: Rank):
        self.suit = suit
        self.rank = rank
        if suit == Suit.Hearts or suit == Suit.Diamonds:
            self.color = Color.Red
        else:
            self.color = Color.Black
    
    def __str__(self) -> str:
        return f"{{ suit: {self.suit.name}, color: {self.color.name}, rank: {self.rank.name} }}"

    def __lt__(self, other):
        return self.rank.value < other.rank.value

    def __eq__(self, other):
        return self.rank.value == other.rank.value
