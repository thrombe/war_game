

import random
from typing import Iterable

from card import Card, Suit, Rank

class Deck:
    def __init__(self, cards: list[Card]):
        '''assuming the card faces are downwards, and the last card is on the top of the deck'''
        self.__cards = cards

    @classmethod
    def new(cls):
        cards = []
        for suit in Suit:
            for rank in Rank:
                card = Card(suit, rank)
                cards.append(card)
        return cls(cards)
    
    def __str__(self) -> str:
        string = "[ \n"
        for card in self.__cards:
            string += f"    {card} \n"
        string += "]"
        return string

    def split(self, number: int):
        '''returns an iterable of Deck with first deck with possibly more cards than the ones that follow it'''
        total = len(self.__cards)
        num = total//number
        cards = self.__cards
        yield Deck(cards[ : num + total - num*number])
        cards = cards[num + total - num*number : ]
        for _ in range(number-1):
            yield Deck(cards[:num])
            cards = cards[num:]

    def shuffle(self):
        random.shuffle(self.__cards)

    def add_to_bottom(self, cards: Iterable[Card]):
        cards = list(cards)
        cards.extend(self.__cards)
        self.__cards = cards
    
    def add_to_top(self, cards: Iterable[Card]):
        for card in cards:
            self.__cards.append(card)

    def pop(self) -> Card | None:
        if len(self.__cards) > 0:
            return self.__cards.pop()
        else:
            return None
    
    def is_empty(self):
        return len(self.__cards) == 0
    
    def num_cards(self):
        return len(self.__cards)
