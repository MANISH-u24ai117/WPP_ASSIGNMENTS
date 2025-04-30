import random
import numpy as np

N = 8

def print_solution(board):
    for row in board:
        print(" ".join("Q" if col else "." for col in row))
    print("\n")

def is_safe(board, row, col):
    for i in range(row):
        if board[i][col]:
            return False
    
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j]:
            return False
    
    for i, j in zip(range(row, -1, -1), range(col, N)):
        if board[i][j]:
            return False
    
    return True

def place_queens_randomly():
    board = np.zeros((N, N), dtype=int)
    rows = list(range(N))
    cols = list(range(N))
    random.shuffle(cols)
    
    for row, col in enumerate(cols):
        if is_safe(board, row, col):
            board[row][col] = 1
        else:
            return None  # Failed placement
    
    return board

def find_random_solution():
    board = None
    while board is None:
        board = place_queens_randomly()
    print_solution(board)

find_random_solution()
