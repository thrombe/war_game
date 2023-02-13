
from game import *

def run_game_once():
    _, player1, player2, turns = simulate_game()

    if player1.is_empty() and player2.is_empty():
        print("the game ended in a Tie")
    elif player1.is_empty():
        print("Player 2 wins")
    else:
        print("Player 1 wins")
    
    print(f"game lasted {turns} turns")


if __name__ == "__main__":
    run_game_once()

