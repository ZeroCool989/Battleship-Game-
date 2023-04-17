import random

#Build 8x8 game board
board = []
for x in range (8):
    board.append(["O" * 8])

#Display board
def print_board(board):
    for row in board:
        print(" ".join(row))

#Defining random position for battleship
def place_ship(board):
    ship_row = random.randit(0, 7)
    ship_col = random.randit(0, 7)
    board[ship_row][ship_col]=" * "
    return(ship_row, ship_col)


