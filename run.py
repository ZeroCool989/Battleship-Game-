import random

#Build 8x8 game board
board = []
for x in range (8):
    board.append(["O" * 8])

#Display board
def print_board(board):
    for row in board:
        print(" ".join(row))
print_board(board)