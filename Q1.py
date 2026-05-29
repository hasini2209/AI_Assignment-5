#Q1. Implement the Minimax search algorithm, Alpha-Beta search, Heuristic alpha-beta search, and Monte-Carlo Tree search. 
import math
import random

board = [" " for _ in range(9)]

# Display Board
def print_board(board):
    print()
    for i in range(0, 9, 3):
        print(board[i] + " | " + board[i+1] + " | " + board[i+2])
    print()

# Check Winner
def check_winner(board, player):
    win_positions = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]

    for pos in win_positions:
        if board[pos[0]] == board[pos[1]] == board[pos[2]] == player:
            return True

    return False

# Check Draw
def is_draw(board):
    return " " not in board

# Minimax Algorithm
def minimax(board, depth, is_maximizing):

    if check_winner(board, "X"):
        return 1

    if check_winner(board, "O"):
        return -1

    if is_draw(board):
        return 0

    if is_maximizing:
        best_score = -math.inf

        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(board, depth + 1, False)
                board[i] = " "
                best_score = max(score, best_score)

        return best_score

    else:
        best_score = math.inf

        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(board, depth + 1, True)
                board[i] = " "
                best_score = min(score, best_score)

        return best_score

# Alpha-Beta Pruning
def alpha_beta(board, depth, alpha, beta, is_maximizing):

    if check_winner(board, "X"):
        return 1

    if check_winner(board, "O"):
        return -1

    if is_draw(board):
        return 0

    if is_maximizing:
        best_score = -math.inf

        for i in range(9):

            if board[i] == " ":
                board[i] = "X"

                score = alpha_beta(
                    board,
                    depth + 1,
                    alpha,
                    beta,
                    False
                )

                board[i] = " "

                best_score = max(best_score, score)
                alpha = max(alpha, best_score)

                if beta <= alpha:
                    break

        return best_score

    else:
        best_score = math.inf

        for i in range(9):

            if board[i] == " ":
                board[i] = "O"

                score = alpha_beta(
                    board,
                    depth + 1,
                    alpha,
                    beta,
                    True
                )

                board[i] = " "

                best_score = min(best_score, score)
                beta = min(beta, best_score)

                if beta <= alpha:
                    break

        return best_score

# Heuristic Function
def heuristic(board):

    if check_winner(board, "X"):
        return 10

    elif check_winner(board, "O"):
        return -10

    return 0

# Heuristic Alpha-Beta
def heuristic_alpha_beta(
    board,
    depth,
    alpha,
    beta,
    is_maximizing,
    max_depth
):

    score = heuristic(board)

    if abs(score) == 10 or depth == max_depth or is_draw(board):
        return score

    if is_maximizing:

        best = -math.inf

        for i in range(9):

            if board[i] == " ":
                board[i] = "X"

                best = max(
                    best,
                    heuristic_alpha_beta(
                        board,
                        depth + 1,
                        alpha,
                        beta,
                        False,
                        max_depth
                    )
                )

                board[i] = " "

                alpha = max(alpha, best)

                if beta <= alpha:
                    break

        return best

    else:

        best = math.inf

        for i in range(9):

            if board[i] == " ":
                board[i] = "O"

                best = min(
                    best,
                    heuristic_alpha_beta(
                        board,
                        depth + 1,
                        alpha,
                        beta,
                        True,
                        max_depth
                    )
                )

                board[i] = " "

                beta = min(beta, best)

                if beta <= alpha:
                    break

        return best

# Monte Carlo Simulation
def monte_carlo_move(board, player):

    empty = [i for i in range(9) if board[i] == " "]

    return random.choice(empty)

# Initial Board
board = [
    "X", "O", "X",
    "O", "X", " ",
    " ", " ", "O"
]

print("Initial Board:")
print_board(board)

# Minimax Result
print("Minimax Evaluation:",
      minimax(board, 0, True))

# Alpha-Beta Result
print("Alpha-Beta Evaluation:",
      alpha_beta(board, 0, -math.inf, math.inf, True))

# Heuristic Alpha-Beta Result
print("Heuristic Alpha-Beta Evaluation:",
      heuristic_alpha_beta(
          board,
          0,
          -math.inf,
          math.inf,
          True,
          3
      ))

# Monte Carlo Move
move = monte_carlo_move(board, "X")

print("Monte Carlo Suggested Move:", move)
