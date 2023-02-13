

import random

from deck import Deck

def simulate_game() -> (Deck, Deck, Deck, int):
    full_deck = Deck.new()
    full_deck.shuffle()
    player1, player2 = full_deck.split(2)

    turns = 0
    while (not player1.is_empty()) and (not player2.is_empty()):
        turns += 1

        card1 = player1.pop()
        card2 = player2.pop()
        cards = [card1, card2]

        # problem statement does not provide any ordering for
        # the cards, so randomising it
        random.shuffle(cards)

        if card1 > card2:
            player1.add_to_bottom(cards)
        elif card2 > card1:
            player2.add_to_bottom(cards)
    
    return full_deck, player1, player2, turns

def gather_data(n = 1000):
    turn_freqs = {}
    num_cards_left_freq = {}

    for _ in range(n):
        _, p1, p2, turns = simulate_game()
        turn_freqs.setdefault(turns, 0)
        turn_freqs[turns] += 1
        
        num_cards = p1.num_cards() + p2.num_cards()
        num_cards_left_freq.setdefault(num_cards, 0)
        num_cards_left_freq[num_cards] += 1

    return turn_freqs, num_cards_left_freq
