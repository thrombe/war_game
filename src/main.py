
from game import *

def run_game_once():
    _, player1, player2, turns = simulate_game()

    if player1.is_empty() and player2.is_empty():
        print("the game ended in a Tie")
    elif player1.is_empty():
        print("Player 1 wins")
    else:
        print("Player 2 wins")
    
    print(f"game lasted {turns} turns")
    # print(player1)
    # print(player2)


if __name__ == "__main__":
    # deck = Deck.new()
    # print(list(str(d) for d in deck.split(4)))
    # deck.shuffle()
    # d1, d2 = deck.split(2)
    # print(d1.pop() >= d2.pop())
    run_game_once()
    # gather_data()

