# Tic Tac Toe game implementation

import random

# Let's use a list of 9 spaces to represent the board
board = [" " for _ in range(9)]

def print_board(b):
    """ Prints the Tic Tac Toe Board as a 3x3 grid. """
    
    for i in range(3):
        row = " | ".join(b[i*3:(i+1)*3])
        print(" " + row)
        if i < 2:
            print("---+---+---")

def player_move(player):
    "Prompt the player for a move and update the board. """
    while True:
        try:
            pos = int(input("Choose your move (1-9): ")) - 1
            if pos < 0 or pos > 8:
                print("Invalid input. Please enter a number from 1 to 9.")
            elif board[pos] != " ":
                print("That spot is already taken. Try another.")
            else:
                board[pos] = player
                break
        except ValueError:
            print("Invalid input. Please enter a number.")

def check_winner(player):
    """Return True if the given player has won the game."""
    win_conditions = [
        [0, 1, 2],  # Row 1
        [3, 4, 5],  # Row 2
        [6, 7, 8],  # Row 3
        [0, 3, 6],  # Col 1
        [1, 4, 7],  # Col 2
        [2, 5, 8],  # Col 3
        [0, 4, 8],  # Diagonal \
        [2, 4, 6],  # Diagonal /
    ]
    for combo in win_conditions:
        if all(board[i] == player for i in combo):
            return True
    return False

def winner(state):
    """Return 'X' or 'O' if there is a winner on this board; otherwise None."""
    for p in ("X", "O"):
        if check_winner_state(state, p):
            return p
    return None

def minimax(state, player):
    """
    Recursively score the board.
    Returns (score, move_index)
    score: +1  … 'O' (AI) wins
           -1 … 'X' (human) wins
            0 … tie
    """
    win = winner(state)
    if win == "O":      # AI win
        return 1, None
    if win == "X":      # Human win
        return -1, None
    if " " not in state:
        return 0, None  # Tie

    best_score = None
    best_move  = None

    for i in range(9):
        if state[i] != " ":
            continue            # already filled

        # Simulate move
        next_state = state[:]
        next_state[i] = player
        score, _ = minimax(next_state, "X" if player == "O" else "O")

        # If it's AI's turn, we want max; if it's X's, we want min
        score = -score  # neat trick: flip sign instead of branching

        if best_score is None or score > best_score:
            best_score, best_move = score, i

    return best_score, best_move


def check_winner_state(state, player):
    """check_winner() needs the global board, this one works for any state list."""
    win_sets = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]
    return any(all(state[i] == player for i in trio) for trio in win_sets)



def ai_move():
    """Perfect move for 'O' using Minimax."""
    _, move = minimax(board, "O")
    board[move] = "O"
    print(f"AI (O) played at position {move + 1}")


# Main game loop 

if __name__ == "__main__":
    current_player = "X"

    for turn in range(9):
        print_board(board)

        if current_player == "X":
            player_move("X")
        else:
            ai_move()

        print()

        # Check for winner
        if check_winner(current_player):
            print_board(board)
            print(f"Player {current_player} wins! 🎉")
            break

        # Switch player
        current_player = "O" if current_player == "X" else "X"
    else:
        print_board(board)
        print("It's a tie! 🤝")
